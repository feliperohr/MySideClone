# Entidades do Domínio

> Todos os campos de auditoria (`createdAt`, `updatedAt`) são padrão em todas as entidades e serão gerenciados automaticamente pelo ORM (SQLAlchemy). Não serão repetidos individualmente abaixo para manter a legibilidade.

---

## City
Representa a cidade onde o empreendimento está localizado.

| Campo       | Tipo    | Descrição                              |
|-------------|---------|----------------------------------------|
| `id`        | UUID    | Chave Primária (Primary Key)           |
| `name`      | String  | Nome da cidade                         |
| `state`     | String  | Sigla do estado (ex: "SP", "RJ")       |
| `slug`      | String  | Identificador amigável para URLs       |
| `createdAt` | DateTime| Data de criação do registro            |
| `updatedAt` | DateTime| Data da última atualização do registro |

---

## Builder
Representa a empresa/construtora responsável pelo empreendimento.

| Campo         | Tipo    | Descrição                              |
|---------------|---------|----------------------------------------|
| `id`          | UUID    | Chave Primária (Primary Key)           |
| `name`        | String  | Nome da construtora                    |
| `description` | Text    | Descrição breve da empresa             |
| `logoImage`   | String  | Caminho ou URL do logotipo da empresa  |
| `websiteUrl`  | String  | Site oficial (opcional)                |
| `createdAt`   | DateTime| Data de criação do registro            |
| `updatedAt`   | DateTime| Data da última atualização do registro |

---

## Development
Representa um empreendimento imobiliário.

| Campo            | Tipo                                    | Descrição                                    |
|------------------|-----------------------------------------|----------------------------------------------|
| `id`             | UUID                                    | Chave Primária (Primary Key)                 |
| `name`           | String                                  | Nome do empreendimento                       |
| `description`    | Text                                    | Descrição detalhada                          |
| `cityId`         | UUID                                    | FK → `City`                                  |
| `builderId`      | UUID                                    | FK → `Builder`                               |
| `address`        | String                                  | Endereço completo                            |
| `neighborhood`   | String                                  | Bairro                                       |
| `startingPrice`  | Decimal                                 | Preço mínimo (a partir de)                   |
| `coverImage`     | String                                  | Caminho ou URL da imagem de capa             |
| `status`         | Enum: `DRAFT`, `UNDER_CONSTRUCTION`, `READY` | Ciclo de vida da obra                   |
| `latitude`       | Decimal (nullable)                      | Coordenada geográfica — latitude (opcional)  |
| `longitude`      | Decimal (nullable)                      | Coordenada geográfica — longitude (opcional) |
| `createdAt`      | DateTime                                | Data de criação do registro                  |
| `updatedAt`      | DateTime                                | Data da última atualização do registro       |

---

## Unit
Representa uma tipologia/planta disponível dentro de um empreendimento.

> **Nota:** No MVP, as unidades funcionam como "Tipologias" (ex: Planta de 2 quartos, 50m²) e não como unidades físicas literais (ex: Apt 101). Isso reflete como portais imobiliários reais expõem os dados ao usuário final.

| Campo            | Tipo    | Descrição                              |
|------------------|---------|----------------------------------------|
| `id`             | UUID    | Chave Primária (Primary Key)           |
| `developmentId`  | UUID    | FK → `Development`                     |
| `name`           | String  | Nome da tipologia (ex: "Planta Padrão")|
| `price`          | Decimal | Preço sugerido                         |
| `sizeArea`       | Decimal | Metragem quadrada (m²)                 |
| `bedrooms`       | Integer | Quantidade de quartos                  |
| `bathrooms`      | Integer | Quantidade de banheiros                |
| `parkingSpaces`  | Integer | Vagas de garagem                       |
| `isAvailable`    | Boolean | Situação de disponibilidade            |
| `createdAt`      | DateTime| Data de criação do registro            |
| `updatedAt`      | DateTime| Data da última atualização do registro |
