from fastapi import APIRouter
from app.routers import users, shops, orders

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(shops.router, prefix="/shops", tags=["Shops"])
api_router.include_router(orders.router, prefix="/orders", tags=["Orders"])
