from fastapi import FastAPI
from prisma import Prisma

app = FastAPI(
    docs_url="/api/py/docs",
    openapi_url="/api/py/openapi.json",
    title="My Custom API",
    description="API for managing items with CRUD operations",
    version="1.0.0",
)

prisma = Prisma()