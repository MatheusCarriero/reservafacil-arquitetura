from dataclasses import FrozenInstanceError
from datetime import UTC, datetime

import pytest

from app.domain.eventos import EventoReserva, TipoEventoReserva
from app.domain.modelos import (
    ContextoPoliticaReserva,
    Sala,
    SolicitacaoReserva,
    Usuario,
)


def test_criar_usuario() -> None:
    usuario = Usuario(
        id=1,
        nome="João",
        email="joao@exemplo.com",
    )

    assert usuario.id == 1
    assert usuario.nome == "João"


def test_usuario_nao_pode_ser_modificado() -> None:
    usuario = Usuario(
        id=1,
        nome="João",
        email="joao@exemplo.com",
    )

    with pytest.raises(FrozenInstanceError):
        usuario.nome = "Maria"


def test_sala_ativa_por_padrao() -> None:
    sala = Sala(
        id=1,
        nome="Sala de Reunião",
        capacidade=10,
    )

    assert sala.ativa is True


def test_criar_solicitacao_reserva() -> None:
    inicio = datetime(2026, 11, 10, 14, 0, tzinfo=UTC)
    fim = datetime(2026, 11, 10, 15, 0, tzinfo=UTC)

    solicitacao = SolicitacaoReserva(
        usuario_id=1,
        sala_id=2,
        inicio=inicio,
        fim=fim,
    )

    assert solicitacao.usuario_id == 1
    assert solicitacao.sala_id == 2
    assert solicitacao.inicio == inicio
    assert solicitacao.fim == fim


def test_contexto_politica_reserva() -> None:
    contexto = ContextoPoliticaReserva(
        quantidade_reservas_ativas_usuario=2,
    )

    assert contexto.quantidade_reservas_ativas_usuario == 2


def test_criar_evento_reserva() -> None:
    evento = EventoReserva(
        tipo=TipoEventoReserva.CRIADA,
        reserva_id=10,
        usuario_id=1,
        sala_id=2,
        ocorrido_em=datetime.now(UTC),
    )

    assert evento.tipo == TipoEventoReserva.CRIADA
    assert evento.reserva_id == 10
