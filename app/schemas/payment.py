# app/schemas/payment.py
from pydantic import BaseModel, condecimal
from typing import Optional, Dict
from uuid import UUID
from datetime import datetime

class PaymentCreate(BaseModel):
    order_id: UUID
    method: str
    status: Optional[str] = None
    amount: condecimal(gt=0)
    provider_id: Optional[str] = None
    extra: Optional[dict] = None

class PaymentRead(BaseModel):
    order_id: UUID
    method: str
    status: Optional[str]
    amount: condecimal(gt=0)
    created_at: datetime
    paid_at: Optional[datetime] = None

    class Config:
        orm_mode = True
