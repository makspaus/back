# app/crud/menu_item.py
import logging
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.menu_item import MenuItem
from app.schemas.menu_item import MenuItemCreate, MenuItemUpdate
from app.crud.base import get_all, get_by_id, create_instance, update_instance, delete_instance

logger = logging.getLogger("crud.menu_item")

async def list_menu_items(db: AsyncSession, shop_id=None):
    if shop_id:
        q = await db.execute(select(MenuItem).where(MenuItem.shop_id == shop_id))
        return q.scalars().all()
    return await get_all(db, MenuItem)

async def get_menu_item(db: AsyncSession, item_id):
    return await get_by_id(db, MenuItem, item_id)

async def create_menu_item(db: AsyncSession, item_in: MenuItemCreate):
    try:
        obj = MenuItem(**item_in.model_dump())
        return await create_instance(db, obj)
    except Exception:
        logger.exception("create_menu_item failed")
        raise

async def update_menu_item(db: AsyncSession, item_obj, item_in: MenuItemUpdate):
    try:
        return await update_instance(db, item_obj, item_in.model_dump(exclude_none=True))
    except Exception:
        logger.exception("update_menu_item failed")
        raise

async def delete_menu_item(db: AsyncSession, item_obj):
    try:
        return await delete_instance(db, item_obj)
    except Exception:
        logger.exception("delete_menu_item failed")
        raise
