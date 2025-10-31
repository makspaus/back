# app/crud/base.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update
from typing import Generic, TypeVar, Type, List, Optional, Any
from pydantic import BaseModel

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: AsyncSession, id: Any) -> Optional[ModelType]:
        result = await db.execute(select(self.model).where(self.model.id == id))
        return result.scalar_one_or_none()

    async def get_multi(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[ModelType]:
        result = await db.execute(select(self.model).offset(skip).limit(limit))
        return result.scalars().all()

    async def create(self, db: AsyncSession, obj_in: CreateSchemaType) -> ModelType:
        obj_data = obj_in.dict(exclude_unset=True)
        db_obj = self.model(**obj_data)
        db.add(db_obj)
        await db.flush()
        return db_obj

    async def update(self, db: AsyncSession, db_obj: ModelType, obj_in: UpdateSchemaType) -> ModelType:
        update_data = obj_in.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        await db.flush()
        return db_obj

    async def remove(self, db: AsyncSession, id: Any) -> None:
        await db.execute(delete(self.model).where(self.model.id == id))
        await db.flush()
async def get_all(db: AsyncSession, model: Type):
    q = await db.execute(select(model))
    return q.scalars().all()

async def get_by_id(db: AsyncSession, model: Type, id_):
    q = await db.execute(select(model).where(model.id == id_))
    return q.scalar_one_or_none()

async def create_instance(db: AsyncSession, instance):
    db.add(instance)
    await db.commit()
    await db.refresh(instance)
    return instance

async def delete_instance(db: AsyncSession, instance):
    await db.delete(instance)
    await db.commit()
    return instance

async def update_instance(db: AsyncSession, instance, data: dict):
    for k, v in data.items():
        if hasattr(instance, k):
            setattr(instance, k, v)
    db.add(instance)
    await db.commit()
    await db.refresh(instance)
    return instance
