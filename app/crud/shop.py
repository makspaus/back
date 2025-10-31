# app/crud/shop.py
from sqlalchemy import select
from app.models import Shop, OwnerAccount, OwnerShop, ShopAccount, ShopDeviceToken
from app.schemas import (
    ShopCreate, ShopUpdate, OwnerAccountCreate, OwnerShopCreate, ShopAccountCreate, ShopDeviceTokenCreate
)
from app.crud.base import CRUDBase
import logging
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.shop import Shop
from app.schemas.shop import ShopCreate, ShopUpdate
from app.crud.base import get_all, get_by_id, create_instance, update_instance, delete_instance

logger = logging.getLogger("crud.shop")

async def list_shops(db: AsyncSession, active_only: bool = False):
    if active_only:
        q = await db.execute(select(Shop).where(Shop.is_active == True))
        return q.scalars().all()
    return await get_all(db, Shop)

async def get_shop(db: AsyncSession, shop_id):
    return await get_by_id(db, Shop, shop_id)

    async def get_by_owner(self, db: AsyncSession, owner_id):
        result = await db.execute(select(Shop).join(OwnerShop).where(OwnerShop.owner_id == owner_id))
        return result.scalars().all()

async def create_shop(db: AsyncSession, shop_in: ShopCreate):
    try:
        obj = Shop(**shop_in.model_dump())
        return await create_instance(db, obj)
    except Exception:
        logger.exception("create_shop failed")
        raise

async def update_shop(db: AsyncSession, shop_obj, shop_in: ShopUpdate):
    try:
        return await update_instance(db, shop_obj, shop_in.model_dump(exclude_none=True))
    except Exception:
        logger.exception("update_shop failed")
        raise

async def delete_shop(db: AsyncSession, shop_obj):
    try:
        return await delete_instance(db, shop_obj)
    except Exception:
        logger.exception("delete_shop failed")
        raise

class CRUDOwnerAccount(CRUDBase[OwnerAccount, OwnerAccountCreate, OwnerAccountCreate]):
    pass


class CRUDOwnerShop(CRUDBase[OwnerShop, OwnerShopCreate, OwnerShopCreate]):
    pass


class CRUDShopAccount(CRUDBase[ShopAccount, ShopAccountCreate, ShopAccountCreate]):
    pass


class CRUDShopDeviceToken(CRUDBase[ShopDeviceToken, ShopDeviceTokenCreate, ShopDeviceTokenCreate]):
    pass

owner_account = CRUDOwnerAccount(OwnerAccount)
owner_shop = CRUDOwnerShop(OwnerShop)
shop_account = CRUDShopAccount(ShopAccount)
shop_device_token = CRUDShopDeviceToken(ShopDeviceToken)
