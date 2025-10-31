from pydantic import BaseModel
from datetime import datetime

class UserFavoriteBase(BaseModel):
    user_id: str
    shop_id: str

class UserFavoriteCreate(UserFavoriteBase):
    pass

class UserFavorite(UserFavoriteBase):
    id: str
    added_at: datetime

    class Config:
        orm_mode = True
