# app/cruds/search.py

from sqlalchemy.orm import Session
from app.models.user import User  # Если нужно работать с моделью пользователя

def get_corpus(db: Session, corpus_id: int) -> str:
    # Здесь нужно реализовать извлечение текста по id из базы данных
    # Пример для пользователей: берем всех пользователей и собираем их имена
    corpus = db.query(User.name).filter(User.id == corpus_id).first()
    if corpus:
        return corpus.name  # Возвращаем текст для поиска
    else:
        return ""  # Если нет данных, возвращаем пустую строку
