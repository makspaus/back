import sqlalchemy as sa
from sqlalchemy import Column, Float, String, ForeignKey, Integer, DateTime, Boolean, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base

class OrderItemOption(Base):
    __tablename__ = "order_item_options"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_item_id = Column(UUID(as_uuid=True), ForeignKey("order_items.id", ondelete="CASCADE"))
    option_id = Column(UUID(as_uuid=True), ForeignKey("item_options.id", ondelete="SET NULL"))
    name_snapshot = Column(String)
    price_delta = Column(Float)

    order_item = relationship("OrderItem", back_populates="options")
    option = relationship("ItemOption")
