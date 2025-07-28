# app/database.py  ← copia y pega todo esto

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings   # ← tu Settings con sqlalchemy_uri
from dotenv import load_dotenv
load_dotenv()
# Motor async
engine = create_async_engine(
    settings.sqlalchemy_uri,  # decide TCP local o socket /cloudsql/...
    pool_pre_ping=True,
)

# Factory de sesiones
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_db():
    """Dependencia para FastAPI (yield session)."""
    async with AsyncSessionLocal() as session:
        yield session
