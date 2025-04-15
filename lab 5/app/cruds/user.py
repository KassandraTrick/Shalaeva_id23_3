#app/cruds/user.py

import bcrypt
from app.models.user import User
from app.schemas.user import UserCreate
from sqlalchemy.orm import Session

def create_user(db: Session, user: UserCreate):
    # Хешируем пароль перед добавлением в базу
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    
    db_user = User(username=user.username, email=user.email, name=user.name, password=hashed_password.decode('utf-8'))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
