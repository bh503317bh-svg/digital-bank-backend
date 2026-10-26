
from __future__ import annotations
from contextlib import asynccontextmanager
from fastapi import FastAPI, Header, Query
from bank_common import ErrorCode, fail, ok
from app.auth import is_error, require_admin, require_user
from app.schemas import ContactReq, OpenCaseReq
from app.seed import seed_demo
from app import services
from app.store import STORE
from app.strategies import STRATEGIES, pick_strategies

@asynccontextmanager
async def lifespan(_: FastAPI):
    seed_demo()
    yield

app = FastAPI(title="bank-cl", lifespan=lifespan)

@app.get("/health")
def health():
    return ok({"service": "bank-cl", "status": "up", "mode": "full", "strategies": len(STRATEGIES)})

@app.get("/api/cl/ping")
def ping():
    return ok({"domain": "cl", "message": "collections ready"})

@app.get("/api/cl/strategies")
def strategies(dpd: int = 30, limit: int = Query(default=10, le=50)):
    rows = pick_strategies(dpd, limit)
    return ok([{"code": s.code, "name": s.name, "channel": s.channel, "intensity": s.intensity, "script": s.script} for s in rows])

@app.post("/api/cl/cases")
def open_case(body: OpenCaseReq, authorization: str | None = Header(default=None)):
    payload = require_user(authorization)
    if is_error(payload):
        return payload
    data = body.model_dump()
    if payload.get("role") != "admin":
        data["user_id"] = int(payload["uid"])
    try:
        c = services.open_case(data)
    except services.ClError as exc:
        return fail(ErrorCode.VALIDATION, exc.message)
    return ok(c.to_dict())

@app.get("/api/cl/cases")
def list_cases(authorization: str | None = Header(default=None), status: str | None = None, stage: str | None = None):
    payload = require_user(authorization)
    if is_error(payload):
        return payload
    uid = None if payload.get("role") == "admin" else int(payload["uid"])
    rows = STORE.list(status=status, stage=stage, user_id=uid)
    return ok([c.to_dict(include_contacts=False) for c in rows])

@app.get("/api/cl/cases/{case_id}")
def get_case(case_id: str, authorization: str | None = Header(default=None)):
    payload = require_user(authorization)
    if is_error(payload):
        return payload
    c = STORE.get(case_id)
    if not c:
        return fail(ErrorCode.NOT_FOUND, "not found")
    if payload.get("role") != "admin" and c.user_id != int(payload["uid"]):
        return fail(ErrorCode.FORBIDDEN, "forbidden")
    return ok(c.to_dict())

@app.post("/api/cl/cases/{case_id}/contacts")
def contact(case_id: str, body: ContactReq, authorization: str | None = Header(default=None)):
    payload = require_user(authorization)
    if is_error(payload):
        return payload
    agent = f"user:{payload['uid']}"
    try:
        c = services.add_contact(case_id, body.model_dump(), agent)
    except services.ClError as exc:
        code = ErrorCode.NOT_FOUND if exc.code == "NOT_FOUND" else ErrorCode.VALIDATION
        return fail(code, exc.message)
    return ok(c.to_dict())

@app.post("/api/cl/cases/{case_id}/paid")
def paid(case_id: str, authorization: str | None = Header(default=None)):
    payload = require_admin(authorization)
    if is_error(payload):
        return payload
    try:
        c = services.mark_paid(case_id)
    except services.ClError as exc:
        return fail(ErrorCode.VALIDATION, exc.message)
    return ok(c.to_dict(include_contacts=False))

@app.post("/api/cl/cases/{case_id}/break-promise")
def break_promise(case_id: str, authorization: str | None = Header(default=None)):
    payload = require_admin(authorization)
    if is_error(payload):
        return payload
    try:
        c = services.break_promise(case_id)
    except services.ClError as exc:
        return fail(ErrorCode.VALIDATION, exc.message)
    return ok(c.to_dict(include_contacts=False))

@app.get("/api/cl/admin/metrics")
def metrics(authorization: str | None = Header(default=None)):
    payload = require_admin(authorization)
    if is_error(payload):
        return payload
    return ok(services.metrics())
