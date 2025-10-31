from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Boolean, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base
class ShopDeviceToken(Base):
    __tablename__ = "shop_device_tokens"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    shop_account_id = Column(UUID(as_uuid=True), ForeignKey("shop_accounts.id", ondelete="CASCADE"), nullable=False)
    token = Column(String, unique=True, nullable=False)
    platform = Column(String, nullable=True)  # Например, "iOS", "Android"
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    shop_account = relationship("ShopAccount", back_populates="device_tokens")