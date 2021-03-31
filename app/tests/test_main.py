from app.main.app import create_app
from fastapi.testclient import TestClient

app = create_app()

client = TestClient(app)