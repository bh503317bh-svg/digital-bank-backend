
from __future__ import annotations
from datetime import datetime, timedelta
from app.taxonomy import SLA_HOURS

def compute_sla_due(priority: str, start: datetime | None = None) -> str:
    start = start or datetime.utcnow()
    hours = SLA_HOURS.get(priority, 72)
    return (start + timedelta(hours=hours)).isoformat() + "Z"

def sla_breached(sla_due_at: str) -> bool:
    if not sla_due_at:
        return False
    try:
        due = datetime.fromisoformat(sla_due_at.replace("Z", ""))
    except ValueError:
        return False
    return datetime.utcnow() > due
