from pydantic import BaseModel, constr
from datetime import datetime
from typing import Optional

class DeviceTokenBase(BaseModel):
    user_id: Optional[str] = None
    platform: constr(max_length=50)
    token: str
    last_used_at: Optional[datetime] = None

class DeviceTokenCreate(DeviceTokenBase):
    user_id: str

class DeviceToken(DeviceTokenBase):
    id: str

    class Config:
        orm_mode = True
