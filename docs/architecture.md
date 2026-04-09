# Arquitetura

## Visão Geral
A arquitetura inicial aposta em uma estrutura simples (monolítica do ponto de vista de repositório), mas buscando a separação lógica de responsabilidades entre Frontend, APIs Backend e o Banco de Dados.

## Stack Tecnológica
Após a etapa de documentação e System Design (SDD), definimos as bases tecnológicas:
- **Frontend:** Next.js (Ecosistema React)
- **Backend:** Python (Sugerido o uso de FastAPI, aprofundaremos depois)
- **Banco de Dados:** PostgreSQL

## Componentes Principais

### Frontend Web (Client)
- Aplicação focada em UI construída com **Next.js**.
- Consome dados da API backend desenvolvida em Python.
- Renderiza as views principais da plataforma: Lista de Empreendimentos, Filtros e a tela de Detalhes do Empreendimento.

### Backend (REST API)
- Serve como camada de dados expondo nossos pacotes de informações sobre os empreendimentos através de JSON.
- **Mapeamento lógico de Rotas (Endpoints da V1):**
  - `GET /api/developments` (Retorna a lista agregada, permitindo filtros por `cityId`)
  - `GET /api/developments/:id` (Retorna todos detalhes, como dados de `Builder` e lista de `Units` do respectivo empreendimento)
  - `GET /api/cities` (Retorna a lista de cidades referenciadas para o filtro principal do frontend)

### Banco de Dados (RDBMS)
- O **PostgreSQL** será o gerenciador de banco de dados relacional oficial.
- Sua finalidade primária será garantir integridade estrutural, Foreign Keys e estabilidade nos agrupamentos de `City`, `Builder`, `Development` e `Unit`.

## Observações Gerais
- Usaremos uma abordagem de alinhar os projetos cliente e API na mesma pasta master (Monorepo) para suavizar a curva de aprendizado inicial e acelerar a ponte de comunicação.
- Mesmo os textos da interface web final sendo focados no público PT-BR, toda a estrutura de código será feita utilizando jargões técnicos em inglês.