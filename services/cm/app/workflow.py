
from __future__ import annotations
TRANSITIONS = {
    "open": {"assigned", "closed"},
    "assigned": {"in_progress", "open"},
    "in_progress": {"pending_customer", "resolved", "assigned"},
    "pending_customer": {"in_progress", "resolved"},
    "resolved": {"closed", "reopened"},
    "closed": {"reopened"},
    "reopened": {"assigned", "in_progress"},
}

class BadTransition(Exception):
    pass

def move(status: str, target: str) -> str:
    if target not in TRANSITIONS.get(status, set()):
        raise BadTransition(f"{status}->{target}")
    return target
