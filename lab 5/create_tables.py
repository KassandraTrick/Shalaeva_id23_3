from app.db.database import engine
from app.models.product import Product
from app.db.database import Base

# Создание всех таблиц, если они еще не были созданы
Base.metadata.create_all(bind=engine)
