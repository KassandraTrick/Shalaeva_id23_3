# app/api/endpoints/products.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductOut
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.product import Product
from app.schemas.product import ProductOut
from sqlalchemy import func

router = APIRouter()

@router.post("/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(name=product.name, description=product.description, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/search", response_model=list[ProductOut])
def search_products(query: str, db: Session = Depends(get_db)):
    # Фильтрация по имени продукта
    products = db.query(Product).filter(Product.name.ilike(f"%{query}%")).all()
    return products

