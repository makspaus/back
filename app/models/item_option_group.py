import sqlalchemy as sa
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Boolean, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base


class ItemOptionGroup(Base):
    __tablename__ = "item_option_groups"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    menu_item_id = Column(UUID(as_uuid=True), ForeignKey("menu_items.id", ondelete="CASCADE"))
    name = Column(String)
    min_select = Column(Integer)
    max_select = Column(Integer)
    is_required = Column(Boolean, default=False)
    sort_order = Column(Integer)

    menu_item = relationship("MenuItem", back_populates="option_groups")
    options = relationship("ItemOption", back_populates="group", cascade="all, delete-orphan")
