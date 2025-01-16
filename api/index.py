
from api.items import router as item_route
from api.movies import router as movie_route
from api.init import app
from api.init import prisma

# Start the Prisma connection
@app.on_event("startup")
async def startup():
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()
    
routes = [item_route, movie_route]
for route in routes:
    app.include_router(item_route)
    app.include_router(movie_route)