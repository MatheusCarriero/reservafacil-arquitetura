import logging

from app.domain.contratos import ObservadorReserva
from app.domain.eventos import EventoReserva

logger = logging.getLogger(__name__)


class PublicadorEventosEmMemoria:
    def __init__(self) -> None:
        self._observadores: list[ObservadorReserva] = []

    def registrar(self, observador: ObservadorReserva) -> None:
        self._observadores.append(observador)

    def publicar(self, evento: EventoReserva) -> None:
        for observador in self._observadores:
            try:
                observador.notificar(evento)
            except Exception:
                logger.exception(
                    "Falha ao notificar observador %s para o evento %s",
                    type(observador).__name__,
                    evento.tipo,
                )
