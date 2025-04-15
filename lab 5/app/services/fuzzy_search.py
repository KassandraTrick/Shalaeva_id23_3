#app/services/fuzzy_search.py

import Levenshtein

def fuzzy_search_products(db: Session, query: str, threshold: int = 3):
    products = db.query(Product).all()
    results = []
    for product in products:
        distance = Levenshtein.distance(query.lower(), product.name.lower())
        if distance <= threshold:
            results.append((distance, product))
    results.sort(key=lambda x: x[0])  # Sort by distance
    return [r[1] for r in results]
