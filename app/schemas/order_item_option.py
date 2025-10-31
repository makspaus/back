from pydantic import BaseModel, condecimal

class OrderItemOptionBase(BaseModel):
    order_item_id: str
    option_id: str | None = None
    name_snapshot: str
    price_delta: condecimal(ge=0)

class OrderItemOptionCreate(OrderItemOptionBase):
    pass

class OrderItemOption(OrderItemOptionBase):
    id: str

    class Config:
        orm_mode = True
