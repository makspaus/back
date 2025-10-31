from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.models.webhook_event import WebhookEvent
from app.logger import logger
from datetime import datetime

router = APIRouter(prefix="/webhook", tags=["Webhook"])

@router.post("/order-status")
async def receive_order_status(
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    try:
        start = datetime.utcnow()

        payload = await request.json()
        event_type = payload.get("event") or "unknown"

        logger.info(f"[WEBHOOK] Received: {event_type}, payload={payload}")

        webhook_event = WebhookEvent(event_type=event_type, payload=payload)
        db.add(webhook_event)
        await db.commit()

        duration_ms = (datetime.utcnow() - start).total_seconds() * 1000
        logger.info(f"[WEBHOOK] saved to DB in {duration_ms:.2f} ms")

        return {"status": "ok"}  # MUST reply <1 sec

    except Exception as e:
        logger.error(f"[WEBHOOK] Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Webhook processing failed")
