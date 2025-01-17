from fastapi import FastAPI
from prisma import Prisma
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Connect Prisma
    await prisma.connect()
    yield
    # Shutdown: Disconnect Prisma
    await prisma.disconnect()
    
app = FastAPI(
    lifespan=lifespan,
    docs_url="/api/py/docs",
    openapi_url="/api/py/openapi.json",
    title="My Custom API",
    description="API for managing items with CRUD operations",
    version="1.0.0",
)

prisma = Prisma()