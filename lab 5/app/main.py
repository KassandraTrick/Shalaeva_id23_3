# app/main.py

from fastapi import FastAPI
from app.api.endpoints import users  # Импортируем роуты для пользователей
from app.db import Base, engine
from app.api.endpoints import products, tsp  # Импортируем роуты для продуктов и tsp

from sqlalchemy import text  # Добавляем импорт text для SQL-запросов

# Проверяем таблицы в базе данных
print("Существующие таблицы в базе данных:")
with engine.connect() as connection:
    result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
    for row in result:
        print(row)

# Создаем приложение
app = FastAPI()

# Создаем все таблицы
Base.metadata.create_all(bind=engine)

# Подключаем роуты
app.include_router(users.router)  # Подключаем роуты для пользователей
app.include_router(products.router, prefix="/products", tags=["products"])  # Подключаем роуты для продуктов
app.include_router(tsp.router, prefix="/tsp", tags=["tsp"])  # Подключаем роуты для tsp



