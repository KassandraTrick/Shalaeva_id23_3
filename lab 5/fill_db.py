from app.db.database import SessionLocal, engine
from app.models.product import Product
from sqlalchemy.orm import Session

# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Заполнение базы данных
def fill_database():
    db: Session = next(get_db())  # Получаем сессию
    # Добавляем продукты
    products = [
        Product(name="Apple", description="Fresh red apple", price=1.2),
        Product(name="Banana", description="Yellow ripe banana", price=0.5),
        Product(name="Orange", description="Juicy orange", price=0.8),
        Product(name="Strawberry", description="Sweet red strawberry", price=2.5),
        Product(name="Pineapple", description="Tropical pineapple", price=3.0),
    ]
    
    db.add_all(products)  # Добавляем все продукты
    db.commit()  # Сохраняем изменения
    print("Database filled with products.")

if __name__ == "__main__":
    fill_database()
