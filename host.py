"""User API and admin API in one process. Ledger calls go to core."""

from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path

import httpx
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from assistant import router as assistant_router

from bank_common import ErrorCode, decode_token, fail

ROOT = Path(__file__).resolve().parent
CORE = os.environ.get("CORE_URL", "http://core:8001")
SKIP = {"/openapi.json", "/docs", "/docs/oauth2-redirect", "/redoc", "/health"}
CORE_PREFIXES = ("/api/auth", "/api/cf", "/api/dp", "/api/ac", "/api/ln")
PUBLIC_PREFIXES = ("/api/auth/login", "/api/auth/register")


def load_service(name: str):
    for key in list(sys.modules):
        if key == "app" or key.startswith("app."):
            del sys.modules[key]
    service_dir = str(ROOT / "services" / name)
    sys.path.insert(0, service_dir)
    try:
        module = importlib.import_module("app.main")
        application = module.app
    finally:
        sys.path.remove(service_dir)
    prefix = f"_svc_{name}"
    for key in list(sys.modules):
        if key == "app" or key.startswith("app."):
            sys.modules[f"{prefix}.{key}"] = sys.modules.pop(key)
    return application


def build():
    os.environ.setdefault("JWT_SECRET", "wecode-bank-demo-secret-change-me")
    os.environ["US_URL"] = CORE
    os.environ["CF_URL"] = CORE
    os.environ["DP_URL"] = CORE
    os.environ["AC_URL"] = CORE
    os.environ["LN_URL"] = CORE
    local = os.environ.get("SELF_URL", "http://127.0.0.1:8080")
    os.environ["CL_URL"] = local
    os.environ["CM_URL"] = local

    services = [
        load_service("cl"),
        load_service("cm"),
        load_service("bff_app"),
        load_service("bff_admin"),
    ]
    app = FastAPI(title="digital-bank-backend")
    app.include_router(assistant_router)

    @app.get("/health")
    def health():
        return {"code": 0, "message": "ok", "data": {"service": "digital-bank-backend", "status": "up"}}

    for sub in services:
        for route in list(sub.router.routes):
            path = getattr(route, "path", "") or ""
            if path in SKIP:
                continue
            app.router.routes.append(route)

    @app.middleware("http")
    async def proxy_core(request: Request, call_next):
        path = request.url.path
        if not any(path.startswith(prefix) for prefix in CORE_PREFIXES):
            return await call_next(request)
        public = any(path.startswith(prefix) for prefix in PUBLIC_PREFIXES)
        if not public:
            auth = request.headers.get("authorization") or ""
            if not auth.lower().startswith("bearer "):
                return JSONResponse(fail(ErrorCode.UNAUTHORIZED, "missing token"))
            try:
                decode_token(auth.split(" ", 1)[1], secret=os.environ.get("JWT_SECRET", ""))
            except Exception:
                return JSONResponse(fail(ErrorCode.UNAUTHORIZED, "invalid token"))
        url = CORE.rstrip("/") + path
        if request.url.query:
            url = f"{url}?{request.url.query}"
        headers = {k: v for k, v in request.headers.items() if k.lower() not in {"host", "content-length"}}
        body = await request.body()
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                resp = await client.request(request.method, url, content=body, headers=headers)
        except httpx.TimeoutException:
            return JSONResponse(fail(ErrorCode.UPSTREAM_TIMEOUT, "upstream timeout"))
        except httpx.HTTPError as exc:
            return JSONResponse(fail(ErrorCode.INTERNAL, f"upstream error: {exc}"))
        return Response(content=resp.content, status_code=resp.status_code, media_type=resp.headers.get("content-type"))

    return app


app = build()
