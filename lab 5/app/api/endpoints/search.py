# app/api/endpoints/search.py

from fastapi import APIRouter, HTTPException
from app.services.fuzzy_search import levenshtein_distance
from app.cruds.search import get_corpus
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db