from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SessionBase(BaseModel):
    user_id: Optional[str] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None

class SessionCreate(SessionBase):
    user_id: str

class Session(SessionBase):
    id: str

    class Config:
        orm_mode = True
