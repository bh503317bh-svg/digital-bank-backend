import httpx
from fastapi import FastAPI, Header
from pydantic_settings import BaseSettings

from bank_common import ErrorCode, decode_token, fail, ok


class Settings(BaseSettings):
    jwt_secret: str = "wecode-bank-demo-secret-change-me"
    cf_url: str = "http://cf:8002"
    dp_url: str = "http://dp:8003"
    ac_url: str = "http://ac:8004"
    ln_url: str = "http://ln:8005"
    cl_url: str = "http://cl:8006"
    cm_url: str = "http://cm:8007"


settings = Settings()
app = FastAPI(title="bank-bff-admin")


def require_admin(authorization: str | None):
    if not authorization or not authorization.lower().startswith("bearer "):
        return fail(ErrorCode.UNAUTHORIZED, "missing token")
    try:
        payload = decode_token(authorization.split(" ", 1)[1], secret=settings.jwt_secret)
    except Exception:
        return fail(ErrorCode.UNAUTHORIZED, "invalid token")
    if payload.get("role") != "admin":
        return fail(ErrorCode.FORBIDDEN, "admin only")
    return payload


def _data(resp) -> dict | list | None:
    try:
        body = resp.json()
    except Exception:
        return None
    if isinstance(body, dict) and body.get("code") == 0:
        return body.get("data")
    return None


@app.get("/health")
def health():
    return ok({"service": "bank-bff-admin", "status": "up"})


@app.get("/api/admin/overview")
async def overview(authorization: str | None = Header(default=None)):
    auth = require_admin(authorization)
    if isinstance(auth, dict) and auth.get("code") and auth.get("code") != 0:
        return auth
    headers = {"Authorization": authorization or ""}
    async with httpx.AsyncClient(timeout=15.0) as client:
        customers = await client.get(f"{settings.cf_url}/api/cf/customers", headers=headers)
        accounts = await client.get(f"{settings.dp_url}/api/dp/accounts?all=true", headers=headers)
        events = await client.get(f"{settings.ac_url}/api/ac/events", headers=headers)
        entries = await client.get(f"{settings.ac_url}/api/ac/entries", headers=headers)
        ln_port = await client.get(f"{settings.ln_url}/api/ln/admin/portfolio", headers=headers)
        cm_met = await client.get(f"{settings.cm_url}/api/cm/admin/metrics", headers=headers)
        cl_met = await client.get(f"{settings.cl_url}/api/cl/admin/metrics", headers=headers)
        ln_loans = await client.get(f"{settings.ln_url}/api/ln/loans", headers=headers)
        cm_cases = await client.get(f"{settings.cm_url}/api/cm/cases", headers=headers)
        cl_cases = await client.get(f"{settings.cl_url}/api/cl/cases", headers=headers)
    cust = _data(customers) or []
    accs = _data(accounts) or []
    evs = _data(events) or []
    ents = _data(entries) or []
    total = sum(int(a.get("balance_cents") or 0) for a in accs if isinstance(a, dict))
    return ok(
        {
            "customer_count": len(cust) if isinstance(cust, list) else 0,
            "account_count": len(accs) if isinstance(accs, list) else 0,
            "event_count": len(evs) if isinstance(evs, list) else 0,
            "entry_count": len(ents) if isinstance(ents, list) else 0,
            "total_balance": f"{total / 100:.2f}",
            "customers": cust[:20] if isinstance(cust, list) else [],
            "accounts": accs[:20] if isinstance(accs, list) else [],
            "recent_entries": ents[:20] if isinstance(ents, list) else [],
            "ln_portfolio": _data(ln_port) or {},
            "cm_metrics": _data(cm_met) or {},
            "cl_metrics": _data(cl_met) or {},
            "ln_loans": (_data(ln_loans) or [])[:20] if isinstance(_data(ln_loans), list) else [],
            "cm_cases": (_data(cm_cases) or [])[:20] if isinstance(_data(cm_cases), list) else [],
            "cl_cases": (_data(cl_cases) or [])[:20] if isinstance(_data(cl_cases), list) else [],
        }
    )


@app.get("/api/admin/customers")
async def customers(authorization: str | None = Header(default=None)):
    auth = require_admin(authorization)
    if isinstance(auth, dict) and auth.get("code") and auth.get("code") != 0:
        return auth
    async with httpx.AsyncClient(timeout=10.0) as client:
        r = await client.get(
            f"{settings.cf_url}/api/cf/customers",
            headers={"Authorization": authorization or ""},
        )
    return r.json()


@app.get("/api/admin/accounts")
async def accounts(authorization: str | None = Header(default=None)):
    auth = require_admin(authorization)
    if isinstance(auth, dict) and auth.get("code") and auth.get("code") != 0:
        return auth
    async with httpx.AsyncClient(timeout=10.0) as client:
        r = await client.get(
            f"{settings.dp_url}/api/dp/accounts?all=true",
            headers={"Authorization": authorization or ""},
        )
    return r.json()


@app.get("/api/admin/entries")
async def entries(authorization: str | None = Header(default=None)):
    auth = require_admin(authorization)
    if isinstance(auth, dict) and auth.get("code") and auth.get("code") != 0:
        return auth
    async with httpx.AsyncClient(timeout=10.0) as client:
        r = await client.get(f"{settings.ac_url}/api/ac/entries")
    return r.json()
