from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Boolean, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base

from sqlalchemy import UniqueConstraint


class UserFavorite(Base):
    __tablename__ = "user_favorites"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("app_users.id", ondelete="CASCADE"), nullable=False)
    shop_id = Column(UUID(as_uuid=True), ForeignKey("shops.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Чтобы не было дублей "пользователь — кофейня"
    __table_args__ = (UniqueConstraint("user_id", "shop_id", name="uq_user_shop_favorite"),)

    user = relationship("User", back_populates="favorites")
    shop = relationship("Shop", back_populates="favorited_by")