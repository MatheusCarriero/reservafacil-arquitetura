import logging

from app.domain.eventos import EventoReserva

logger = logging.getLogger(__name__)


class ObservadorLogReserva:
    def notificar(self, evento: EventoReserva) -> None:
        logger.info(
            "evento_reserva",
            extra={
                "tipo_evento": evento.tipo.value,
                "reserva_id": evento.reserva_id,
                "usuario_id": evento.usuario_id,
                "sala_id": evento.sala_id,
                "ocorrido_em": evento.ocorrido_em.isoformat(),
            },
        )
