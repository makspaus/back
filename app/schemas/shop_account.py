from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ShopAccountBase(BaseModel):
    shop_id: str
    username: str
    password_hash: str
    last_login_at: Optional[datetime] = None

class ShopAccountCreate(ShopAccountBase):
    pass

class ShopAccount(ShopAccountBase):
    id: str

    class Config:
        orm_mode = True
