# app/cruds/tsp.py

from typing import List

def solve_tsp(query: str) -> List[str]:
    # Примерный алгоритм для задачи коммивояжера.
    cities = query.split(",")
    route = cities  # Можешь заменить на более сложную логику, если нужно.
    return route
