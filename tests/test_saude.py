from datetime import datetime

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.api.saude import router

app = FastAPI()
app.include_router(router)
client = TestClient(app)


def test_health_detalhes_retorna_status_ok() -> None:
    response = client.get("/health/detalhes")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_health_detalhes_informa_horario_em_utc() -> None:
    dados = client.get("/health/detalhes").json()

    horario = datetime.fromisoformat(dados["horario_utc"])

    assert horario.utcoffset() is not None
    assert horario.utcoffset().total_seconds() == 0


def test_health_detalhes_informa_uptime_nao_negativo() -> None:
    dados = client.get("/health/detalhes").json()

    assert isinstance(dados["uptime_segundos"], int)
    assert dados["uptime_segundos"] >= 0
