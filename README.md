# MySideClone

Projeto de estudo inspirado na plataforma imobiliária [MySide](https://www.myside.com.br/).

## Objetivo
Construir uma versão simplificada de uma plataforma web para listagem de empreendimentos imobiliários, com foco em aprendizado de engenharia de software, arquitetura, modelagem de domínio e desenvolvimento assistido por IA.

## Stack Tecnológica
| Camada         | Tecnologia                  |
|----------------|-----------------------------|
| Frontend       | Next.js (React)             |
| Backend        | Python + FastAPI            |
| Banco de Dados | PostgreSQL                  |
| ORM            | SQLAlchemy + Alembic        |

## Estrutura do Repositório (Monorepo)
```
MySideClone/
  README.md
  docs/          → Documentação do projeto (SDD, ADR, Entidades)
  frontend/      → Aplicação Next.js
  backend/       → API Python com FastAPI
```

## Documentação
A documentação detalhada do projeto pode ser encontrada na pasta `docs/`:
- [Visão Geral](docs/vision.md)
- [Requisitos](docs/requirements.md)
- [Entidades do Domínio](docs/entities.md)
- [Arquitetura de Software](docs/architecture.md)
- [Decisões Técnicas (ADR)](docs/decisions.md)
