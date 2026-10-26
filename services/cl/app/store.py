
from __future__ import annotations
import threading
from typing import Optional
from app.models import CollectionCase

class ClStore:
    def __init__(self) -> None:
        self._lock = threading.RLock()
        self.cases: dict[str, CollectionCase] = {}

    def save(self, c: CollectionCase) -> None:
        with self._lock:
            self.cases[c.case_id] = c

    def get(self, case_id: str) -> Optional[CollectionCase]:
        with self._lock:
            return self.cases.get(case_id)

    def list(self, status=None, stage=None, user_id=None):
        with self._lock:
            rows = list(self.cases.values())
        if status:
            rows = [r for r in rows if r.status == status]
        if stage:
            rows = [r for r in rows if r.stage == stage]
        if user_id is not None:
            rows = [r for r in rows if r.user_id == user_id]
        rows.sort(key=lambda x: (-x.dpd, x.created_at), reverse=False)
        rows.sort(key=lambda x: x.dpd, reverse=True)
        return rows

STORE = ClStore()
