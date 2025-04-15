#app/core/celery.py

from celery import Celery
from app.core.config import settings
from app.services.search import complex_search_function

app = Celery(
    'tasks',
    broker=settings.REDIS_URL,  # Укажи ссылку на Redis
    backend=settings.REDIS_URL
)

@app.task
def process_large_search(query):
    # Example of a task
    return complex_search_function(query)
