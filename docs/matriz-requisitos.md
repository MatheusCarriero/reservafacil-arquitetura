# Matriz de Requisitos Acadêmicos — ReservaFácil

## 1. Objetivo

Este documento acompanha os requisitos da disciplina de Arquitetura de Software, relacionando cada exigência às atividades do ReservaFácil.

O objetivo é identificar o que já foi desenvolvido, o que ainda está pendente e quais evidências deverão ser apresentadas na entrega final.

## 2. Arquitetura e documentação

| Requisito | Responsável | Situação |
|---|---|---|
| Definição do estilo arquitetural | Integrante 1 | Publicado, em revisão |
| Justificativa e alternativas descartadas | Integrante 1 | Documentado no ADR-0001 |
| Diagrama C4 — Contexto | Integrante 5 | Pendente |
| Diagrama C4 — Contêineres | Integrante 5 | Pendente |
| Diagrama C4 — Componentes | Integrante 1 | Versão inicial criada |
| Diagrama de sequência | Integrante 3 | Pendente |
| Descrição dos três atributos de qualidade prioritários | Grupo | Pendente |
| Trade-offs arquiteturais | Grupo | Parcialmente documentados |
| Documentação de implantação | Grupo | Pendente |

## 3. Decisões arquiteturais

| Documento | Tema planejado | Responsável | Situação |
|---|---|---|---|
| ADR-0001 | Arquitetura monolítica modular | Integrante 1 | Publicado, em revisão |
| ADR-0002 | Persistência SQLite | Integrante 2 | Pendente |
| ADR-0003 | Regras e organização da aplicação | Integrante 3 | Pendente |
| ADR-0004 | Implantação e operação | Integrante 5, com apoio do grupo | Pendente |
| ADR-0005 | Políticas de reserva | Integrante 4 | Pendente |

Os temas e responsáveis dos ADRs pendentes poderão ser ajustados pelo grupo, mantendo o mínimo de cinco decisões justificadas.

Cada ADR deverá apresentar contexto, decisão, alternativas, consequências positivas e negativas, status e evidências relacionadas ao código.

## 4. Princípios SOLID

| Princípio | Evidência esperada | Situação |
|---|---|---|
| SRP — Responsabilidade Única | Separação coerente das responsabilidades entre classes e serviços | Pendente de comprovação |
| OCP — Aberto/Fechado | Inclusão de novas políticas sem modificar o serviço principal | Pendente |
| LSP — Substituição de Liskov | Implementações intercambiáveis respeitando seus contratos | Pendente |
| ISP — Segregação de Interfaces | Interfaces específicas para responsabilidades distintas | Contratos criados; uso pendente |
| DIP — Inversão de Dependências | Serviços dependendo de abstrações em vez de repositórios concretos | Contratos criados; uso pendente |

**Responsabilidade:** o Integrante 4 coordena as evidências SOLID, com participação dos integrantes responsáveis pelo código.

A existência de interfaces não comprova, isoladamente, a aplicação completa dos princípios.

## 5. Padrões GoF

| Padrão | Responsável | Situação |
|---|---|---|
| State | Integrante 3 | Pendente |
| Strategy | Integrante 4 | Pendente |
| Observer | Integrante 5 | Pendente |

Para cada padrão serão necessários:

- Problema real que motivou sua utilização.
- Código funcional.
- Testes automatizados.
- Diagrama de classes.
- Justificativa dos benefícios e custos.
- Evidências com links permanentes do GitHub.

## 6. Qualidade e testes

| Requisito | Responsável | Situação |
|---|---|---|
| Configuração Ruff | Integrante 1 | Publicada no PR #1 |
| Configuração Pytest | Integrante 1 | Publicada no PR #1 |
| GitHub Actions | Integrante 1 | Publicado no PR #1 |
| Testes iniciais de domínio | Integrante 1 | Publicados no PR #7 |
| Testes dos repositórios | Integrante 2 | Pendente |
| Testes de reservas e conflitos | Integrante 3 | Pendente |
| Testes das políticas | Integrante 4 | Pendente |
| Testes de eventos | Integrante 5 | Pendente |
| Testes de integração | Integrante 1, com apoio do grupo | Pendente |
| Evidências de Clean Code | Grupo | Pendente |
| Documentação ISO/IEC 25010:2023 | Grupo | Pendente |

## 7. Observabilidade

| Requisito | Responsável | Situação |
|---|---|---|
| Endpoint GET /health | Integrante 1 | Implementado na estrutura inicial |
| Logs estruturados | Integrante 5 | Pendente |
| Justificativa do padrão transversal | Integrante 5 | Pendente |
| Testes dos mecanismos de observabilidade | Integrante 5 | Pendente |

A existência do health check não significa que o conjunto completo de observabilidade esteja implementado.

## 8. GitHub e colaboração

| Requisito | Situação |
|---|---|
| Repositório compartilhado | Criado |
| GitHub Project | Criado |
| Issues distribuídas | Criadas |
| Branches por funcionalidade | Em utilização |
| Pull Requests | Em utilização |
| Aprovação por outro integrante | Pendente |
| Proteção efetiva da branch main | A verificar |
| Evidências da participação dos cinco integrantes | Em andamento |
| Estratégia de merge consistente | A confirmar na integração |
| Links permanentes para evidências | Iniciados no ADR-0001 |

## 9. Evidências publicadas

**Arquitetura e contratos:**

- [PR #7 — Arquitetura e contratos](https://github.com/MatheusCarriero/reservafacil-arquitetura/pull/7)
- [ADR-0001 — Arquitetura monolítica modular](../adrs/0001-estrutura-geral.md)
- [Modelos de domínio — commit 00b28b1](https://github.com/MatheusCarriero/reservafacil-arquitetura/blob/00b28b17241867cd405046c12030b39c28a8872a/app/domain/modelos.py)
- [Contratos compartilhados — commit 00b28b1](https://github.com/MatheusCarriero/reservafacil-arquitetura/blob/00b28b17241867cd405046c12030b39c28a8872a/app/domain/contratos.py)
- [Testes iniciais — commit 00b28b1](https://github.com/MatheusCarriero/reservafacil-arquitetura/blob/00b28b17241867cd405046c12030b39c28a8872a/tests/test_domain.py)

**Estrutura inicial:**

- [PR #1 — Estrutura inicial](https://github.com/MatheusCarriero/reservafacil-arquitetura/pull/1)

## 10. Critérios para marcar um requisito como concluído

Um requisito só deverá ser marcado como concluído quando:

1. A implementação necessária estiver pronta.
2. Os testes correspondentes estiverem aprovados.
3. A documentação estiver atualizada.
4. As evidências utilizarem links permanentes para as linhas relevantes.
5. O Pull Request tiver sido revisado e integrado à branch principal.

A matriz deverá ser atualizada conforme o desenvolvimento do projeto avançar.