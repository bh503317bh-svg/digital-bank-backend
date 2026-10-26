from __future__ import annotations

import threading
from dataclasses import asdict, dataclass, field
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from typing import Any
from uuid import uuid4

# 1 point = 0.01 yuan (1 cent)
POINTS_PER_YUAN = 100


@dataclass
class ShopProduct:
    product_id: str
    name: str
    category: str
    price_yuan: str
    cover: str
    desc: str
    stock: int = 99

    @property
    def price_cents(self) -> int:
        return int(Decimal(self.price_yuan).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) * 100)

    @property
    def price_points(self) -> int:
        return self.price_cents  # 1 cent = 1 point

    def to_dict(self) -> dict[str, Any]:
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price_yuan": self.price_yuan,
            "price_points": self.price_points,
            "cover": self.cover,
            "desc": self.desc,
            "stock": self.stock,
        }


CATALOG: list[ShopProduct] = [
    ShopProduct("amz5", "Amazon Gift Card $5", "gift_card", "5.00", "🛒", "Digital code emailed instantly"),
    ShopProduct("amz10", "Amazon Gift Card $10", "gift_card", "10.00", "🛒", "Digital code emailed instantly"),
    ShopProduct("amz25", "Amazon Gift Card $25", "gift_card", "25.00", "🛒", "Digital code emailed instantly"),
    ShopProduct("sbx10", "Starbucks Card $10", "gift_card", "10.00", "☕", "Reloadable e-gift"),
    ShopProduct("sbx25", "Starbucks Card $25", "gift_card", "25.00", "☕", "Reloadable e-gift"),
    ShopProduct("nflx1", "Netflix 1-Month Credit", "subscription", "15.49", "🎬", "Statement credit toward Netflix"),
    ShopProduct("spot1", "Spotify Premium 1-Month", "subscription", "11.99", "🎵", "Premium subscription credit"),
    ShopProduct("fee1", "Fee-free Wire Coupon", "banking", "3.00", "🏦", "Waive one domestic wire fee"),
    ShopProduct("cash5", "Statement Credit $5", "banking", "5.00", "💵", "Posted to deposit account"),
    ShopProduct("uber15", "Uber Cash $15", "gift_card", "15.00", "🚗", "Rides & Uber Eats"),
]


@dataclass
class ShopOrder:
    order_id: str
    user_id: int
    product_id: str
    product_name: str
    qty: int
    pay_cash_cents: int
    pay_points: int
    account_no: str
    status: str = "paid"
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["pay_cash"] = f"{self.pay_cash_cents / 100:.2f}"
        return d


_lock = threading.RLock()
_orders: list[ShopOrder] = []


def list_catalog(category: str | None = None) -> list[dict]:
    rows = CATALOG
    if category:
        rows = [p for p in rows if p.category == category]
    return [p.to_dict() for p in rows]


def get_product(product_id: str) -> ShopProduct | None:
    for p in CATALOG:
        if p.product_id == product_id:
            return p
    return None


def list_orders(user_id: int) -> list[dict]:
    with _lock:
        rows = [o for o in _orders if o.user_id == user_id]
    rows.sort(key=lambda x: x.created_at, reverse=True)
    return [o.to_dict() for o in rows]


def record_order(order: ShopOrder) -> None:
    with _lock:
        _orders.insert(0, order)
        if len(_orders) > 2000:
            del _orders[1500:]


def new_order_id() -> str:
    return "ord_" + uuid4().hex[:16]


def yuan_to_cents(amount: str | float | int) -> int:
    d = Decimal(str(amount)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return int(d * 100)
