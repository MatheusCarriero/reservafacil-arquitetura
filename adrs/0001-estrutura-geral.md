
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

## Implementação

Issue relacionada:
https://github.com/MatheusCarriero/reservafacil-arquitetura/issues/2

PR de implementação: pendente.

Evidências iniciais:
- app/domain/modelos.py
- app/domain/contratos.py
- app/domain/eventos.py

Os links permanentes para o código serão adicionados
após a implementação e revisão do Pull Request.
