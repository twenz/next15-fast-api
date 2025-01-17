
from api.init import app
from api.items import router as item_route
from api.movies import router as movie_route
    
routes = [item_route, movie_route]
for route in routes:
    app.include_router(item_route)
    app.include_router(movie_route)