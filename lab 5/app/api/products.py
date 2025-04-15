# app/api/products.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.product import Product
from app.schemas.product import ProductOut, ProductCreate  # Импортируем ProductOut здесь
import Levenshtein

router = APIRouter()

@router.get("/search", response_model=list[ProductOut])
def search_products(query: str = Query(...), db: Session = Depends(get_db)):
    # Получаем все продукты из базы данных
    products = db.query(Product).all()

    # Если нет продуктов в базе, сразу возвращаем пустой список
    if not products:
        return []

    # Выполняем поиск с использованием Levenshtein
    results = []
    for product in products:
        # Считаем расстояние Левенштейна
        distance = Levenshtein.distance(query.lower(), product.name.lower())
        if distance <= 3:  # Порог для поиска
            results.append((distance, product))

    # Сортируем результаты по расстоянию
    results.sort(key=lambda x: x[0])

    # Возвращаем только продукты
    return [r[1] for r in results]

@router.post("/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(name=product.name, description=product.description, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
