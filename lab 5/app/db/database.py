# app/db/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Определяем Base здесь
Base = declarative_base()

# Здесь создаем подключение к базе данных
engine = create_engine('sqlite:///./test.db')  # Замените на ваш URL подключения

# Сессия
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
