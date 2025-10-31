# app/schemas/menu_item.py
from pydantic import BaseModel, condecimal
from typing import Optional
from uuid import UUID

class MenuItemBase(BaseModel):
    shop_id: Optional[UUID]
    name: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    base_price: Optional[condecimal(gt=0)] = None
    is_active: Optional[bool] = True
    sort_order: Optional[int] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(MenuItemBase):
    pass

class MenuItemRead(MenuItemBase):
    id: UUID

    class Config:
        orm_mode = True
