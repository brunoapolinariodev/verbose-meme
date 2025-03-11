from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Verbose Meme API",
    description="Uma API simples para demonstração do FastAPI",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens, ajuste conforme necessário
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", summary="Rota raiz", description="Retorna uma mensagem de boas-vindas")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}", summary="Obter item", description="Retorna um item pelo ID")
async def read_item(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Item ID deve ser positivo")
    return {"item_id": item_id, "name": f"Item {item_id}"}