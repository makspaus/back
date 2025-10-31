# app/routers/shop.py
import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import Optional, List
from app.schemas.shop import ShopCreate, ShopRead, ShopUpdate
from app.crud.shop import list_shops, get_shop, create_shop, update_shop, delete_shop
from app.core.database import get_db
from typing import List
from app import crud, schemas

logger = logging.getLogger("routers.shop")
router = APIRouter(prefix="/shops", tags=["shops"])

@router.get("/", response_model=List[ShopRead])
async def route_list_shops(active: Optional[bool] = Query(None), db: AsyncSession = Depends(get_db)):
    if active is True:
        shops = await list_shops(db, active_only=True)
    else:
        shops = await list_shops(db)
    return shops

@router.get("/{shop_id}", response_model=ShopRead)
async def route_get_shop(shop_id: UUID, db: AsyncSession = Depends(get_db)):
    shop = await get_shop(db, shop_id)
    if not shop:
        raise HTTPException(404, "Shop not found")
    return shop

@router.post("/", response_model=ShopRead, status_code=201)
async def route_create_shop(payload: ShopCreate, db: AsyncSession = Depends(get_db)):
    obj = await create_shop(db, payload)
    return obj

@router.put("/{shop_id}", response_model=ShopRead)
async def route_update_shop(shop_id: UUID, payload: ShopUpdate, db: AsyncSession = Depends(get_db)):
    shop = await get_shop(db, shop_id)
    if not shop:
        raise HTTPException(404, "Shop not found")
    updated = await update_shop(db, shop, payload)
    return updated

@router.delete("/{shop_id}", response_model=ShopRead)
async def route_delete_shop(shop_id: UUID, db: AsyncSession = Depends(get_db)):
    shop = await get_shop(db, shop_id)
    if not shop:
        raise HTTPException(404, "Shop not found")
    deleted = await delete_shop(db, shop)
    return deleted

# === OWNER ACCOUNTS ===
@router.post("/owners", response_model=schemas.OwnerAccount)
async def create_owner(owner_in: schemas.OwnerAccountCreate, db: AsyncSession = Depends(get_db)):
    logger.info(f"Creating owner account: {owner_in.email}")
    return await crud.owner_account.create(db, owner_in)


@router.post("/owners/{owner_id}/shops", response_model=schemas.OwnerShop)
async def link_owner_shop(owner_id: str, link_in: schemas.OwnerShopCreate, db: AsyncSession = Depends(get_db)):
    link_in.owner_id = owner_id
    logger.info(f"Linking owner {owner_id} to shop {link_in.shop_id}")
    return await crud.owner_shop.create(db, link_in)


# === SHOP ACCOUNTS ===
@router.post("/{shop_id}/accounts", response_model=schemas.ShopAccount)
async def create_shop_account(shop_id: str, acc_in: schemas.ShopAccountCreate, db: AsyncSession = Depends(get_db)):
    acc_in.shop_id = shop_id
    logger.info(f"Creating shop account for shop={shop_id}")
    return await crud.shop_account.create(db, acc_in)


# === SHOP DEVICE TOKENS ===
@router.post("/accounts/{acc_id}/tokens", response_model=schemas.ShopDeviceToken)
async def register_shop_token(acc_id: str, token_in: schemas.ShopDeviceTokenCreate, db: AsyncSession = Depends(get_db)):
    token_in.shop_account_id = acc_id
    logger.info(f"Registering shop device token for account={acc_id}")
    return await crud.shop_device_token.create(db, token_in)