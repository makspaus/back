# app/schemas/order_item.py
from pydantic import BaseModel, condecimal
from typing import List, Optional
from uuid import UUID
from app.schemas.order_item_option import OrderItemOptionCreate, OrderItemOption

class OrderItemCreate(BaseModel):
    menu_item_id: UUID
    menu_item_id: str | None = None
    name_snapshot: str
    unit_price: condecimal(gt=0)
    qty: int
    line_total: condecimal(gt=0)

class OrderItemCreate(OrderItemCreate):
    options: List[OrderItemOptionCreate] = []
class OrderItemRead(BaseModel):
    id: UUID
    menu_item_id: UUID
    name_snapshot: str
    unit_price: float
    qty: int
    line_total: float
    options: List[OrderItemOption] = []

    class Config:
        orm_mode = True
