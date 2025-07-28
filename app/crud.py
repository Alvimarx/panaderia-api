from sqlalchemy.orm import Session
from app import models, schemas

def listar_productos(db: Session):
    return db.query(models.Producto).all()

def crear_pedido(db: Session, pedido: schemas.PedidoCreate):
    total = 0
    for item in pedido.productos:
        producto = db.query(models.Producto).get(item.producto_id)
        if not producto:
            raise ValueError(f"Producto {item.producto_id} no existe")
        total += float(producto.precio) * item.cantidad

    nuevo_pedido = models.Pedido(cliente=pedido.cliente, total=total)
    db.add(nuevo_pedido)
    db.flush()  # importante para obtener el id

    for item in pedido.productos:
        db.add(models.PedidoProducto(
            pedido_id=nuevo_pedido.id,
            producto_id=item.producto_id,
            cantidad=item.cantidad
        ))

    db.commit()
    return nuevo_pedido
