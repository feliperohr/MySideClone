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
- [ERD — Relacionamentos entre Entidades](docs/erd.md)
- [Contrato da API](docs/api_contract.md)
- [Arquitetura de Software](docs/architecture.md)
- [Decisões Técnicas (ADR)](docs/decisions.md)

## Padrões de Desenvolvimento (Git)

Para mantermos o histórico do projeto organizado e seguirmos o padrão de uma SDD robusta, utilizamos a combinação de **Commits Atômicos** e **Conventional Commits**.

### 1. Commits Atômicos
Regra de ouro: não utilize `git add .` para subir o trabalho de um dia inteiro. Adicione os arquivos por contexto e crie commits focados. Isso salva o repositório se um *revert* for necessário.

```bash
# Errado: Tudo de uma vez
git add .
git commit -m "fiz o backend e o readme"

# Correto: Separação de Responsabilidades
git add app/main.py
git commit -m "feat(api): configuracao inicial do servidor web e rotas"

git add README.md
git commit -m "docs(backend): criacao do manual de dev local"
```

### 2. Padrão de Mensagem (Conventional Commits)
Sempre inicie a mensagem com um destes "tipos":

* `feat`: Nova funcionalidade (criação de um model, rota ou componente).
* `fix`: Correção de bug.
* `docs`: Inclusão de documentação, Readmes.
* `build`: Mudanças nas bibliotecas, Poetry, package.json.
* `refactor`: Melhoria de código que não adiciona funcionalidade nova.

Opcionalmente, especifique de qual serviço estamos falando `(backend)` ou `(frontend)`:
👉 `tipo(escopo): resumo direto indicando o que foi feito`
