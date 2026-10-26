
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Any
from uuid import uuid4

def now_iso() -> str:
    return datetime.utcnow().isoformat() + "Z"

def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex[:16]}"

@dataclass
class ContactLog:
    contact_id: str
    case_id: str
    channel: str
    result: str
    promise_amount_cents: int = 0
    promise_date: str = ""
    note: str = ""
    agent: str = ""
    created_at: str = field(default_factory=now_iso)
    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["promise_amount"] = f"{self.promise_amount_cents / 100:.2f}"
        return d

@dataclass
class CollectionCase:
    case_id: str
    loan_id: str
    user_id: int
    customer_id: int
    overdue_principal_cents: int
    overdue_interest_cents: int
    dpd: int
    stage: str  # early / mid / late / legal / closed
    status: str  # open / promised / broken / paid / written_off
    assignee: str = ""
    strategy_code: str = ""
    created_at: str = field(default_factory=now_iso)
    updated_at: str = field(default_factory=now_iso)
    contacts: list[ContactLog] = field(default_factory=list)
    meta: dict[str, Any] = field(default_factory=dict)

    def to_dict(self, include_contacts: bool = True) -> dict[str, Any]:
        d = {
            "case_id": self.case_id,
            "loan_id": self.loan_id,
            "user_id": self.user_id,
            "customer_id": self.customer_id,
            "overdue_principal": f"{self.overdue_principal_cents / 100:.2f}",
            "overdue_interest": f"{self.overdue_interest_cents / 100:.2f}",
            "dpd": self.dpd,
            "stage": self.stage,
            "status": self.status,
            "assignee": self.assignee,
            "strategy_code": self.strategy_code,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "meta": self.meta,
        }
        if include_contacts:
            d["contacts"] = [c.to_dict() for c in self.contacts]
        return d
