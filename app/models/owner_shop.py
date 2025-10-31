from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Boolean, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base
from sqlalchemy import UniqueConstraint

class OwnerShop(Base):
    __tablename__ = "owner_shops"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("shop_accounts.id", ondelete="CASCADE"), nullable=False)
    shop_id = Column(UUID(as_uuid=True), ForeignKey("shops.id", ondelete="CASCADE"), nullable=False)

    __table_args__ = (UniqueConstraint("owner_id", "shop_id", name="uq_owner_shop"),)

    owner = relationship("ShopAccount", back_populates="owned_shops")
    shop = relationship("Shop", back_populates="owners")