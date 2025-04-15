# app/cruds/product.py

from sqlalchemy.orm import Session
from app.models.product import Product
import Levenshtein

def fuzzy_search_products(db: Session, query: str, threshold: int = 3):
    products = db.query(Product).all()
    result = []
    for product in products:
        distance = Levenshtein.distance(query.lower(), product.name.lower())
        if distance <= threshold:
            result.append(product)
    return result
