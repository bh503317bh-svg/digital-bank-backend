from __future__ import annotations

QUEUE_MAP = {
    "KYC_SUB_01": "queue_kyc_1",
    "KYC_SUB_02": "queue_kyc_2",
    "KYC_SUB_03": "queue_kyc_3",
    "KYC_SUB_04": "queue_kyc_4",
    "KYC_SUB_05": "queue_kyc_5",
    "CARD_SUB_01": "queue_card_1",
    "CARD_SUB_02": "queue_card_2",
    "CARD_SUB_03": "queue_card_3",
    "CARD_SUB_04": "queue_card_4",
    "CARD_SUB_05": "queue_card_5",
    "DEPOSIT_SUB_01": "queue_deposit_1",
    "DEPOSIT_SUB_02": "queue_deposit_2",
    "DEPOSIT_SUB_03": "queue_deposit_3",
    "DEPOSIT_SUB_04": "queue_deposit_4",
    "DEPOSIT_SUB_05": "queue_deposit_5",
    "WEALTH_SUB_01": "queue_wealth_1",
    "WEALTH_SUB_02": "queue_wealth_2",
    "WEALTH_SUB_03": "queue_wealth_3",
    "WEALTH_SUB_04": "queue_wealth_4",
    "WEALTH_SUB_05": "queue_wealth_5",
    "LOAN_SUB_01": "queue_loan_1",
    "LOAN_SUB_02": "queue_loan_2",
    "LOAN_SUB_03": "queue_loan_3",
    "LOAN_SUB_04": "queue_loan_4",
    "LOAN_SUB_05": "queue_loan_5",
    "COMPLAINT_SUB_01": "queue_complaint_1",
    "COMPLAINT_SUB_02": "queue_complaint_2",
    "COMPLAINT_SUB_03": "queue_complaint_3",
    "COMPLAINT_SUB_04": "queue_complaint_4",
    "COMPLAINT_SUB_05": "queue_complaint_5",
    "FRAUD_SUB_01": "queue_fraud_1",
    "FRAUD_SUB_02": "queue_fraud_2",
    "FRAUD_SUB_03": "queue_fraud_3",
    "FRAUD_SUB_04": "queue_fraud_4",
    "FRAUD_SUB_05": "queue_fraud_5",
    "DATA_SUB_01": "queue_data_1",
    "DATA_SUB_02": "queue_data_2",
    "DATA_SUB_03": "queue_data_3",
    "DATA_SUB_04": "queue_data_4",
    "DATA_SUB_05": "queue_data_5",
    "CHANNEL_SUB_01": "queue_channel_1",
    "CHANNEL_SUB_02": "queue_channel_2",
    "CHANNEL_SUB_03": "queue_channel_3",
    "CHANNEL_SUB_04": "queue_channel_4",
    "CHANNEL_SUB_05": "queue_channel_5",
    "OPS_SUB_01": "queue_ops_1",
    "OPS_SUB_02": "queue_ops_2",
    "OPS_SUB_03": "queue_ops_3",
    "OPS_SUB_04": "queue_ops_4",
    "OPS_SUB_05": "queue_ops_5",
}

AGENT_SKILLS = {
    "agent_01": ["CARD", "OPS"],
    "agent_02": ["LOAN", "OPS"],
    "agent_03": ["COMPLAINT", "OPS"],
    "agent_04": ["FRAUD", "OPS"],
    "agent_05": ["KYC", "OPS"],
    "agent_06": ["CARD", "OPS"],
    "agent_07": ["LOAN", "OPS"],
    "agent_08": ["COMPLAINT", "OPS"],
    "agent_09": ["FRAUD", "OPS"],
    "agent_10": ["KYC", "OPS"],
    "agent_11": ["CARD", "OPS"],
    "agent_12": ["LOAN", "OPS"],
    "agent_13": ["COMPLAINT", "OPS"],
    "agent_14": ["FRAUD", "OPS"],
    "agent_15": ["KYC", "OPS"],
    "agent_16": ["CARD", "OPS"],
    "agent_17": ["LOAN", "OPS"],
    "agent_18": ["COMPLAINT", "OPS"],
    "agent_19": ["FRAUD", "OPS"],
    "agent_20": ["KYC", "OPS"],
    "agent_21": ["CARD", "OPS"],
    "agent_22": ["LOAN", "OPS"],
    "agent_23": ["COMPLAINT", "OPS"],
    "agent_24": ["FRAUD", "OPS"],
    "agent_25": ["KYC", "OPS"],
    "agent_26": ["CARD", "OPS"],
    "agent_27": ["LOAN", "OPS"],
    "agent_28": ["COMPLAINT", "OPS"],
    "agent_29": ["FRAUD", "OPS"],
    "agent_30": ["KYC", "OPS"],
}


def route_queue(case_type: str) -> str:
    return QUEUE_MAP.get(case_type, "queue_general")

def suggest_assignee(case_type: str, priority: str) -> str:
    domain = case_type.split("_")[0]
    candidates = [a for a, skills in AGENT_SKILLS.items() if domain in skills or "OPS" in skills]
    if not candidates:
        return "agent_01"
    # sticky by priority
    idx = hash(case_type + priority) % len(candidates)
    return candidates[idx]
