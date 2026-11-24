import io
import json
import logging
from datetime import UTC, datetime

from app.domain.eventos import EventoReserva, TipoEventoReserva
from app.infrastructure.logging_config import (
    FormatadorJson,
    configurar_logging,
)
from app.infrastructure.observador_log import ObservadorLogReserva


def criar_logger(nome: str) -> tuple[logging.Logger, io.StringIO]:
    fluxo = io.StringIO()
    handler = logging.StreamHandler(fluxo)
    handler.setFormatter(FormatadorJson())
    logger = logging.getLogger(nome)
    logger.handlers = [handler]
    logger.setLevel(logging.INFO)
    logger.propagate = False
    return logger, fluxo


def test_formatador_gera_json_com_campos_basicos():
    logger, fluxo = criar_logger("teste.basico")

    logger.info("ola")

    dados = json.loads(fluxo.getvalue())
    assert dados["mensagem"] == "ola"
    assert dados["nivel"] == "INFO"
    assert dados["logger"] == "teste.basico"
    assert "timestamp" in dados


def test_formatador_inclui_campos_extras():
    logger, fluxo = criar_logger("teste.extras")

    logger.info("evento", extra={"reserva_id": 1, "sala_id": 3})

    dados = json.loads(fluxo.getvalue())
    assert dados["reserva_id"] == 1
    assert dados["sala_id"] == 3


def test_formatador_inclui_excecao():
    logger, fluxo = criar_logger("teste.excecao")

    try:
        raise ValueError("boom")
    except ValueError:
        logger.exception("falhou")

    dados = json.loads(fluxo.getvalue())
    assert dados["nivel"] == "ERROR"
    assert "ValueError: boom" in dados["excecao"]


def test_observador_log_gera_json_com_campos_do_evento():
    fluxo = io.StringIO()
    handler = logging.StreamHandler(fluxo)
    handler.setFormatter(FormatadorJson())
    logger = logging.getLogger("app.infrastructure.observador_log")
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    evento = EventoReserva(
        tipo=TipoEventoReserva.CRIADA,
        reserva_id=1,
        usuario_id=2,
        sala_id=3,
        ocorrido_em=datetime(2026, 11, 23, 10, 0, tzinfo=UTC),
    )

    try:
        ObservadorLogReserva().notificar(evento)
    finally:
        logger.removeHandler(handler)
        logger.setLevel(logging.NOTSET)

    dados = json.loads(fluxo.getvalue())
    assert dados["mensagem"] == "evento_reserva"
    assert dados["tipo_evento"] == "reserva.criada"
    assert dados["ocorrido_em"] == "2026-11-23T10:00:00+00:00"


def test_configurar_logging_nao_duplica_handler():
    raiz = logging.getLogger()
    nivel_original = raiz.level
    try:
        configurar_logging()
        configurar_logging()
        handlers_json = [
            h for h in raiz.handlers if isinstance(h.formatter, FormatadorJson)
        ]
        assert len(handlers_json) == 1
    finally:
        for h in list(raiz.handlers):
            if isinstance(h.formatter, FormatadorJson):
                raiz.removeHandler(h)
        raiz.setLevel(nivel_original)
