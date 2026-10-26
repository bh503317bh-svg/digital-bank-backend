
from __future__ import annotations
from typing import Any
from app.models import Case, CaseNote, KycReview, new_id, now_iso
from app.routing import route_queue, suggest_assignee
from app.sla import compute_sla_due, sla_breached
from app.store import STORE
from app.taxonomy import CASE_TYPES, DISPOSITIONS, KYC_CHECKLIST, PRIORITIES
from app.workflow import BadTransition, move

class CmError(Exception):
    def __init__(self, message: str, code: str = "VALIDATION"):
        self.message = message
        self.code = code

def create_case(user_id: int, body: dict[str, Any]) -> Case:
    case_type = body.get("case_type") or CASE_TYPES[0]
    if case_type not in CASE_TYPES:
        raise CmError("invalid case_type")
    priority = body.get("priority") or "P3"
    if priority not in PRIORITIES:
        raise CmError("invalid priority")
    c = Case(
        case_id=new_id("cm"),
        case_type=case_type,
        priority=priority,
        channel=body.get("channel") or "app",
        status="open",
        customer_id=int(body.get("customer_id", 1)),
        user_id=user_id,
        subject=str(body.get("subject") or "Item"),
        description=str(body.get("description") or ""),
        sla_due_at=compute_sla_due(priority),
        tags=list(body.get("tags") or []),
        meta={"queue": route_queue(case_type)},
    )
    if body.get("auto_assign"):
        c.assignee = suggest_assignee(case_type, priority)
        c.status = move(c.status, "assigned")
    STORE.save_case(c)
    return c

def add_note(case_id: str, author_user_id: int, body: str) -> Case:
    c = STORE.get_case(case_id)
    if not c:
        raise CmError("case not found", "NOT_FOUND")
    c.notes.append(CaseNote(note_id=new_id("nt"), author_user_id=author_user_id, body=body))
    c.updated_at = now_iso()
    STORE.save_case(c)
    return c

def transition(case_id: str, target: str, actor: int, disposition: str = "") -> Case:
    c = STORE.get_case(case_id)
    if not c:
        raise CmError("case not found", "NOT_FOUND")
    try:
        c.status = move(c.status, target)
    except BadTransition as exc:
        raise CmError(str(exc)) from exc
    if disposition:
        codes = {d["code"] for d in DISPOSITIONS}
        if disposition not in codes:
            raise CmError("invalid disposition")
        c.disposition = disposition
    c.updated_at = now_iso()
    c.meta["last_actor"] = actor
    c.meta["sla_breached"] = sla_breached(c.sla_due_at)
    STORE.save_case(c)
    return c

def assign(case_id: str, assignee: str) -> Case:
    c = STORE.get_case(case_id)
    if not c:
        raise CmError("case not found", "NOT_FOUND")
    c.assignee = assignee
    if c.status == "open":
        c.status = move(c.status, "assigned")
    c.updated_at = now_iso()
    STORE.save_case(c)
    return c

def create_kyc(user_id: int, customer_id: int) -> KycReview:
    checklist = {k: False for k in KYC_CHECKLIST}
    k = KycReview(
        review_id=new_id("kyc"),
        customer_id=customer_id,
        user_id=user_id,
        status="pending",
        checklist=checklist,
    )
    STORE.save_kyc(k)
    return k

def update_kyc(review_id: str, status: str, checklist: dict | None, reviewer: str, reason: str) -> KycReview:
    k = STORE.kyc.get(review_id)
    if not k:
        raise CmError("kyc not found", "NOT_FOUND")
    if status:
        k.status = status
    if checklist:
        k.checklist.update(checklist)
    k.reviewer = reviewer
    k.reason = reason
    k.updated_at = now_iso()
    STORE.save_kyc(k)
    return k

def metrics() -> dict[str, Any]:
    cases = STORE.list_cases()
    open_c = [c for c in cases if c.status not in {"closed", "resolved"}]
    breached = sum(1 for c in open_c if sla_breached(c.sla_due_at))
    by_pri = {}
    for c in cases:
        by_pri[c.priority] = by_pri.get(c.priority, 0) + 1
    kyc = STORE.list_kyc()
    return {
        "case_count": len(cases),
        "open_cases": len(open_c),
        "sla_breached": breached,
        "by_priority": by_pri,
        "kyc_pending": sum(1 for k in kyc if k.status == "pending"),
        "kyc_total": len(kyc),
    }
