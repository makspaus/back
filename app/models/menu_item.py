import sqlalchemy as sa
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Boolean, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base

class MenuItem(Base):
    __tablename__ = 'menu_items'


    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    shop_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey("shops.id", ondelete="CASCADE"), nullable=False)
    item_name = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.Text)
    image_url = sa.Column(sa.Text)
    base_price = sa.Column(sa.Numeric)
    is_active = sa.Column(sa.Boolean, default=True)
    sort_order = sa.Column(sa.Integer, default=0)
    shop = relationship("Shop", back_populates="menu_items")
    option_groups = relationship("ItemOptionGroup", back_populates="menu_item")