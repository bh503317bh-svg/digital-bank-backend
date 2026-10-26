
from pydantic import BaseModel

class OpenCaseReq(BaseModel):
    loan_id: str = ""
    user_id: int = 1
    customer_id: int = 1
    dpd: int = 1
    overdue_principal: str = "0"
    overdue_interest: str = "0"
    assignee: str = "collector_01"

class ContactReq(BaseModel):
    channel: str = "human_call"
    result: str = "no_answer_01"
    promise_amount: str = ""
    promise_date: str = ""
    note: str = ""
