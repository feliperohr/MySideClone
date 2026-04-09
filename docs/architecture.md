# Arquitetura

## Visão Geral
A arquitetura inicial aposta em uma estrutura simples (monolítica do ponto de vista de repositório), buscando a separação lógica de responsabilidades entre Frontend, APIs Backend e o Banco de Dados.

---

## Stack Tecnológica

| Camada         | Tecnologia                     | Justificativa                                               |
|----------------|--------------------------------|-------------------------------------------------------------|
| Frontend       | Next.js (React)                | Líder de mercado, componentização, SSR nativo               |
| Backend        | Python + FastAPI               | Alta produtividade, tipagem com Pydantic, Swagger automático|
| ORM            | SQLAlchemy + Alembic           | Padrão de mercado Python para RDBMS e migrações             |
| Banco de Dados | PostgreSQL                     | Robusto, relacional, suporte completo a UUID e JSON         |

---

## Estrutura do Repositório (Monorepo)
```
MySideClone/
  README.md
  docs/            → Documentação do projeto
  frontend/        → Aplicação Next.js
    src/
      app/         → Rotas (App Router do Next.js)
      components/  → Componentes reutilizáveis
  backend/         → API Python com FastAPI
    app/
      api/         → Routers / Endpoints
      models/      → Modelos do banco (SQLAlchemy)
      schemas/     → Schemas de validação (Pydantic)
      db/          → Configuração do banco e sessão
```

---

## Componentes Principais

### Frontend Web (Client)
- Aplicação construída com **Next.js**, utilizando o **App Router**.
- Consome dados da API backend via chamadas HTTP (`fetch` ou `axios`).
- Renderiza as views principais: Lista de Empreendimentos, Filtros e Página de Detalhe.

### Backend (REST API)
- Exposição de dados via endpoints JSON usando **FastAPI**.
- A validação dos dados de entrada e saída é feita com **Pydantic** (schemas tipados).
- **Endpoints da V1:**

| Método | Rota                       | Descrição                                                           |
|--------|----------------------------|---------------------------------------------------------------------|
| `GET`  | `/api/developments`        | Lista empreendimentos. Suporta filtro por `city_id` via query param |
| `GET`  | `/api/developments/{id}`   | Detalhes do empreendimento, incluindo `Builder` e lista de `Units`  |
| `GET`  | `/api/cities`              | Lista de cidades disponíveis (usada no filtro do frontend)          |

### Banco de Dados (RDBMS)
- **PostgreSQL** como gerenciador de banco de dados relacional.
- **Alembic** para controle de migrações de schema (versionamento do banco).
- Integridade garantida por Foreign Keys entre `City`, `Builder`, `Development` e `Unit`.

---

## Observações Gerais
- Toda a nomenclatura interna (tabelas, endpoints, variáveis) será em inglês, mesmo sendo uma plataforma voltada ao público PT-BR.
- O ambiente local de desenvolvimento usará um banco PostgreSQL via Docker (ou instalação local).
- A decisão de escolher cada tecnologia está documentada em [decisions.md](decisions.md).