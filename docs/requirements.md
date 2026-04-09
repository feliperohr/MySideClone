# Requisitos

## Requisitos Funcionais (FR)
- **FR01:** O sistema deve listar os empreendimentos cadastrados (`Development`).
- **FR02:** O usuário deve poder filtrar empreendimentos por cidade (`City`).
- **FR03:** O usuário deve poder acessar a página de detalhe de um empreendimento específico.
- **FR04:** O sistema deve exibir as unidades/plantas (`Unit`) relacionadas a um empreendimento na tela de detalhe.
- **FR05:** O sistema deve exibir informações básicas sobre a construtora (`Builder`) responsável pelo empreendimento.
- **FR06:** A página de detalhe deve conter um botão de "Call To Action" (CTA) para facilitar o contato com um corretor (ex: link do WhatsApp).

## Requisitos Não Funcionais (NFR)
- **NFR01:** A estrutura do projeto deve ser simples o suficiente para aprendizado e evolução incremental.
- **NFR02:** O sistema deve possuir uma separação lógica clara entre frontend (UI), backend (API REST) e camada de persistência de dados.
- **NFR03:** O projeto deve utilizar termos em inglês para nomenclaturas de código, variáveis, tipos e tabelas no banco de dados.

## Restrições Atuais
- O projeto será construído em etapas (incrementalmente).
- A primeira versão foca apenas no tipo de visualização "somente leitura" (read-only) para o usuário final.
- Os dados podem ser *mockados* ou inseridos via scripts (`seeders`) inicialmente (sem necessidade de painel administrativo na V1).
