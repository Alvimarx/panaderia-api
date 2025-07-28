from typing import List
from pydantic import BaseModel, validator

class PedidoLineaIn(BaseModel):
    producto_id: int
    cantidad:   int

    @validator("cantidad")
    def cantidad_positiva(cls, v):
        assert v > 0, "La cantidad debe ser mayor a cero"
        return v

class PedidoCreate(BaseModel):
    cliente:   str
    productos: List[PedidoLineaIn]

class PedidoOut(BaseModel):
    id:    int
    total: float

    class Config:
        from_attributes = True  # Pydantic v2
