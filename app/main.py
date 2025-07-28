from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, database

app = FastAPI()

@app.get("/productos", response_model=list[schemas.Producto])
def listar_productos(db: Session = Depends(database.get_db)):
    return crud.listar_productos(db)

@app.post("/pedido", response_model=schemas.PedidoDetalle, status_code=201)
def crear_pedido(pedido: schemas.PedidoCrear, db: Session = Depends(database.get_db)):
    try:
        return crud.crear_pedido(db, pedido)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
