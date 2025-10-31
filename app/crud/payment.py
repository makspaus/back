# app/crud/payment.py
import logging
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.payment import Payment
from app.schemas.payment import PaymentCreate
from app.crud.base import get_all, get_by_id, create_instance, update_instance, delete_instance

logger = logging.getLogger("crud.payment")

async def list_payments(db: AsyncSession, order_id=None):
    if order_id:
        q = await db.execute(select(Payment).where(Payment.order_id == order_id))
        return q.scalars().all()
    return await get_all(db, Payment)

async def get_payment(db: AsyncSession, payment_id):
    return await get_by_id(db, Payment, payment_id)

async def create_payment(db: AsyncSession, payment_in: PaymentCreate, order_id=None):
    try:
        data = payment_in.model_dump()
        if order_id:
            data["order_id"] = order_id
        obj = Payment(**data)
        return await create_instance(db, obj)
    except Exception:
        logger.exception("create_payment failed")
        raise
