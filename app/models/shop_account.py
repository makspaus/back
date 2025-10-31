import sqlalchemy as sa
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base

class ShopAccount(Base):
    __tablename__ = 'shop_accounts'


    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    shop_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey("shops.id", ondelete="CASCADE"), nullable=False)
    username = sa.Column(sa.String, nullable=False)
    password_hash = sa.Column(sa.String, nullable=False)
    last_login_at = sa.Column(sa.DateTime(timezone=True))
    owned_shops = relationship("OwnerShop", back_populates="owner", cascade="all, delete-orphan")
    device_tokens = relationship("ShopDeviceToken", back_populates="shop_account", cascade="all, delete-orphan")
