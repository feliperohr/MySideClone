# Entidades do Domínio

## City
Representa a cidade onde o empreendimento está localizado.

- `id` (UUID) - Chave Primária (Primary Key)
- `name` (String) - Nome da cidade
- `state` (String) - Estado (ex: "SP", "RJ")
- `slug` (String) - Identificador amigável para URLs

## Builder
Representa a empresa/construtora responsável pelo empreendimento.

- `id` (UUID) - Chave Primária (Primary Key)
- `name` (String) - Nome da construtora
- `description` (Text) - Descrição breve da empresa
- `websiteUrl` (String) - Site da construtora (opcional)

## Development
Representa um empreendimento imobiliário.

- `id` (UUID) - Chave Primária (Primary Key)
- `name` (String) - Nome do empreendimento
- `description` (Text) - Descrição detalhada
- `cityId` (UUID) - Chave Estrangeira (Foreign Key) para `City`
- `builderId` (UUID) - Chave Estrangeira (Foreign Key) para `Builder`
- `address` (String) - Endereço completo
- `neighborhood` (String) - Bairro
- `startingPrice` (Decimal) - Preço mínimo (a partir de)
- `coverImage` (String) - Caminho ou URL da imagem de capa
- `status` (Enum: DRAFT, UNDER_CONSTRUCTION, READY) - Ciclo de vida da obra

## Unit
Representa uma unidade disponível ou uma planta dentro de um empreendimento. 
*Nota: Para um MVP, as unidades geralmente funcionam como "Tipologias/Plantas" (Ex: Planta padrão de 2 quartos) e não unidades literais (Ex: Apt 101).*

- `id` (UUID) - Chave Primária (Primary Key)
- `developmentId` (UUID) - Chave Estrangeira (Foreign Key) para `Development`
- `name` (String) - Nome da planta (ex: "Apartamento Padrão")
- `price` (Decimal) - Preço sugerido
- `sizeArea` (Decimal) - Metragem quadrada
- `bedrooms` (Integer) - Quantidade de quartos
- `bathrooms` (Integer) - Quantidade de banheiros
- `parkingSpaces` (Integer) - Vagas de garagem
- `isAvailable` (Boolean) - Situação de disponibilidade
