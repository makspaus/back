from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TimeSlotBase(BaseModel):
    shop_id: str
    start: datetime
    end: datetime
    capacity: int
    is_active: Optional[bool] = True

class TimeSlotCreate(TimeSlotBase):
    pass

class TimeSlot(TimeSlotBase):
    id: str

    class Config:
        orm_mode = True
