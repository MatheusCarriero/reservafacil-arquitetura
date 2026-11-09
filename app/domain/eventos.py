from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class TipoEventoReserva(StrEnum):
    CRIADA = "reserva.criada"
    CANCELADA = "reserva.cancelada"


@dataclass(frozen=True, slots=True)
class EventoReserva:
    tipo: TipoEventoReserva
    reserva_id: int
    usuario_id: int
    sala_id: int
    ocorrido_em: datetime
