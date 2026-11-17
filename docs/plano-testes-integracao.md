# Plano de Testes de Integração — ReservaFácil

## 1. Objetivo

Este documento estabelece os cenários de testes de integração previstos para o ReservaFácil.

O objetivo é verificar se os módulos de usuários, salas, reservas, políticas, persistência e eventos funcionam corretamente quando conectados.

Os testes descritos são planejados e **ainda não foram implementados**.

Sua execução dependerá da integração das funcionalidades desenvolvidas pelos integrantes do grupo.

## 2. Escopo

Os testes deverão avaliar:

- Comunicação entre a API e os serviços de aplicação.
- Integração dos serviços com os repositórios SQLite.
- Persistência e recuperação das informações.
- Regras de criação e cancelamento de reservas.
- Verificação de conflitos de horários.
- Aplicação de políticas de negócio.
- Controle de estados das reservas.
- Publicação e tratamento de eventos.
- Tratamento de erros.

## 3. Estratégia de testes

Os testes de integração serão implementados utilizando Pytest, com um banco SQLite temporário e isolado para cada teste ou conjunto de testes.

Sempre que possível, serão utilizados os componentes reais da aplicação.

Simulações serão utilizadas apenas para isolar dependências externas ou funcionalidades que não façam parte do cenário avaliado.

Os testes não deverão depender de dados cadastrados manualmente ou da ordem de execução de outros testes.

## 4. Matriz de cenários

| ID | Cenário | Resultado esperado | Responsável pelo módulo |
|---|---|---|---|
| TI-01 | Cadastrar usuário válido | Usuário persistido e recuperável | Integrante 2 |
| TI-02 | Cadastrar sala válida | Sala persistida e recuperável | Integrante 2 |
| TI-03 | Criar reserva com usuário e sala existentes | Reserva registrada | Integrantes 2 e 3 |
| TI-04 | Tentar reservar uma sala inexistente | Operação rejeitada | Integrante 3 |
| TI-05 | Criar reservas com horários sobrepostos na mesma sala | Conflito detectado e segunda reserva rejeitada | Integrantes 2 e 3 |
| TI-06 | Criar reservas simultâneas para o mesmo horário | Não permitir duas reservas conflitantes persistidas | Integrantes 2 e 3 |
| TI-07 | Criar reservas válidas em salas diferentes | Ambas registradas | Integrante 3 |
| TI-08 | Solicitar reserva com horário inicial posterior ou igual ao final | Solicitação rejeitada | Integrante 3 |
| TI-09 | Cancelar uma reserva válida | Estado e persistência atualizados conforme a regra definida | Integrante 3 |
| TI-10 | Aplicar política que rejeita uma reserva | Reserva não persistida | Integrante 4 |
| TI-11 | Substituir a estratégia de validação | Serviço utiliza a política selecionada | Integrante 4 |
| TI-12 | Criar reserva e publicar evento | Observadores registrados recebem o evento esperado | Integrante 5 |
| TI-13 | Cancelar reserva e publicar evento | Observadores recebem o evento de cancelamento | Integrante 5 |
| TI-14 | Executar `GET /health` | API responde com o status esperado | Integrantes 1 e 5 |
| TI-15 | Consultar registros após reinicialização da conexão SQLite | Registros persistidos permanecem disponíveis | Integrante 2 |

## 5. Cenários críticos

### 5.1. Conflito entre reservas

**Objetivo:** garantir que uma sala não seja reservada duas vezes para períodos sobrepostos.

**Preparação:**
- Criar um usuário.
- Criar uma sala.
- Registrar uma reserva válida.

**Execução:**
- Tentar criar outra reserva para a mesma sala em horário sobreposto.

**Resultado esperado:**
- A segunda solicitação é rejeitada.
- Apenas a reserva original permanece registrada.

### 5.2. Concorrência na criação de reservas

**Objetivo:** verificar o comportamento quando duas solicitações tentam reservar a mesma sala simultaneamente.

**Preparação:**
- Criar uma sala disponível.
- Preparar duas solicitações com horários conflitantes.

**Execução:**
- Disparar as solicitações concorrentes.

**Resultado esperado:**
- Não existem duas reservas conflitantes persistidas após a execução.

**Observação:** o contrato `criar_se_disponivel` já está definido, mas a garantia de atomicidade ainda precisa ser implementada e validada.

### 5.3. Integração com políticas de reserva

**Objetivo:** verificar se as políticas de negócio são respeitadas pelo serviço de reservas.

**Execução:**
- Configurar uma política que rejeite determinada solicitação.
- Tentar registrar uma reserva que viole essa política.

**Resultado esperado:**
- A validação impede a criação da reserva.
- Nenhuma reserva inválida é persistida.

### 5.4. Integração com eventos

**Objetivo:** verificar a publicação de eventos quando uma reserva é criada.

**Execução:**
- Registrar um observador.
- Criar uma reserva válida.
- Verificar o evento recebido.

**Resultado esperado:**
- O evento corresponde à reserva efetivamente criada.
- Os identificadores e o tipo do evento estão corretos.

O momento de publicação e o tratamento de falhas dos observadores deverão ser definidos durante a integração.

## 6. Decisões pendentes antes da implementação

A equipe deverá confirmar:

1. Como serão representados e validados os fusos horários.
2. Se reservas consecutivas, sem sobreposição real, serão permitidas.
3. Quais transições de estado serão aceitas.
4. Como o cancelamento afetará a disponibilidade.
5. Quais códigos HTTP serão utilizados em cada erro.
6. Como serão tratadas transações e solicitações concorrentes no SQLite.
7. Se falhas nos observadores deverão afetar ou não a operação principal.

Essas decisões devem ser alinhadas aos integrantes responsáveis e documentadas quando necessário.

## 7. Critérios de conclusão

Os testes de integração serão considerados concluídos quando:

- Os cenários aplicáveis estiverem automatizados.
- Os testes executarem em um banco isolado.
- Não houver dependência da ordem de execução.
- Os casos críticos de conflito forem aprovados.
- O Pytest e o Ruff estiverem aprovados.
- O Pull Request correspondente tiver sido revisado e integrado.
- As evidências estiverem documentadas com links permanentes para o código.

## 8. Responsabilidades

O **Integrante 1** coordenará o planejamento e a execução dos testes de integração.

Os integrantes responsáveis pelos módulos deverão apoiar a preparação dos cenários e corrigir falhas encontradas em seus componentes.

O planejamento dos testes não substitui os testes unitários que cada integrante deverá implementar.

## 9. Situação atual

**Status: Planejado.**

A estrutura inicial e os contratos do domínio foram publicados no PR #7.

As implementações de SQLite, reservas, Strategy, State e Observer ainda dependem das entregas dos integrantes responsáveis.

Este documento será atualizado conforme essas implementações forem integradas.