
from __future__ import annotations

def stage_for_dpd(dpd: int) -> str:
    if dpd <= 30:
        return "early"
    if dpd <= 90:
        return "mid"
    if dpd <= 180:
        return "late"
    return "legal"

def recovery_score(dpd: int, overdue_principal_cents: int, contact_success: int, broken_promises: int) -> int:
    score = 700
    score -= min(300, dpd * 2)
    score -= min(200, overdue_principal_cents // 100000)
    score += contact_success * 15
    score -= broken_promises * 40
    return max(100, min(900, score))

def recommend_intensity(score: int) -> int:
    if score >= 700:
        return 1
    if score >= 550:
        return 2
    if score >= 400:
        return 3
    if score >= 250:
        return 4
    return 5
