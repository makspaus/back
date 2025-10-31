from pydantic import BaseModel, EmailStr
from datetime import datetime

class OwnerAccountBase(BaseModel):
    email: EmailStr
    password_hash: str

class OwnerAccountCreate(OwnerAccountBase):
    pass

class OwnerAccount(OwnerAccountBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True
