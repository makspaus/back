import sqlalchemy as sa
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base

class OwnerAccount(Base):
    __tablename__ = 'owner_accounts'


    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = sa.Column(sa.String, nullable=False)
    password_hash = sa.Column(sa.String, nullable=False)
    created_at = sa.Column(sa.DateTime(timezone=True))
