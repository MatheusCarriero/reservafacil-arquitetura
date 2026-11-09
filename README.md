
# ReservaFácil

Sistema de gerenciamento de reservas de salas desenvolvido para o
Trabalho Final da disciplina de Arquitetura de Software.

## Objetivo

Permitir o gerenciamento de salas e reservas, evitando conflitos
de horários e aplicando regras de negócio.

## Tecnologias

- Python 3.13
- FastAPI
- SQLite (planejado)
- Ruff
- Pytest

## Requisitos

- Python 3.13
- Git

## Instalação

Clone o repositório:

```bash
git clone https://github.com/MatheusCarriero/reservafacil-arquitetura.git
cd reservafacil-arquitetura
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente no PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## Executar a aplicação

```bash
python -m uvicorn app.main:app --reload
```

Acesse a documentação interativa:

http://127.0.0.1:8000/docs

Verificação de funcionamento:

http://127.0.0.1:8000/health

## Qualidade do código

Verificar regras do Ruff:

```bash
python -m ruff check .
```

Verificar formatação:

```bash
python -m ruff format --check .
```

Executar testes automatizados:

```bash
python -m pytest -q
```

## Organização inicial

- `app/`: código da aplicação
- `tests/`: testes automatizados
- `.github/workflows/`: integração contínua
- `pyproject.toml`: configuração do Ruff e Pytest
- `requirements.txt`: dependências do projeto

## Desenvolvimento colaborativo

As alterações serão desenvolvidas em branches específicas e
integradas ao `main` por Pull Requests revisados.

## Integrantes

A definir.

## Status

Estrutura inicial em desenvolvimento.

A implementação das reservas, regras de negócio, padrões GoF,
ADRs e diagramas será realizada nas próximas etapas.
