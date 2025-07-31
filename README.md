# Panaderia API

Este proyecto contiene una pequeña aplicación web desarrollada con **FastAPI** que simula una panadería en línea. Incluye un API para crear pedidos y una interfaz de ejemplo hecha con HTML y JavaScript que permite agregar productos a un carrito.

## Estructura del proyecto

```
├── Dockerfile            # Imagen de Docker para ejecutar la aplicación
├── app/                  # Código de la aplicación FastAPI
│   ├── api/              # Rutas de la API (p.ej. /api/pedido)
│   ├── core/             # Configuración y conexión a la base de datos
│   ├── models.py         # Modelos de SQLAlchemy
│   ├── schemas.py        # Esquemas Pydantic
│   └── main.py           # Punto de entrada de la aplicación
├── templates/            # Plantillas HTML (Jinja2)
├── static/               # Archivos estáticos (JS y CSS)
├── requirements.txt      # Dependencias de Python
└── cargar_productos.py   # Script para poblar la base de datos con productos
```

## Configuración

Se utilizan variables de entorno para la conexión a la base de datos. Puedes definirlas en un archivo `.env` en la raíz del proyecto:

```
DB_USER=usuario
DB_PASS=contraseña
DB_NAME=panaderia
DB_HOST=localhost
DB_PORT=5432
# Si utilizas Cloud SQL en GCP puedes definir INSTANCE_CONNECTION_NAME
# INSTANCE_CONNECTION_NAME=proyecto:región:instancia
```

El archivo `app/core/config.py` construye la URI de SQLAlchemy a partir de estas variables.

## Ejecución con entorno virtual

1. Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```
3. (Opcional) Ejecuta `cargar_productos.py` para insertar algunos productos de ejemplo en la base de datos.

   ```bash
   python cargar_productos.py
   ```
4. Inicia el servidor:

   ```bash
   uvicorn app.main:app --reload
   ```
5. Abre `http://localhost:8000` en tu navegador para ver la tienda y `http://localhost:8000/docs` para la documentación interactiva generada por FastAPI.

## Ejecución con Docker

También puedes construir y ejecutar la aplicación en un contenedor:

```bash
docker build -t panaderia .
docker run -p 8080:8080 --env-file .env panaderia
```

El puerto por defecto en el contenedor es `8080` pero puedes cambiarlo con la variable `PORT`.

## Endpoints principales

- **GET /**         - Página de inicio con la lista de productos.
- **GET /checkout** - Vista del carrito y formulario para confirmar el pedido.
- **POST /api/pedido** - Crea un pedido. Recibe un objeto `PedidoCreate` con el nombre del cliente y la lista de productos.

## Scripts adicionales

- `cargar_productos.py`: inserta algunos productos de ejemplo en la base de datos.
- `app/test.py`: script de prueba para verificar la conexión con una instancia de Cloud SQL.

## Requisitos

- Python 3.10 o superior.
- PostgreSQL (local o una instancia en la nube).

## Licencia

Este proyecto se proporciona con fines educativos y no cuenta con una licencia específica.

