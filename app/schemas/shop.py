# app/schemas/shop.py
from pydantic import BaseModel, Field, constr
from typing import Optional, Any, Dict
from uuid import UUID
from datetime import datetime

class Shop(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    tz: Optional[str] = None
    open_hours: Optional[Any] = None  # JSON structure
    is_active: Optional[bool] = True

class ShopCreate(Shop):
    name: str

class ShopUpdate(Shop):
    pass

class ShopRead(Shop):
    id: UUID
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
