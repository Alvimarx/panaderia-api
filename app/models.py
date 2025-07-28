from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Producto(Base):
    __tablename__ = "productos"
    id          = Column(Integer, primary_key=True, index=True)
    nombre      = Column(String, nullable=False)
    precio      = Column(Numeric(10, 2), nullable=False)
    descripcion = Column(String)

class Pedido(Base):
    __tablename__ = "pedidos"
    id      = Column(Integer, primary_key=True, index=True)
    cliente = Column(String, nullable=False)
    total   = Column(Numeric(10, 2), nullable=False)
    fecha   = Column(DateTime(timezone=True), server_default=func.now())

    lineas  = relationship("PedidoProducto", back_populates="pedido")

class PedidoProducto(Base):
    __tablename__ = "pedido_productos"
    id           = Column(Integer, primary_key=True)
    pedido_id    = Column(Integer, ForeignKey("pedidos.id", ondelete="CASCADE"))
    producto_id  = Column(Integer, ForeignKey("productos.id"))
    cantidad     = Column(Integer, nullable=False)

    pedido   = relationship("Pedido", back_populates="lineas")
    producto = relationship("Producto")
