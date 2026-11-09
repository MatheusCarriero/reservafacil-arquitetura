from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Usuario:
    id: int
    nome: str
    email: str


@dataclass(frozen=True, slots=True)
class Sala:
    id: int
    nome: str
    capacidade: int
    ativa: bool = True


@dataclass(frozen=True, slots=True)
class SolicitacaoReserva:
    usuario_id: int
    sala_id: int
    inicio: datetime
    fim: datetime


@dataclass(frozen=True, slots=True)
class ContextoPoliticaReserva:
    quantidade_reservas_ativas_usuario: int
