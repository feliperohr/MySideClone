# Backend - MySideClone

API desenvolvida em FastAPI (Python).

## Como Rodar Localmente

1. Abra o terminal na pasta `backend`:
   ```bash
   cd backend
   ```
2. Inicie o servidor via Poetry:
   ```bash
   python -m poetry run uvicorn app.main:app --reload
   ```

A API estará disponível em:
- **Base**: `http://127.0.0.1:8000/`
- **Documentação/Testes (Swagger)**: `http://127.0.0.1:8000/docs`
