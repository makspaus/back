# app/main.py
import logging
from fastapi import FastAPI, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.core.database import engine, Base
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.routers import users, shops, orders
from app.crud import order as crud_order
from app.routers import webhooks


LOGFILE = "app.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    handlers=[
        logging.FileHandler(LOGFILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("app")


# Импорт всех моделей
from app import models



app = FastAPI(title="Coffee Aggregator API")

app.include_router(webhooks.router)

app.include_router(users.router)
app.include_router(shops.router)
app.include_router(orders.router)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"request start: {request.method} {request.url}")
    try:
        response = await call_next(request)
        logger.info(f"request complete: {request.method} {request.url} -> {response.status_code}")
        return response
    except Exception as e:
        logger.exception("Unhandled exception in request")
        raise

@app.get("/health/db")
async def check_db_connection(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT now()"))
        time = result.scalar_one()
        return {"status": "ok", "time": str(time)}
    except Exception as e:
        return {"status": "error", "details": str(e)}

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database initialized successfully.")

@app.get("/")
async def root():
    return {"HELLO": "API is running 🚀"}

