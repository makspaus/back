from pydantic import BaseModel
from uuid import UUID
class OwnerShopBase(BaseModel):
    owner_id: UUID
    shop_id: UUID

class OwnerShopCreate(OwnerShopBase):
    pass

class OwnerShop(OwnerShopBase):
    owner_id: UUID
    shop_id: UUID

    class Config:
        orm_mode = True
