import logging
from datetime import datetime

from app.domain.eventos import EventoReserva, TipoEventoReserva
from app.infrastructure.publicador_eventos import PublicadorEventosEmMemoria


def criar_evento() -> EventoReserva:
    return EventoReserva(
        tipo=TipoEventoReserva.CRIADA,
        reserva_id=1,
        usuario_id=2,
        sala_id=3,
        ocorrido_em=datetime(2026, 11, 23, 10, 0),
    )


class ObservadorGravador:
    def __init__(self) -> None:
        self.recebidos: list[EventoReserva] = []

    def notificar(self, evento: EventoReserva) -> None:
        self.recebidos.append(evento)


class ObservadorQueFalha:
    def notificar(self, evento: EventoReserva) -> None:
        raise RuntimeError("falha de teste")


def test_publicar_entrega_evento_ao_observador_registrado():
    publicador = PublicadorEventosEmMemoria()
    observador = ObservadorGravador()
    publicador.registrar(observador)
    evento = criar_evento()

    publicador.publicar(evento)

    assert observador.recebidos == [evento]


def test_publicar_entrega_evento_a_todos_os_observadores():
    publicador = PublicadorEventosEmMemoria()
    primeiro = ObservadorGravador()
    segundo = ObservadorGravador()
    publicador.registrar(primeiro)
    publicador.registrar(segundo)
    evento = criar_evento()

    publicador.publicar(evento)

    assert primeiro.recebidos == [evento]
    assert segundo.recebidos == [evento]


def test_publicar_sem_observadores_nao_gera_erro():
    publicador = PublicadorEventosEmMemoria()

    publicador.publicar(criar_evento())


def test_falha_de_um_observador_nao_impede_os_demais(caplog):
    publicador = PublicadorEventosEmMemoria()
    saudavel = ObservadorGravador()
    publicador.registrar(ObservadorQueFalha())
    publicador.registrar(saudavel)
    evento = criar_evento()

    with caplog.at_level(logging.ERROR):
        publicador.publicar(evento)

    assert saudavel.recebidos == [evento]
    assert "ObservadorQueFalha" in caplog.text
