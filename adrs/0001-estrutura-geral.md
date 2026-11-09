
# ADR-0001 — Arquitetura monolítica modular em camadas

## Status

Proposto — aguardando revisão e aprovação.

## Contexto

O ReservaFácil é um sistema acadêmico de gerenciamento
de reservas de salas.

O projeto será desenvolvido por cinco integrantes e
precisa demonstrar organização arquitetural, princípios
SOLID, Clean Code e padrões GoF.

O sistema envolve diferentes responsabilidades:
gerenciamento de usuários e salas, reservas, políticas
de negócio, persistência e notificações.

É necessário organizar essas funcionalidades sem
introduzir complexidade operacional desnecessária.

## Decisão

Adotar um monolito modular em Python e FastAPI,
com organização interna em quatro camadas:

- API: recebe requisições HTTP.
- Application: coordena os casos de uso.
- Domain: contém modelos e contratos de negócio.
- Infrastructure: implementa persistência e integrações.

As regras de negócio deverão utilizar abstrações
sempre que necessário, evitando dependência direta
de mecanismos de persistência e frameworks.

## Alternativas consideradas

### Microsserviços

Descartados devido à necessidade de comunicação
distribuída, maior complexidade operacional e custos
de implantação incompatíveis com o escopo atual.

### Monolito sem separação de camadas

Descartado porque aumentaria o risco de acoplamento
entre rotas HTTP, regras de negócio e banco de dados.

## Consequências positivas

- Separação clara de responsabilidades.
- Facilidade de testes automatizados.
- Organização do trabalho entre integrantes.
- Maior facilidade para substituir implementações.
- Melhor manutenção das regras de negócio.

## Consequências negativas

- Maior quantidade de arquivos e interfaces.
- Necessidade de coordenar os contratos compartilhados.
- Mais indireção para operações simples.

## Implementação e evidências

**Issue relacionada:** [Issue #2 — Arquitetura e contratos](https://github.com/MatheusCarriero/reservafacil-arquitetura/issues/2)

**Pull Request:** [PR #7 — Arquitetura e contratos](https://github.com/MatheusCarriero/reservafacil-arquitetura/pull/7)

**Commit de referência:** `00b28b17241867cd405046c12030b39c28a8872a`

### 1. Organização em camadas

A estrutura inicial está organizada nos seguintes pacotes:

- `app/api/` — camada de comunicação HTTP.
- `app/application/` — camada dos casos de uso.
- `app/domain/` — modelos, contratos e eventos.
- `app/infrastructure/` — implementações de persistência e integrações.

As pastas foram criadas para separar as responsabilidades. No estágio atual, as camadas API, Application e Infrastructure ainda não possuem todas as funcionalidades previstas.

### 2. Modelos de domínio

Os modelos são definidos utilizando `dataclasses` do Python.

Exemplo:

```python
@dataclass(frozen=True, slots=True)
class Usuario:
    id: int
    nome: str
    email: str
```

**Evidência:** [app/domain/modelos.py — linhas 5 a 9](https://github.com/MatheusCarriero/reservafacil-arquitetura/blob/00b28b17241867cd405046c12030b39c28a8872a/app/domain/modelos.py#L5-L9)

Essa estrutura representa os dados do domínio sem depender diretamente do FastAPI ou do SQLite.

### 3. Contratos de persistência

As interfaces dos repositórios utilizam `Protocol`, permitindo definir operações sem escolher uma implementação concreta.

Exemplo:

```python
class RepositorioUsuarios(Protocol):
    def obter(self, usuario_id: int) -> Usuario | None: ...
```

**Evidência:** [app/domain/contratos.py — linhas 13 a 14](https://github.com/MatheusCarriero/reservafacil-arquitetura/blob/00b28b17241867cd405046c12030b39c28a8872a/app/domain/contratos.py#L13-L14)

Os serviços poderão depender dessas abstrações, enquanto a implementação do acesso ao banco de dados ficará na camada Infrastructure.

### 4. Contratos de políticas e eventos

Foram definidas interfaces para as futuras políticas de reserva e para a comunicação por eventos.

Exemplo:

```python
class ObservadorReserva(Protocol):
    def notificar(self, evento: EventoReserva) -> None: ...
```

**Evidência:** [app/domain/contratos.py — linhas 43 a 44](https://github.com/MatheusCarriero/reservafacil-arquitetura/blob/00b28b17241867cd405046c12030b39c28a8872a/app/domain/contratos.py#L43-L44)

Os contratos preparam a integração futura dos padrões Strategy e Observer, sem afirmar que esses padrões já foram implementados.

### 5. Testes automatizados

Os modelos do domínio possuem testes automatizados, incluindo a verificação de imutabilidade da classe Usuario.

**Evidência:** [tests/test_domain.py — linhas 26 a 34](https://github.com/MatheusCarriero/reservafacil-arquitetura/blob/00b28b17241867cd405046c12030b39c28a8872a/tests/test_domain.py#L26-L34)

A validação local realizada nesta etapa apresentou sete testes aprovados.

### 6. Limitações da implementação atual

A arquitetura ainda está em desenvolvimento.

Nesta etapa foram implementados os modelos e contratos compartilhados. Os serviços completos de reservas, a persistência SQLite e as implementações dos padrões GoF serão desenvolvidos posteriormente pelos integrantes responsáveis.

O diagrama atual está disponível em [C4 — Componentes](../diagrams/c4-componentes.md) e será atualizado conforme os módulos forem implementados.