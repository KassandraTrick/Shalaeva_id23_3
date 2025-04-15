# app/models/product.py
from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

from sqlalchemy import Column, Integer, String, Float

class Product(Base):
    __tablename__ = "product"  # Название таблицы

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)  # Добавлен новый столбец
    price = Column(Float)