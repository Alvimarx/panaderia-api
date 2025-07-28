from pydantic import BaseModel
from typing import List, Optional

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    descripcion: Optional[str] = None

    model_config = {"from_attributes": True}

class ProductoPedido(BaseModel):
    producto_id: int
    cantidad: int

class PedidoCrear(BaseModel):
    cliente: str
    productos: List[ProductoPedido]

class PedidoDetalle(BaseModel):
    id: int
    cliente: str
    total: float

    class Config:
        orm_mode = True
