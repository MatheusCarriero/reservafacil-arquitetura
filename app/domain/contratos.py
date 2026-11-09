from datetime import datetime
from typing import Protocol

from app.domain.eventos import EventoReserva
from app.domain.modelos import (
    ContextoPoliticaReserva,
    Sala,
    SolicitacaoReserva,
    Usuario,
)


class RepositorioUsuarios(Protocol):
    def obter(self, usuario_id: int) -> Usuario | None: ...


class RepositorioSalas(Protocol):
    def obter(self, sala_id: int) -> Sala | None: ...


class RepositorioReservas(Protocol):
    def existe_conflito(
        self,
        sala_id: int,
        inicio: datetime,
        fim: datetime,
    ) -> bool: ...

    def criar_se_disponivel(
        self,
        solicitacao: SolicitacaoReserva,
    ) -> int | None: ...


class PoliticaReserva(Protocol):
    def validar(
        self,
        solicitacao: SolicitacaoReserva,
        contexto: ContextoPoliticaReserva,
    ) -> None: ...


class ObservadorReserva(Protocol):
    def notificar(self, evento: EventoReserva) -> None: ...


class PublicadorEventosReserva(Protocol):
    def registrar(self, observador: ObservadorReserva) -> None: ...

    def publicar(self, evento: EventoReserva) -> None: ...
