# app/api/endpoints/tsp.py

from fastapi import APIRouter
from app.schemas.tsp import TSPRequest, TSPResponse
from typing import List
import itertools

router = APIRouter()

@router.post("/solve", response_model=TSPResponse)
def solve_tsp(request: TSPRequest):
    cities = request.cities
    # Пример простого решения задачи коммивояжера методом полного перебора
    best_path = None
    best_distance = float('inf')

    for perm in itertools.permutations(cities):
        distance = calculate_total_distance(perm)
        if distance < best_distance:
            best_distance = distance
            best_path = perm

    return TSPResponse(path=best_path, distance=best_distance)

def calculate_total_distance(path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_between(path[i], path[i+1])
    total_distance += distance_between(path[-1], path[0])  # Закрытие пути
    return total_distance

def distance_between(city1, city2):
    # Примерная функция для вычисления расстояния между городами
    return ((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)**0.5

