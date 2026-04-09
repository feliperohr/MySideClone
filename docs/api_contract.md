# Contrato da API (API Contract)

> **O que é um API Contract?**
> É o documento que define *exatamente* o que cada endpoint da API recebe e retorna, antes de qualquer linha de código ser escrita. Ele funciona como um contrato legal entre o time de backend e o time de frontend: ambos podem trabalhar em paralelo porque concordam com o formato dos dados de antemão.
> Em projetos que usam FastAPI, este contrato se traduz diretamente nos **Pydantic Schemas** (os objetos tipados de entrada e saída da API).

---

## Convenções deste documento

- Os tipos aqui seguem a notação da API (JSON/HTTP), não necessariamente do banco de dados.
- Campos marcados com `?` são opcionais (podem ser `null`).
- Todos os endpoints retornam `Content-Type: application/json`.
- Erros seguem o formato padrão `{ "detail": "mensagem de erro" }`.

---

## Endpoints da V1

---

### `GET /api/cities`

**Propósito:** Retornar a lista de cidades disponíveis para popular o filtro na tela de listagem.

> **Conceito-chave:** Este endpoint retorna dados "simples" sem relacionamentos aninhados — um array plano de objetos. É o endpoint mais simples e geralmente o primeiro a ser implementado no backend.

**Request:**
```
GET /api/cities
```
Sem body, sem parâmetros obrigatórios.

**Response — `200 OK`:**
```json
[
  {
    "id": "uuid-string",
    "name": "São Paulo",
    "state": "SP",
    "slug": "sao-paulo"
  },
  {
    "id": "uuid-string",
    "name": "Rio de Janeiro",
    "state": "RJ",
    "slug": "rio-de-janeiro"
  }
]
```

---

### `GET /api/developments`

**Propósito:** Retornar a lista de empreendimentos para a tela principal de listagem (cards). Suporta filtragem por cidade via query parameter opcional.

> **Conceito-chave — Query Parameters vs Path Parameters:**
> - `GET /api/developments?city_id=uuid` → O `city_id` é um **query parameter** (filtro opcional, vai após o `?`). Usado para *filtrar* uma coleção.
> - `GET /api/developments/uuid` → O `uuid` é um **path parameter** (identificador, faz parte da rota). Usado para *identificar* um recurso específico.

> **Conceito-chave — Resposta Agregada (Partial Object):**
> Repare que este endpoint retorna apenas os campos necessários para o *card* do empreendimento na listagem (nome, cidade, preço), **não** todos os detalhes completos, como a lista de unidades. Retornar menos dados aqui é uma decisão de performance e design: não carregue o que você não vai usar.

**Request:**
```
GET /api/developments
GET /api/developments?city_id={uuid}   ← filtro opcional por cidade
```

**Response — `200 OK`:**
```json
[
  {
    "id": "uuid-string",
    "name": "Nome do Empreendimento",
    "neighborhood": "Bairro",
    "startingPrice": 450000.00,
    "coverImage": "/images/cover.jpg",
    "status": "READY",
    "city": {
      "name": "São Paulo",
      "state": "SP"
    }
  }
]
```

> **Atenção ao campo `city`:** Mesmo que no banco o `Development` só armazene `cityId`, a API já retorna o objeto `city` aninhado com `name` e `state`. Isso é responsabilidade do backend: fazer o JOIN e montar o objeto de resposta para poupar o frontend de fazer chamadas extras.

---

### `GET /api/developments/{id}`

**Propósito:** Retornar os dados completos de um único empreendimento para a página de detalhe.

> **Conceito-chave — Objeto Completo (Full/Nested Object):**
> Diferente do endpoint de listagem, aqui retornamos **tudo**: os dados do empreendimento, os dados da construtora aninhados (`builder`) e a lista completa de unidades (`units`). Essa estratégia de "carregar tudo em uma chamada" é chamada de **eager loading** e é ideal quando o usuário está em uma página dedicada para aquele recurso.

> **Conceito-chave — Contrato de Erro:**
> Quando o `id` não corresponde a nenhum empreendimento, retornamos `404 Not Found`. Documentar os erros é tão importante quanto documentar o sucesso — o frontend precisa saber o que fazer quando algo der errado.

**Request:**
```
GET /api/developments/{id}
```

**Response — `200 OK`:**
```json
{
  "id": "uuid-string",
  "name": "Nome do Empreendimento",
  "description": "Descrição completa e detalhada do empreendimento...",
  "address": "Rua Exemplo, 123",
  "neighborhood": "Bairro",
  "startingPrice": 450000.00,
  "coverImage": "/images/cover.jpg",
  "status": "READY",
  "latitude": -23.5505,
  "longitude": -46.6333,
  "city": {
    "id": "uuid-string",
    "name": "São Paulo",
    "state": "SP"
  },
  "builder": {
    "id": "uuid-string",
    "name": "Nome da Construtora",
    "description": "Descrição breve da construtora.",
    "logoImage": "/images/builder-logo.png",
    "websiteUrl": "https://construtora.com.br"
  },
  "units": [
    {
      "id": "uuid-string",
      "name": "Planta Padrão",
      "price": 480000.00,
      "sizeArea": 65.5,
      "bedrooms": 2,
      "bathrooms": 1,
      "parkingSpaces": 1,
      "isAvailable": true
    },
    {
      "id": "uuid-string",
      "name": "Planta Premium",
      "price": 620000.00,
      "sizeArea": 88.0,
      "bedrooms": 3,
      "bathrooms": 2,
      "parkingSpaces": 2,
      "isAvailable": false
    }
  ]
}
```

**Response — `404 Not Found`:**
```json
{
  "detail": "Development not found."
}
```

---

## Como este contrato vira código (Preview)

> Este bloco é um *preview* de como o contrato se mapeia para Pydantic no FastAPI. Não é código final — é para você visualizar a relação entre documento e implementação.

```python
# Exemplo de como o schema Pydantic reflete este contrato
from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal

class CityResponse(BaseModel):
    id: UUID
    name: str
    state: str
    slug: str

class UnitResponse(BaseModel):
    id: UUID
    name: str
    price: Decimal
    sizeArea: Decimal
    bedrooms: int
    bathrooms: int
    parkingSpaces: int
    isAvailable: bool

class DevelopmentDetailResponse(BaseModel):
    id: UUID
    name: str
    description: str
    startingPrice: Decimal
    status: str
    city: CityResponse      # <- objeto aninhado
    units: list[UnitResponse] # <- lista de objetos aninhados
```

> **Perceba:** O schema Python é uma tradução quase direta do JSON documentado aqui. É por isso que definir o contrato antes do código economiza retrabalho.

---

## Referências entre arquivos
- **Entidades e tipos de dados:** [entities.md](entities.md)
- **Relacionamentos entre entidades:** [erd.md](erd.md)
- **Visão geral da arquitetura:** [architecture.md](architecture.md)
