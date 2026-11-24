from datetime import UTC, datetime
from time import monotonic

from fastapi import APIRouter

router = APIRouter(tags=["Infraestrutura"])

_INICIO = monotonic()


@router.get("/health/detalhes")
def health_detalhes() -> dict[str, str | int]:
    return {
        "status": "ok",
        "horario_utc": datetime.now(UTC).isoformat(),
        "uptime_segundos": int(monotonic() - _INICIO),
    }
