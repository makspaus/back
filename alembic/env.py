from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.core.database import Base
from app.models import *  # импорт моделей

# Настройки Alembic
config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

# ВАЖНО: заменить async-ссылку на sync для alembic
import os

DATABASE_URL = os.getenv("DATABASE_URL_SYNC", "postgresql+psycopg2://coffee_user:3004@localhost:5432/cafe")

def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        {"sqlalchemy.url": DATABASE_URL},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
