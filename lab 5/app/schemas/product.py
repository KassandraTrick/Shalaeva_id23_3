# app/schemas/product.py

from pydantic import BaseModel

class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        from_attributes = True  # Заменили orm_mode на from_attributes

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

    class Config:
            from_attributes = True