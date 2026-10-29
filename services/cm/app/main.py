
from __future__ import annotations
from contextlib import asynccontextmanager
from fastapi import FastAPI, Header, Query
from bank_common import ErrorCode, fail, ok
from app.auth import is_error, require_admin, require_user
from app.schemas import AssignReq, CreateCaseReq, KycUpdateReq, NoteReq, TransitionReq
from app.seed import seed_demo
from app import services
from app.store import STORE
from app.taxonomy import CASE_TYPES, DISPOSITIONS, PRIORITIES
from app.playbooks import get_playbook
from app.knowledge import search_kb

@asynccontextmanager
async def lifespan(_: FastAPI):
    seed_demo()
    yield

app = FastAPI(title="bank-cm", lifespan=lifespan)

@app.get("/health")
def health():
    return ok({"service": "bank-cm", "status": "up", "mode": "full", "case_types": len(CASE_TYPES)})

@app.get("/api/cm/ping")
def ping():
    return ok({"domain": "cm", "message": "case management ready"})

@app.get("/api/cm/meta")
def meta():
    return ok({"case_types": CASE_TYPES, "priorities": PRIORITIES, "dispositions": DISPOSITIONS[:40]})

@app.post("/api/cm/cases")
def create_case(body: CreateCaseReq, authorization: str | None = Header(default=None)):
    payload = require_user(authorization)
    if is_error(payload):
        return payload
    try:
        c = services.create_case(int(payload["uid"]), body.model_dump())
    except services.CmError as exc:
        return fail(ErrorCode.VALIDATION, exc.message)
    return ok(c.to_dict())

@app.get("/api/cm/cases")
def list_cases(authorization: str | None = Header(default=None), status: str | None = None, priority: str | None = None, case_type: str | None = None):
    payload = require_user(authorization)
    if is_error(payload):
        return payload
    uid = None if payload.get("role") == "admin" else int(payload["uid"])
    rows = STORE.list_cases(status=status, priority=priority, user_id=uid, case_type=case_type)
    return ok([c.to_dict(include_notes=False) for c in rows])

@app.get("/api/cm/cases/{case_id}")
def get_case(case_id: str, authorization: str | None = Header(default=None)):
    payload = require_user(authorization)
    if is_error(payload):
        return payload
    c = STORE.get_case(case_id)
    if not c:
        return fail(ErrorCode.NOT_FOUND, "not found")
    if payload.get("role") != "admin" and c.user_id != int(payload["uid"]):
        return fail(ErrorCode.FORBIDDEN, "forbidden")
    return ok(c.to_dict())

@app.post("/api/cm/cases/{case_id}/notes")
def note(case_id: str, body: NoteReq, authorization: str | None = Header(default=None)):
    payload = require_user(authorization)
    if is_error(payload):
        return payload
    try:
        c = services.add_note(case_id, int(payload["uid"]), body.body)
    except services.CmError as exc:
        return fail(ErrorCode.NOT_FOUND if exc.code == "NOT_FOUND" else ErrorCode.VALIDATION, exc.message)
    return ok(c.to_dict())

@app.post("/api/cm/cases/{case_id}/transition")
def transition(case_id: str, body: TransitionReq, authorization: str | None = Header(default=None)):
    payload = require_user(authorization)
    if is_error(payload):
        return payload
    try:
        c = services.transition(case_id, body.status, int(payload["uid"]), body.disposition)
    except services.CmError as exc:
        return fail(ErrorCode.VALIDATION, exc.message)
    return ok(c.to_dict(include_notes=False))

@app.post("/api/cm/cases/{case_id}/assign")
def assign(case_id: str, body: AssignReq, authorization: str | None = Header(default=None)):
    payload = require_admin(authorization)
    if is_error(payload):
        return payload
    try:
        c = services.assign(case_id, body.assignee)
    except services.CmError as exc:
        return fail(ErrorCode.VALIDATION, exc.message)
    return ok(c.to_dict(include_notes=False))

@app.post("/api/cm/kyc")
def kyc_create(authorization: str | None = Header(default=None), customer_id: int = 1):
    payload = require_user(authorization)
    if is_error(payload):
        return payload
    k = services.create_kyc(int(payload["uid"]), customer_id)
    return ok(k.to_dict())

@app.get("/api/cm/kyc")
def kyc_list(authorization: str | None = Header(default=None), status: str | None = None):
    payload = require_user(authorization)
    if is_error(payload):
        return payload
    return ok([k.to_dict() for k in STORE.list_kyc(status=status)])

@app.patch("/api/cm/kyc/{review_id}")
def kyc_update(review_id: str, body: KycUpdateReq, authorization: str | None = Header(default=None)):
    payload = require_admin(authorization)
    if is_error(payload):
        return payload
    try:
        k = services.update_kyc(review_id, body.status, body.checklist, f"admin:{payload['uid']}", body.reason)
    except services.CmError as exc:
        return fail(ErrorCode.NOT_FOUND if exc.code == "NOT_FOUND" else ErrorCode.VALIDATION, exc.message)
    return ok(k.to_dict())

@app.get("/api/cm/admin/metrics")
def admin_metrics(authorization: str | None = Header(default=None)):
    payload = require_admin(authorization)
    if is_error(payload):
        return payload
    return ok(services.metrics())


@app.get("/api/cm/playbooks/{case_type}")
def playbook(case_type: str):
    return ok(get_playbook(case_type))


@app.get("/api/cm/kb")
def kb(q: str = "", limit: int = 20):
    return ok(search_kb(q, limit))
