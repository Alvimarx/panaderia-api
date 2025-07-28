from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio = Column(Numeric(10, 2), nullable=False)
    descripcion = Column(Text)

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True)
    cliente = Column(String, nullable=False)
    total = Column(Numeric(10, 2), nullable=False)
    fecha = Column(DateTime, server_default=func.now())
    productos = relationship("PedidoProducto", back_populates="pedido")

class PedidoProducto(Base):
    __tablename__ = "pedido_productos"
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), primary_key=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), primary_key=True)
    cantidad = Column(Integer, nullable=False)

    pedido = relationship("Pedido", back_populates="productos")
    producto = relationship("Producto")
