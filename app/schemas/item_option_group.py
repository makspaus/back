# app/schemas/item_option_group.py
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ItemOptionGroup(BaseModel):
    menu_item_id: Optional[UUID]
    name: str
    min_select: Optional[int] = 0
    max_select: Optional[int] = 1
    is_required: Optional[bool] = False
    sort_order: Optional[int] = 0

class ItemOptionGroupCreate(ItemOptionGroup):
    pass

class ItemOptionGroupUpdate(ItemOptionGroup):
    pass

class ItemOptionGroupRead(ItemOptionGroup):
    id: UUID

    class Config:
        orm_mode = True

