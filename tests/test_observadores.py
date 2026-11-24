import logging
from datetime import UTC, datetime

from app.domain.eventos import EventoReserva, TipoEventoReserva
from app.infrastructure.observador_log import ObservadorLogReserva
from app.infrastructure.observador_notificacao import (
    ObservadorNotificacaoInterna,
)
from app.infrastructure.publicador_eventos import PublicadorEventosEmMemoria


def criar_evento(tipo: TipoEventoReserva) -> EventoReserva:
    return EventoReserva(
        tipo=tipo,
        reserva_id=1,
        usuario_id=2,
        sala_id=3,
        ocorrido_em=datetime(2026, 11, 23, 10, 0, tzinfo=UTC),
    )


def test_observador_log_registra_campos_do_evento(caplog):
    observador = ObservadorLogReserva()
    evento = criar_evento(TipoEventoReserva.CRIADA)

    with caplog.at_level(logging.INFO):
        observador.notificar(evento)

    registro = caplog.records[0]
    assert registro.getMessage() == "evento_reserva"
    assert registro.tipo_evento == "reserva.criada"
    assert registro.reserva_id == 1
    assert registro.usuario_id == 2
    assert registro.sala_id == 3
    assert registro.ocorrido_em == "2026-11-23T10:00:00+00:00"


def test_notificacao_interna_para_reserva_criada():
    observador = ObservadorNotificacaoInterna()

    observador.notificar(criar_evento(TipoEventoReserva.CRIADA))

    assert observador.notificacoes == ("Reserva 1 criada na sala 3 pelo usuário 2.",)


def test_notificacao_interna_para_reserva_cancelada():
    observador = ObservadorNotificacaoInterna()

    observador.notificar(criar_evento(TipoEventoReserva.CANCELADA))

    assert observador.notificacoes == ("Reserva 1 da sala 3 cancelada pelo usuário 2.",)


def test_publicador_entrega_evento_aos_dois_observadores(caplog):
    publicador = PublicadorEventosEmMemoria()
    observador_log = ObservadorLogReserva()
    observador_notificacao = ObservadorNotificacaoInterna()
    publicador.registrar(observador_log)
    publicador.registrar(observador_notificacao)

    with caplog.at_level(logging.INFO):
        publicador.publicar(criar_evento(TipoEventoReserva.CRIADA))

    assert caplog.records[0].tipo_evento == "reserva.criada"
    assert len(observador_notificacao.notificacoes) == 1
