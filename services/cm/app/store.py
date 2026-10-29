
from __future__ import annotations
import threading
from typing import Optional
from app.models import Case, KycReview

class CmStore:
    def __init__(self) -> None:
        self._lock = threading.RLock()
        self.cases: dict[str, Case] = {}
        self.kyc: dict[str, KycReview] = {}

    def save_case(self, c: Case) -> None:
        with self._lock:
            self.cases[c.case_id] = c

    def get_case(self, case_id: str) -> Optional[Case]:
        with self._lock:
            return self.cases.get(case_id)

    def list_cases(self, status=None, priority=None, user_id=None, customer_id=None, case_type=None):
        with self._lock:
            rows = list(self.cases.values())
        if status:
            rows = [r for r in rows if r.status == status]
        if priority:
            rows = [r for r in rows if r.priority == priority]
        if user_id is not None:
            rows = [r for r in rows if r.user_id == user_id]
        if customer_id is not None:
            rows = [r for r in rows if r.customer_id == customer_id]
        if case_type:
            rows = [r for r in rows if r.case_type == case_type]
        rows.sort(key=lambda x: x.created_at, reverse=True)
        return rows

    def save_kyc(self, k: KycReview) -> None:
        with self._lock:
            self.kyc[k.review_id] = k

    def list_kyc(self, status=None):
        with self._lock:
            rows = list(self.kyc.values())
        if status:
            rows = [r for r in rows if r.status == status]
        rows.sort(key=lambda x: x.created_at, reverse=True)
        return rows

STORE = CmStore()
