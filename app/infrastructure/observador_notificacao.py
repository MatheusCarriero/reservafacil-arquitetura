from app.domain.eventos import EventoReserva, TipoEventoReserva

_MODELOS_MENSAGEM = {
    TipoEventoReserva.CRIADA: (
        "Reserva {reserva_id} criada na sala {sala_id} pelo usuário {usuario_id}."
    ),
    TipoEventoReserva.CANCELADA: (
        "Reserva {reserva_id} da sala {sala_id} cancelada pelo usuário {usuario_id}."
    ),
}


class ObservadorNotificacaoInterna:
    def __init__(self) -> None:
        self._notificacoes: list[str] = []

    @property
    def notificacoes(self) -> tuple[str, ...]:
        return tuple(self._notificacoes)

    def notificar(self, evento: EventoReserva) -> None:
        modelo = _MODELOS_MENSAGEM[evento.tipo]
        mensagem = modelo.format(
            reserva_id=evento.reserva_id,
            sala_id=evento.sala_id,
            usuario_id=evento.usuario_id,
        )
        self._notificacoes.append(mensagem)
