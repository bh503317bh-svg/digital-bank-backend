
from __future__ import annotations
from datetime import datetime
from typing import Any
from app.contact_codes import VALID_RESULTS
from app.models import CollectionCase, ContactLog, new_id, now_iso
from app.scoring import recommend_intensity, recovery_score, stage_for_dpd
from app.store import STORE
from app.strategies import pick_strategies
from app.money import yuan_to_cents
from app.config import settings

class ClError(Exception):
    def __init__(self, message: str, code: str = "VALIDATION"):
        self.message = message
        self.code = code

def open_case(body: dict[str, Any]) -> CollectionCase:
    dpd = int(body.get("dpd", 1))
    principal = yuan_to_cents(body.get("overdue_principal", "0"))
    interest = yuan_to_cents(body.get("overdue_interest", "0"))
    strats = pick_strategies(dpd)
    intensity = recommend_intensity(recovery_score(dpd, principal, 0, 0))
    chosen = next((s for s in strats if s.intensity <= intensity), strats[0] if strats else None)
    c = CollectionCase(
        case_id=new_id("cl"),
        loan_id=str(body.get("loan_id") or new_id("lnref")),
        user_id=int(body.get("user_id", 1)),
        customer_id=int(body.get("customer_id", 1)),
        overdue_principal_cents=principal,
        overdue_interest_cents=interest,
        dpd=dpd,
        stage=stage_for_dpd(dpd),
        status="open",
        assignee=str(body.get("assignee") or "collector_01"),
        strategy_code=chosen.code if chosen else "",
        meta={"recommended_strategies": [s.code for s in strats], "intensity": intensity},
    )
    STORE.save(c)
    return c

def add_contact(case_id: str, body: dict[str, Any], agent: str) -> CollectionCase:
    c = STORE.get(case_id)
    if not c:
        raise ClError("case not found", "NOT_FOUND")
    if c.status in {"paid", "written_off"}:
        raise ClError("case closed")
    # daily contact limit
    today = datetime.utcnow().strftime("%Y-%m-%d")
    today_count = sum(1 for x in c.contacts if x.created_at.startswith(today))
    if today_count >= settings.max_contacts_per_day:
        raise ClError("max contacts per day reached")
    result = body.get("result") or "no_answer_01"
    if result not in VALID_RESULTS:
        # allow bare prefix
        if f"{result}_01" in VALID_RESULTS:
            result = f"{result}_01"
        else:
            raise ClError("invalid contact result")
    promise_cents = yuan_to_cents(body.get("promise_amount", "0")) if body.get("promise_amount") else 0
    log = ContactLog(
        contact_id=new_id("ct"),
        case_id=case_id,
        channel=str(body.get("channel") or "human_call"),
        result=result,
        promise_amount_cents=promise_cents,
        promise_date=str(body.get("promise_date") or ""),
        note=str(body.get("note") or ""),
        agent=agent,
    )
    c.contacts.append(log)
    if result.startswith("promised"):
        c.status = "promised"
    elif result.startswith("refused"):
        c.status = "open"
    success = sum(1 for x in c.contacts if x.result.startswith(("promised", "partial_paid", "app_read")))
    broken = sum(1 for x in c.contacts if x.result.startswith("refused"))
    c.meta["recovery_score"] = recovery_score(c.dpd, c.overdue_principal_cents, success, broken)
    c.updated_at = now_iso()
    STORE.save(c)
    return c

def mark_paid(case_id: str) -> CollectionCase:
    c = STORE.get(case_id)
    if not c:
        raise ClError("case not found", "NOT_FOUND")
    c.status = "paid"
    c.stage = "closed"
    c.updated_at = now_iso()
    STORE.save(c)
    return c

def break_promise(case_id: str) -> CollectionCase:
    c = STORE.get(case_id)
    if not c:
        raise ClError("case not found", "NOT_FOUND")
    if c.status != "promised":
        raise ClError("not in promised status")
    c.status = "broken"
    c.dpd += 1
    c.stage = stage_for_dpd(c.dpd)
    strats = pick_strategies(c.dpd)
    c.strategy_code = strats[0].code if strats else c.strategy_code
    c.updated_at = now_iso()
    STORE.save(c)
    return c

def metrics() -> dict[str, Any]:
    rows = STORE.list()
    by_stage = {}
    by_status = {}
    outstanding = 0
    for c in rows:
        by_stage[c.stage] = by_stage.get(c.stage, 0) + 1
        by_status[c.status] = by_status.get(c.status, 0) + 1
        if c.status not in {"paid", "written_off"}:
            outstanding += c.overdue_principal_cents
    return {
        "case_count": len(rows),
        "by_stage": by_stage,
        "by_status": by_status,
        "outstanding_principal": f"{outstanding / 100:.2f}",
        "strategy_catalog_size": __import__("app.strategies", fromlist=["STRATEGIES"]).STRATEGIES.__len__(),
    }
