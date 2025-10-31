import sqlalchemy as sa
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base

class Shop(Base):
    __tablename__ = 'shops'


    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    shop_name = sa.Column(sa.String, nullable=False)
    address = sa.Column(sa.String, nullable=True)
    lat = sa.Column(sa.Float)
    lng = sa.Column(sa.Float)
    tz = sa.Column(sa.String, nullable=True)
    open_hours = sa.Column(sa.JSON, nullable=True)
    is_active = sa.Column(sa.Boolean, default=True)
    created_at = sa.Column(sa.DateTime(timezone=True))
    owners = relationship("OwnerShop", back_populates="shop", cascade="all, delete-orphan")
    favorited_by = relationship("UserFavorite", back_populates="shop", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="shop", cascade="all, delete-orphan")
    time_slots = relationship("TimeSlot", back_populates="shop", cascade="all, delete-orphan")
    menu_items = relationship("MenuItem", back_populates="shop", cascade="all, delete-orphan")