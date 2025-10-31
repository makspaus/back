# app/routers/order.py
import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List
from app.schemas.order import OrderCreate, OrderRead, OrderUpdate
from app.crud.order import list_orders, get_order, create_order, update_order, delete_order
from app.core.database import get_db
from app import crud, schemas
from typing import List
from app.schemas.menu_item import MenuItemBase, MenuItemRead

logger = logging.getLogger("routers.order")
router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("/", response_model=List[OrderRead])
async def route_list_orders(shop_id: UUID = None, db: AsyncSession = Depends(get_db)):
    orders = await list_orders(db, shop_id=shop_id)
    return orders

@router.get("/{order_id}", response_model=OrderRead)
async def route_get_order(order_id: UUID, db: AsyncSession = Depends(get_db)):
    order = await get_order(db, order_id)
    if not order:
        raise HTTPException(404, "Order not found")
    return order

@router.post("/", response_model=OrderRead, status_code=201)
async def route_create_order(payload: OrderCreate, db: AsyncSession = Depends(get_db)):
    new_order = await create_order(db, payload)
    return new_order

@router.put("/{order_id}", response_model=OrderRead)
async def route_update_order(order_id: UUID, payload: OrderUpdate, db: AsyncSession = Depends(get_db)):
    order = await get_order(db, order_id)
    if not order:
        raise HTTPException(404, "Order not found")
    updated = await update_order(db, order, payload)
    return updated

@router.delete("/{order_id}", response_model=OrderRead)
async def route_delete_order(order_id: UUID, db: AsyncSession = Depends(get_db)):
    order = await get_order(db, order_id)
    if not order:
        raise HTTPException(404, "Order not found")
    deleted = await delete_order(db, order)
    return deleted

# === MENU ITEMS ===
@router.post("/menu", response_model=schemas.MenuItemBase)
async def create_menu_item(item_in: schemas.MenuItemCreate, db: AsyncSession = Depends(get_db)):
    logger.info(f"Creating menu item {item_in.name} for shop={item_in.shop_id}")
    return await crud.menu_item.create(db, item_in)


@router.get("/menu", response_model=List[schemas.MenuItemBase])
async def list_menu_items(db: AsyncSession = Depends(get_db)):
    logger.info("Listing menu items")
    return await crud.menu_item.get_multi(db)


# === TIME SLOTS ===
@router.post("/slots", response_model=schemas.TimeSlot)
async def create_time_slot(slot_in: schemas.TimeSlotCreate, db: AsyncSession = Depends(get_db)):
    logger.info(f"Creating timeslot for shop={slot_in.shop_id}")
    return await crud.time_slot.create(db, slot_in)

@router.get("/slots", response_model=List[schemas.TimeSlot])
async def list_time_slots(db: AsyncSession = Depends(get_db)):
    logger.info("Listing time slots")
    return await crud.time_slot.get_multi(db)