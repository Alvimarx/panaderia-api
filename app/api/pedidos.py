from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from decimal import Decimal

from app.schemas import PedidoCreate, PedidoOut
from app.models  import Producto, Pedido, PedidoProducto
from app.core.database import get_db


router = APIRouter(prefix="/api", tags=["pedidos"])

@router.post("/pedido", response_model=PedidoOut, status_code=status.HTTP_201_CREATED)
async def crear_pedido(datos: PedidoCreate, db: AsyncSession = Depends(get_db)):
    if not datos.productos:
        raise HTTPException(400, "El pedido no contiene productos")

    # Obtener precios de la BD
    ids = [p.producto_id for p in datos.productos]
    result = await db.execute(select(Producto).where(Producto.id.in_(ids)))
    productos_db = {p.id: p for p in result.scalars()}

    # Verificar que existan todos
    faltan = set(ids) - productos_db.keys()
    if faltan:
        raise HTTPException(404, f"Productos no encontrados: {faltan}")

    # Calcular total
    total = Decimal("0")
    lineas = []
    for linea_in in datos.productos:
        prod = productos_db[linea_in.producto_id]
        subtotal = prod.precio * linea_in.cantidad
        total += subtotal
        lineas.append(
            PedidoProducto(producto_id=prod.id, cantidad=linea_in.cantidad)
        )

    pedido = Pedido(cliente=datos.cliente, total=total, lineas=lineas)
    db.add(pedido)
    await db.commit()
    await db.refresh(pedido)      # para obtener el id

    return PedidoOut.from_orm(pedido)
