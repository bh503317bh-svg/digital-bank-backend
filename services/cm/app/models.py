
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
class CaseNote:
    note_id: str
    author_user_id: int
    body: str
    created_at: str = field(default_factory=now_iso)
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

@dataclass
class Case:
    case_id: str
    case_type: str
    priority: str
    channel: str
    status: str
    customer_id: int
    user_id: int
    subject: str
    description: str
    assignee: str = ""
    disposition: str = ""
    sla_due_at: str = ""
    created_at: str = field(default_factory=now_iso)
    updated_at: str = field(default_factory=now_iso)
    notes: list[CaseNote] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    meta: dict[str, Any] = field(default_factory=dict)

    def to_dict(self, include_notes: bool = True) -> dict[str, Any]:
        d = {
            "case_id": self.case_id,
            "case_type": self.case_type,
            "priority": self.priority,
            "channel": self.channel,
            "status": self.status,
            "customer_id": self.customer_id,
            "user_id": self.user_id,
            "subject": self.subject,
            "description": self.description,
            "assignee": self.assignee,
            "disposition": self.disposition,
            "sla_due_at": self.sla_due_at,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "tags": self.tags,
            "meta": self.meta,
        }
        if include_notes:
            d["notes"] = [n.to_dict() for n in self.notes]
        return d

@dataclass
class KycReview:
    review_id: str
    customer_id: int
    user_id: int
    status: str  # pending / approved / rejected / need_info
    checklist: dict[str, bool]
    reviewer: str = ""
    reason: str = ""
    created_at: str = field(default_factory=now_iso)
    updated_at: str = field(default_factory=now_iso)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
