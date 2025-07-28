from app.models import Producto, Base
from app.database import engine, SessionLocal

# Asegura que las tablas estén creadas
Base.metadata.create_all(bind=engine)

productos = [
    {"nombre": "Marraqueta", "precio": 250, "descripcion": "Pan tradicional chileno"},
    {"nombre": "Hallulla", "precio": 300, "descripcion": "Pan plano y redondo"},
    {"nombre": "Pan Amasado", "precio": 350, "descripcion": "Pan rústico hecho a mano"},
    {"nombre": "Integral", "precio": 400, "descripcion": "Pan con harina integral"},
    {"nombre": "Baguette", "precio": 500, "descripcion": "Pan francés crujiente"},
    {"nombre": "Croissant", "precio": 800, "descripcion": "Hojaldre con mantequilla"},
    {"nombre": "Ciabatta", "precio": 600, "descripcion": "Pan italiano aireado"}
]

db = SessionLocal()

for p in productos:
    nuevo = Producto(**p)
    db.add(nuevo)

db.commit()
db.close()

print("Productos insertados con éxito")
