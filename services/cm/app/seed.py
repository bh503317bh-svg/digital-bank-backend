
from __future__ import annotations
from app.services import create_case, create_kyc
from app.store import STORE
from app.taxonomy import CASE_TYPES

def seed_demo() -> None:
    if STORE.list_cases():
        return
    samples = [
        ("KYC_SUB_01", "P2", "Item"),
        ("COMPLAINT_SUB_03", "P1", "："),
        ("LOAN_SUB_02", "P2", "Item"),
        ("FRAUD_SUB_01", "P1", "Item"),
        ("WEALTH_SUB_05", "P3", "Item"),
    ]
    for ct, pri, subj in samples:
        create_case(1, {
            "case_type": ct if ct in CASE_TYPES else CASE_TYPES[0],
            "priority": pri,
            "subject": subj,
            "description": f"seed {subj}",
            "auto_assign": True,
            "channel": "app",
        })
    create_kyc(1, 1)
