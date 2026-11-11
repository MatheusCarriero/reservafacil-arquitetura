# 1. Contexto e Visão Geral — ReservaFácil

## 1.1. Apresentação do projeto

O **ReservaFácil** é um sistema acadêmico de gerenciamento de reservas de salas, desenvolvido como trabalho final da disciplina de Arquitetura de Software.

O projeto tem como objetivo aplicar conceitos de arquitetura de software, boas práticas de programação e padrões de projeto no desenvolvimento de uma aplicação organizada, testável e de fácil manutenção.

O desenvolvimento é realizado por uma equipe de cinco integrantes, com responsabilidades distribuídas entre arquitetura, persistência de dados, regras de reservas, políticas de negócio e observabilidade.

## 1.2. Problema identificado

O gerenciamento de reservas de salas pode apresentar dificuldades quando não existe um mecanismo centralizado para organizar a disponibilidade dos ambientes.

Entre os principais problemas considerados estão:

- Conflitos causados por reservas em horários sobrepostos.
- Dificuldade para identificar a disponibilidade de uma sala.
- Ausência de regras padronizadas para autorizar reservas.
- Falta de organização dos registros de utilização.
- Dificuldade para acompanhar alterações e cancelamentos.

Esses problemas motivam a construção de uma aplicação capaz de centralizar os registros e aplicar regras de negócio consistentes.

## 1.3. Objetivo geral

Desenvolver uma API para gerenciamento de reservas de salas, permitindo organizar usuários, ambientes e solicitações de reserva, com validação de disponibilidade e aplicação de políticas de utilização.

Além das funcionalidades, o projeto busca demonstrar a aplicação prática de princípios SOLID, Clean Code, padrões GoF e decisões arquiteturais documentadas.

## 1.4. Objetivos específicos

O sistema deverá permitir:

1. Cadastrar e consultar usuários.
2. Cadastrar e consultar salas.
3. Registrar solicitações de reservas.
4. Consultar a disponibilidade de salas.
5. Identificar conflitos de horários.
6. Aplicar políticas de validação de reservas.
7. Controlar os estados das reservas.
8. Cancelar reservas conforme as regras definidas.
9. Registrar e publicar eventos relevantes.
10. Armazenar informações em banco de dados SQLite.
11. Disponibilizar operações por meio de uma API HTTP.
12. Realizar testes automatizados das regras implementadas.

Essas funcionalidades representam o escopo planejado e serão implementadas progressivamente.

## 1.5. Público-alvo e interessados

O sistema foi concebido para representar um cenário de organizações que compartilham salas, como instituições de ensino e ambientes corporativos.

Os principais interessados são:

**Usuários das salas:** pessoas que precisam consultar a disponibilidade e solicitar a utilização de ambientes.

**Responsáveis pela gestão dos ambientes:** pessoas interessadas em manter os registros organizados e evitar reservas conflitantes.

**Equipe de desenvolvimento:** responsável pela implementação, manutenção, testes e integração dos módulos.

**Professor avaliador:** responsável pela avaliação das decisões arquiteturais, padrões utilizados, qualidade do código e evidências técnicas apresentadas.

Os perfis acima descrevem os interessados no sistema e não representam, necessariamente, papéis de autorização já implementados na API.

## 1.6. Escopo funcional

O escopo principal está concentrado no gerenciamento de reservas de salas.

As funcionalidades serão organizadas em módulos relacionados a:

- Usuários e salas.
- Persistência e consulta de informações.
- Reservas e disponibilidade.
- Políticas de negócio.
- Estados das reservas.
- Eventos e observabilidade.

Nesta etapa, não está previsto o desenvolvimento obrigatório de uma interface gráfica. A interação poderá ocorrer pela documentação interativa disponibilizada pelo FastAPI.

Recursos adicionais, como autenticação, integração com serviços externos ou reservas de equipamentos, dependerão de definição e alinhamento posterior do grupo, não sendo considerados funcionalidades implementadas nesta versão.

## 1.7. Tecnologias adotadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal de desenvolvimento |
| FastAPI | Desenvolvimento da API HTTP |
| SQLite | Persistência de dados planejada |
| Pytest | Testes automatizados |
| Ruff | Análise estática e formatação |
| Git e GitHub | Versionamento e colaboração |
| GitHub Actions | Execução automatizada de verificações |
| Mermaid | Representação de diagramas arquiteturais |

A escolha dessas ferramentas busca atender ao escopo acadêmico sem introduzir complexidade operacional desnecessária.

## 1.8. Arquitetura proposta

O ReservaFácil adota como proposta uma arquitetura de **monolito modular organizado em camadas**, com separação entre:

- **API:** comunicação HTTP e entrada de requisições.
- **Application:** coordenação dos casos de uso.
- **Domain:** modelos, contratos e regras fundamentais.
- **Infrastructure:** persistência e integrações técnicas.

Essa separação busca reduzir o acoplamento e permitir que componentes sejam testados e desenvolvidos de forma independente.

As justificativas, alternativas consideradas e consequências dessa escolha estão registradas no [ADR-0001 — Arquitetura monolítica modular em camadas](../adrs/0001-estrutura-geral.md).

## 1.9. Restrições e premissas

O desenvolvimento considera as seguintes condições:

- O projeto possui finalidade acadêmica.
- A equipe é composta por cinco integrantes.
- A arquitetura deve ser justificável por meio de decisões documentadas.
- O código deverá demonstrar princípios SOLID e padrões GoF aplicados a problemas reais.
- As alterações devem ser versionadas e submetidas à revisão por Pull Requests.
- Os testes automatizados e as verificações de qualidade deverão acompanhar o desenvolvimento.
- A documentação deverá apresentar evidências verificáveis do código, utilizando links permanentes para commits e linhas do GitHub.
- Não há necessidade de implantação em infraestrutura distribuída para cumprir o objetivo inicial.

As condições descritas orientam o planejamento e poderão ser revistas mediante justificativa e registro das decisões correspondentes.

## 1.10. Atributos de qualidade prioritários

O projeto considera especialmente relevantes:

**Manutenibilidade:** facilitar a compreensão, modificação e evolução dos módulos.

**Confiabilidade:** contribuir para a aplicação consistente das regras de reservas e reduzir a ocorrência de operações inválidas.

**Testabilidade:** permitir a verificação isolada de modelos, políticas e serviços, além de testes de integração.

A seleção definitiva, a relação com a ISO/IEC 25010:2023, as métricas e os trade-offs serão detalhados na documentação específica de atributos de qualidade.

## 1.11. Situação atual do desenvolvimento

Na etapa inicial, foram preparados:

- A aplicação FastAPI com a rota `GET /health`.
- A estrutura de pacotes das camadas arquiteturais.
- Modelos de domínio para usuários, salas e solicitações de reserva.
- Contratos compartilhados utilizando `Protocol`.
- Estruturas para representar eventos de reservas.
- Testes automatizados iniciais.
- Configuração do Ruff e do GitHub Actions.
- O ADR-0001.
- Um diagrama C4 inicial de componentes.

**As funcionalidades completas de persistência, reservas, políticas e notificações ainda dependem dos módulos em desenvolvimento.**

Os trabalhos iniciais estão publicados nos seguintes Pull Requests:

- [PR #1 — Estrutura inicial](https://github.com/MatheusCarriero/reservafacil-arquitetura/pull/1).
- [PR #7 — Arquitetura e contratos](https://github.com/MatheusCarriero/reservafacil-arquitetura/pull/7).

Na atualização de 11/11/2026, ambos aguardavam revisão e integração.

### Evidências técnicas iniciais

- [Inicialização da API e endpoint de saúde](https://github.com/MatheusCarriero/reservafacil-arquitetura/blob/00b28b17241867cd405046c12030b39c28a8872a/app/main.py#L1-L12).
- [Modelos de domínio](https://github.com/MatheusCarriero/reservafacil-arquitetura/blob/00b28b17241867cd405046c12030b39c28a8872a/app/domain/modelos.py#L1-L30).
- [Contratos compartilhados](https://github.com/MatheusCarriero/reservafacil-arquitetura/blob/00b28b17241867cd405046c12030b39c28a8872a/app/domain/contratos.py#L1-L50).
- [Testes automatizados do domínio](https://github.com/MatheusCarriero/reservafacil-arquitetura/blob/00b28b17241867cd405046c12030b39c28a8872a/tests/test_domain.py#L1-L82).

## 1.12. Considerações finais

O ReservaFácil foi planejado para demonstrar como decisões arquiteturais influenciam a organização e a evolução de uma aplicação.

Mais do que desenvolver uma API funcional, o projeto busca apresentar uma estrutura de software fundamentada, com divisão clara de responsabilidades, documentação verificável e testes automatizados.

A implementação ocorrerá de maneira incremental, respeitando os contratos compartilhados e as responsabilidades dos integrantes.