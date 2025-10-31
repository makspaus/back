import sqlalchemy as sa
from sqlalchemy import Column,Float,JSON,  String, ForeignKey, Integer, DateTime, Boolean, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id", ondelete="CASCADE"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("app_users.id", ondelete="CASCADE"))
    method = Column(String)
    status = Column(String)
    amount = Column(Float)
    provider_id = Column(String)
    extra = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    paid_at = Column(DateTime(timezone=True))

    order = relationship("Order", back_populates="payments")
    user = relationship("User", back_populates="payments")

