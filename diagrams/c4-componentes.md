
# C4 — Componentes do ReservaFácil

## Estado atual da arquitetura

Este diagrama representa os componentes já criados
na branch `feat/arquitetura-contratos`.

```mermaid
C4Component
    title ReservaFacil - Componentes atuais do Backend

    Container_Boundary(backend, "Backend ReservaFacil") {
        Component(api, "Aplicacao FastAPI", "Python / FastAPI", "Inicializa a API em app/main.py")

        Component(health, "Health Check", "FastAPI", "Disponibiliza GET /health")

        Component(modelos, "Modelos do Dominio", "Python / dataclasses", "Usuario, Sala, SolicitacaoReserva e ContextoPoliticaReserva")

        Component(contratos, "Contratos do Dominio", "Python / Protocol", "Interfaces de repositorios, politicas e eventos")

        Component(eventos, "Eventos de Reserva", "Python", "Tipos e dados dos eventos de reserva")
    }

    Rel(api, health, "chamada", "HTTP interno")
    Rel(contratos, modelos, "chamada", "Referencias de tipos Python")
    Rel(contratos, eventos, "chamada", "Referencias de tipos Python")
```

## Componentes previstos

Ainda serao implementados pelos demais integrantes:

- API de cadastros de usuarios e salas.
- Servicos de aplicacao para reservas.
- Repositorios concretos de SQLite.
- Politicas de reserva com Strategy.
- Controle de estados com State.
- Publicador e observadores de eventos.

Esses componentes serao incorporados ao diagrama
conforme seus respectivos Pull Requests forem integrados.

## Evidencias iniciais

- `app/main.py`
- `app/domain/modelos.py`
- `app/domain/contratos.py`
- `app/domain/eventos.py`

Os links permanentes para o codigo serao adicionados
apos a revisao e integracao dos Pull Requests.
