from api.init import prisma
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Movie(BaseModel):
    name: str
    year: str
    class Config:
        orm_mode = True
class MovieResponse(Movie):
    id: int
    class Config:
        orm_mode = True

@router.get("/api/py/movie", response_model=List[MovieResponse], tags=["Movie"])
async def get_movies():
    movies = await prisma.movie.find_many()
    return movies

@router.post("/api/py/movie", response_model=MovieResponse, tags=["Movie"])
async def create_movie(movie: Movie):
    movies = await prisma.movie.create(data=movie.model_dump())
    # return movies

@router.post("/api/py/helloFastApi")
def post_hello_fast_api():
    return {"message": "Hello from FastAPI"}
