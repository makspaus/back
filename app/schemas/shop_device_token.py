from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ShopDeviceTokenBase(BaseModel):
    shop_account_id: str
    platform: str
    token: str
    last_used_at: Optional[datetime] = None

class ShopDeviceTokenCreate(ShopDeviceTokenBase):
    pass

class ShopDeviceToken(ShopDeviceTokenBase):
    id: str

    class Config:
        orm_mode = True
