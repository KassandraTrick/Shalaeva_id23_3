from fastapi.testclient import TestClient
from app.main import app  # предполагаем, что app — это твой FastAPI-приложение

@pytest.mark.asyncio
async def test_create_user():
    client = TestClient(app)  # создаем клиент, передавая FastAPI приложение
    response = client.post("/users", json={"username": "test", "password": "secret"})
    assert response.status_code == 200
