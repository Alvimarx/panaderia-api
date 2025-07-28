from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings  # <-- el Settings con sqlalchemy_uri
from dotenv import load_dotenv
load_dotenv()
engine = create_async_engine(
    settings.sqlalchemy_uri,
    pool_pre_ping=True,
    echo=False,           # True para ver las consultas
)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

# Dependencia FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
