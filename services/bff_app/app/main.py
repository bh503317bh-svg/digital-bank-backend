import asyncio

from fastapi import FastAPI, Header, Request
from pydantic import BaseModel, Field
import httpx
from pydantic_settings import BaseSettings

from bank_common import ErrorCode, decode_token, fail, ok, verify_pay_password_async

from app import shop


class Settings(BaseSettings):
    us_url: str = "http://us:8001"
    cf_url: str = "http://cf:8002"
    dp_url: str = "http://dp:8003"
    jwt_secret: str = "wecode-bank-demo-secret-change-me"


settings = Settings()
app = FastAPI(title="bank-bff-app")


class TransferBody(BaseModel):
    from_account_no: str
    to_account_no: str
    amount: str
    pay_password: str = Field(min_length=4, max_length=12)
    beneficiary_name: str = ""
    swift_code: str = ""
    bank_name: str = ""
    bank_country: str = "US"
    bank_address: str = ""
    remittance_info: str = ""
    transfer_type: str = "internal"


class WealthBuyBody(BaseModel):
    account_no: str
    amount: str
    product_id: str
    product_name: str = ""
    pay_password: str = Field(min_length=4, max_length=12)


class ShopBuyBody(BaseModel):
    account_no: str = ""
    product_id: str
    qty: int = Field(default=1, ge=1, le=10)
    pay_cash: str = "0"  # yuan from deposit
    pay_points: int = Field(default=0, ge=0)
    pay_password: str = Field(min_length=4, max_length=12)


def _uid(authorization: str | None) -> tuple[dict | None, int | None]:
    if not authorization or not authorization.lower().startswith("bearer "):
        return fail(ErrorCode.UNAUTHORIZED, "missing token"), None
    try:
        payload = decode_token(authorization.split(" ", 1)[1], secret=settings.jwt_secret)
    except Exception:
        return fail(ErrorCode.UNAUTHORIZED, "invalid token"), None
    return None, int(payload["uid"])


@app.get("/health")
def health():
    return ok({"service": "bank-bff-app", "status": "up"})


@app.get("/api/app/home")
async def home(authorization: str | None = Header(default=None)):
    if not authorization:
        return fail(ErrorCode.UNAUTHORIZED, "missing token")
    headers = {"Authorization": authorization}
    timeout = httpx.Timeout(5.0, connect=2.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        me_t = client.get(f"{settings.us_url}/api/auth/me", headers=headers)
        cust_t = client.get(f"{settings.cf_url}/api/cf/customers/me", headers=headers)
        acc_t = client.get(f"{settings.dp_url}/api/dp/accounts", headers=headers)
        me, customer, accounts = await asyncio.gather(me_t, cust_t, acc_t, return_exceptions=True)
    if isinstance(me, Exception):
        return fail(ErrorCode.UPSTREAM_TIMEOUT, f"us timeout: {me}")
    me_j = me.json()
    if me_j.get("code") != 0:
        return me_j
    cust = None
    if not isinstance(customer, Exception):
        try:
            cust = customer.json().get("data")
        except Exception:  # noqa: BLE001
            cust = None
    accs: list = []
    if not isinstance(accounts, Exception):
        try:
            accs = accounts.json().get("data") or []
        except Exception:  # noqa: BLE001
            accs = []
    total = sum(int(a.get("balance_cents") or 0) for a in accs)
    return ok(
        {
            "user": me_j.get("data"),
            "customer": cust,
            "accounts": accs,
            "total_balance": f"{total / 100:.2f}",
            "brand": "aku-bank",
        }
    )


@app.post("/api/app/transfer")
async def transfer(body: TransferBody, request: Request, authorization: str | None = Header(default=None)):
    if not authorization:
        return fail(ErrorCode.UNAUTHORIZED, "missing token")
    headers = {"Authorization": authorization}
    idem = request.headers.get("idempotency-key")
    if idem:
        headers["Idempotency-Key"] = idem
    async with httpx.AsyncClient(timeout=15.0) as client:
        r = await client.post(
            f"{settings.dp_url}/api/dp/txns/transfer",
            json=body.model_dump(),
            headers=headers,
        )
    return r.json()


@app.post("/api/app/wealth/buy")
async def wealth_buy(body: WealthBuyBody, request: Request, authorization: str | None = Header(default=None)):
    if not authorization:
        return fail(ErrorCode.UNAUTHORIZED, "missing token")
    headers = {"Authorization": authorization}
    idem = request.headers.get("idempotency-key")
    if idem:
        headers["Idempotency-Key"] = idem
    async with httpx.AsyncClient(timeout=15.0) as client:
        r = await client.post(
            f"{settings.dp_url}/api/dp/txns/wealth-buy",
            json=body.model_dump(),
            headers=headers,
        )
    return r.json()


@app.get("/api/app/shop/catalog")
async def shop_catalog(category: str | None = None, authorization: str | None = Header(default=None)):
    err, _ = _uid(authorization)
    if err:
        return err
    return ok({"items": shop.list_catalog(category), "points_per_yuan": shop.POINTS_PER_YUAN})


@app.get("/api/app/shop/orders")
async def shop_orders(authorization: str | None = Header(default=None)):
    err, uid = _uid(authorization)
    if err:
        return err
    return ok(shop.list_orders(uid or 0))


@app.post("/api/app/shop/buy")
async def shop_buy(body: ShopBuyBody, request: Request, authorization: str | None = Header(default=None)):
    err, uid = _uid(authorization)
    if err:
        return err
    pay_check = await verify_pay_password_async(
        authorization, body.pay_password, us_url=settings.us_url
    )
    if pay_check.get("code") != 0:
        return pay_check
    product = shop.get_product(body.product_id)
    if not product:
        return fail(ErrorCode.NOT_FOUND, "product not found")
    qty = body.qty
    total_cents = product.price_cents * qty
    cash_cents = shop.yuan_to_cents(body.pay_cash)
    points = int(body.pay_points)
    if cash_cents < 0 or points < 0:
        return fail(ErrorCode.VALIDATION, "invalid payment")
    covered = cash_cents + points  # 1 point = 1 cent
    if covered != total_cents:
        return fail(
            ErrorCode.VALIDATION,
            f"payment mismatch: need {total_cents} cents equiv, got cash={cash_cents} points={points}",
        )
    if cash_cents > 0 and not body.account_no:
        return fail(ErrorCode.VALIDATION, "account_no required for cash payment")

    withdraw_data = None
    if cash_cents > 0:
        headers = {"Authorization": authorization or ""}
        idem = request.headers.get("idempotency-key") or shop.new_order_id()
        headers["Idempotency-Key"] = idem
        async with httpx.AsyncClient(timeout=15.0) as client:
            r = await client.post(
                f"{settings.dp_url}/api/dp/txns/withdraw",
                json={
                    "account_no": body.account_no,
                    "amount": f"{cash_cents / 100:.2f}",
                    "pay_password": body.pay_password,
                },
                headers=headers,
            )
        withdraw_data = r.json()
        if withdraw_data.get("code") != 0:
            return withdraw_data

    order = shop.ShopOrder(
        order_id=shop.new_order_id(),
        user_id=uid or 0,
        product_id=product.product_id,
        product_name=product.name,
        qty=qty,
        pay_cash_cents=cash_cents,
        pay_points=points,
        account_no=body.account_no or "",
    )
    shop.record_order(order)
    return ok(
        {
            "order": order.to_dict(),
            "withdraw": withdraw_data.get("data") if withdraw_data else None,
            "points_spent": points,
        }
    )
