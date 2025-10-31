import sqlalchemy as sa
from sqlalchemy import Column, Float, String, ForeignKey, Integer, DateTime, Boolean, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base


class ItemOption(Base):
    __tablename__ = "item_options"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    group_id = Column(UUID(as_uuid=True), ForeignKey("item_option_groups.id", ondelete="CASCADE"))
    name = Column(String)
    price_delta = Column(Float)
    is_default = Column(Boolean, default=False)
    sort_order = Column(Integer)
    is_available = Column(Boolean, default=True)

    group = relationship("ItemOptionGroup", back_populates="options")
