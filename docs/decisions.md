# Decisões Técnicas (Architecture Decision Records)

Este documento registra as principais decisões de arquitetura e tecnologia do projeto, incluindo o contexto e o raciocínio por trás de cada escolha. Esse é um padrão chamado de **ADR (Architecture Decision Record)**, amplamente utilizado em times de engenharia de software.

---

## ADR-01: Frontend — Next.js (React)

**Status:** Aceita  
**Data:** Abril/2026

**Contexto:**  
O sistema precisa de uma interface web com interatividade dinâmica (filtros, navegação entre páginas de empreendimento), sem precisar recarregar a página completamente.

**Decisão:**  
Usar Next.js com App Router como framework de frontend.

**Justificativa:**
- É o framework React mais popular e com maior adoção no mercado.
- Permite renderização no servidor (SSR) e geração estática (SSG), o que é vantajoso para SEO de portais imobiliários.
- O ecossistema React força o aprendizado de componentização e gerenciamento de estado.

**Alternativas Descartadas:**
- Vue.js / Nuxt.js: ecossistema menor, menos relevante no mercado brasileiro atual.
- HTML/CSS puro: insuficiente para a interatividade e escala desejadas como plataforma.

---

## ADR-02: Backend — Python + FastAPI

**Status:** Aceita  
**Data:** Abril/2026

**Contexto:**  
O backend precisará servir dados relacionais (empreendimentos, cidades, unidades) em formato JSON para o frontend, e precisar ser fácil de documentar, testar e evoluir.

**Decisão:**  
Usar Python com FastAPI como framework de API REST.

**Justificativa:**
- FastAPI gera documentação interativa (Swagger/OpenAPI) de forma automática, o que resolve a questão de contrato entre frontend e backend ainda em desenvolvimento.
- O uso de Pydantic força a tipagem explícita de dados de entrada e saída, alinhando a implementação diretamente com os schemas definidos no `entities.md`.
- Python é extremamente legível e produtivo, ideal para um projeto de aprendizado incremental.

**Alternativas Descartadas:**
- Node.js + TypeScript: Compartilharia o mesmo ecossistema que o Next.js, porém adiciona complexidade de configuração (tsconfig, ESLint, etc). Pode ser uma boa segunda stack para estudo futuro.
- Django: Mais completo ("baterias inclusas"), porém mais "mágico" e opinionado, o que dificulta o entendimento do que cada camada faz individualmente.

---

## ADR-03: Banco de Dados — PostgreSQL

**Status:** Aceita  
**Data:** Abril/2026

**Contexto:**  
O domínio do projeto (imóveis, cidades, construtoras) é altamente relacional e estruturado. Os dados não têm variação dinâmica de schema.

**Decisão:**  
Usar PostgreSQL como banco de dados relacional principal.

**Justificativa:**
- Excelente suporte nativo a UUID, tipos personalizados (Enum) e campos JSON (extensível para o futuro).
- Suporte robusto a Foreign Keys, garantindo a integridade referencial exigida pelo nosso modelo de dados.
- É o banco de dados relacional open-source mais adotado em aplicações web modernas.

**Alternativas Descartadas:**
- SQLite: Simples e sem servidor, mas limita o aprendizado de configurações de banco reais (conexão, usuários, etc). Pode ser usado para testes unitários locais.
- MySQL: Comparável ao PostgreSQL, porém com menos recursos avançados de tipagem e extensibilidade.

---

## ADR-04: Estratégia de Repositório — Monorepo

**Status:** Aceita  
**Data:** Abril/2026

**Contexto:**  
O projeto possui dois componentes distintos: o frontend (Next.js) e o backend (Python/FastAPI). Precisamos decidir se são repositórios separados ou um único.

**Decisão:**  
Um único repositório (Monorepo) contendo as pastas `frontend/` e `backend/`.

**Justificativa:**
- Reduz a fricção de gerenciar múltiplos repositórios durante o aprendizado inicial.
- Facilita o uso de agentes de IA com contexto compartilhado no mesmo workspace.
- A documentação em `docs/` serve como contrato único e centralizado para ambas as partes.

**Alternativas Descartadas:**
- Polyrepo (repositórios separados): Vantajoso em times grandes, mas desnecessário para um projeto de estudo solo.
