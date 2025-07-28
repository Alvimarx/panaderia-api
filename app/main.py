from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
from app.api import pedidos   # 👈
from app.core.database import get_db


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(pedidos.router)  # 👈  añade /api/pedido

templates = Jinja2Templates(directory="templates")
# Ruta para la home
@app.get("/")
def home(request: Request):
    productos = [
        {"id": 1, "nombre": "Producto 1", "precio": 100},
        {"id": 2, "nombre": "Producto 2", "precio": 200},
        {"id": 3, "nombre": "Producto 3", "precio": 300}
    ]
    return templates.TemplateResponse("index.html", {"request": request, "productos": productos})

@app.get("/checkout")
def checkout(request: Request):
    return templates.TemplateResponse("checkout.html", {"request": request})

@app.post("/api/pedido")
def crear_pedido_api(pedido: schemas.PedidoCreate, db: AsyncSession = Depends(get_db)):
    try:
        nuevo_pedido = crud.crear_pedido(db, pedido)
        return {"id": nuevo_pedido.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")
