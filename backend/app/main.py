from fastapi import FastAPI

app = FastAPI(
    title="MySideClone API",
    description="API RESTful baseada em SDD para o MySideClone.",
    version="0.1.0",
)

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Motor do backend inicializado com sucesso!",
        "docs": "Acesse /docs para o Swagger interativo"
    }
@app.get("/teste")
def teste():
    return {
        "status": "offline",
        "message": "TESSTE"
    }