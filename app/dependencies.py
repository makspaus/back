
from app.core.database import AsyncSessionLocal
from sqlalchemy.orm import Session

# Генератор сессий для зависимостей
def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        db.close()
