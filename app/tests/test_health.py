"""
Minimal smoke test. Extend with a mocked model to test /predict without
needing a real MLflow model registry available in CI.
"""
from unittest.mock import patch

from fastapi.testclient import TestClient


def test_health_endpoint():
    with patch("app.main.mlflow.pyfunc.load_model"):
        from app.main import app
        client = TestClient(app)
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
