# app/crud/user.py
import logging
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User, session, device_token, user_favorite  # adjust if class name differs
from app.schemas import UserCreate, UserUpdate, SessionCreate, DeviceTokenCreate, UserFavoriteCreate
from app.crud.base import get_all, get_by_id, create_instance, update_instance, delete_instance,CRUDBase

logger = logging.getLogger("crud.user")

async def list_users(db: AsyncSession):
    return await get_all(db, User)

async def get_user(db: AsyncSession, user_id):
    return await get_by_id(db, User, user_id)

async def create_user(db: AsyncSession, user_in: UserCreate):
    try:
        obj = User(**user_in.model_dump())
        return await create_instance(db, obj)
    except Exception as e:
        logger.exception("create_user failed")
        raise

async def update_user(db: AsyncSession, user_obj, user_in: UserUpdate):
    try:
        return await update_instance(db, user_obj, user_in.model_dump(exclude_none=True))
    except Exception:
        logger.exception("update_user failed")
        raise

async def delete_user(db: AsyncSession, user_obj):
    try:
        return await delete_instance(db, user_obj)
    except Exception:
        logger.exception("delete_user failed")
        raise
