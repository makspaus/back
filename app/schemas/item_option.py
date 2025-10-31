# app/schemas/item_option.py
from pydantic import BaseModel, condecimal
from typing import Optional
from uuid import UUID

class ItemOption(BaseModel):
    group_id: Optional[UUID]
    name: str
    price_delta: Optional[condecimal(ge=0)] = 0
    is_default: Optional[bool] = False
    sort_order: Optional[int] = 0
    is_available: Optional[bool] = True

class ItemOptionCreate(ItemOption):
    pass

class ItemOptionUpdate(ItemOption):
    pass

class ItemOptionRead(ItemOption):
    id: UUID

    class Config:
        orm_mode = True
