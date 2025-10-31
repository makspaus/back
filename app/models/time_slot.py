import sqlalchemy as sa
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Boolean, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base

class TimeSlot(Base):
    __tablename__ = "time_slots"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    shop_id = Column(UUID(as_uuid=True), ForeignKey("shops.id", ondelete="CASCADE"), nullable=False)
    start = Column(DateTime(timezone=True))
    end = Column(DateTime(timezone=True))
    capacity = Column(Integer)
    is_active = Column(Boolean, default=True)

    shop = relationship("Shop", back_populates="time_slots")
    slot_holds = relationship("SlotHold", back_populates="slot", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="slot", cascade="all, delete-orphan")
