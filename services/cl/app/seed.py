
from __future__ import annotations
from app.services import open_case
from app.store import STORE

def seed_demo() -> None:
    if STORE.list():
        return
    samples = [
        {"loan_id": "seed_ln_1", "user_id": 1, "dpd": 12, "overdue_principal": "3200", "overdue_interest": "120"},
        {"loan_id": "seed_ln_2", "user_id": 1, "dpd": 45, "overdue_principal": "15000", "overdue_interest": "900"},
        {"loan_id": "seed_ln_3", "user_id": 1, "dpd": 120, "overdue_principal": "48000", "overdue_interest": "5200"},
    ]
    for s in samples:
        open_case(s)
