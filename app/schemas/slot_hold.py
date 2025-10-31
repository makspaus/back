from pydantic import BaseModel
from datetime import datetime

class SlotHoldBase(BaseModel):
    slot_id: str
    order_id: str
    expires_at: datetime

class SlotHoldCreate(SlotHoldBase):
    pass

class SlotHold(SlotHoldBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True
