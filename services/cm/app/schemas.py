
from pydantic import BaseModel, Field

class CreateCaseReq(BaseModel):
    case_type: str
    priority: str = "P3"
    channel: str = "app"
    subject: str
    description: str = ""
    customer_id: int = 1
    auto_assign: bool = True
    tags: list[str] = []

class NoteReq(BaseModel):
    body: str

class TransitionReq(BaseModel):
    status: str
    disposition: str = ""

class AssignReq(BaseModel):
    assignee: str

class KycUpdateReq(BaseModel):
    status: str = ""
    checklist: dict[str, bool] | None = None
    reason: str = ""
