# app/schemas/tsp.py

from pydantic import BaseModel
from typing import List, Tuple

# Схема для запроса (получаем список городов с их координатами)
class TSPRequest(BaseModel):
    cities: List[Tuple[float, float]]  # Список городов, каждый город — это кортеж с координатами (x, y)

# Схема для ответа (маршрут и расстояние)
class TSPResponse(BaseModel):
    path: List[Tuple[float, float]]  # Оптимальный путь, список городов в порядке посещения
    distance: float  # Общая длина пути
