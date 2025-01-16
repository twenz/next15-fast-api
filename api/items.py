
from fastapi import HTTPException, status, APIRouter
from pydantic import BaseModel
from typing import List
from api.init import prisma


router = APIRouter()

class Item(BaseModel):
    name: str
    description: str
    class Config:
        orm_mode = True

class ItemResponse(Item):
    id: int
    class Config:
        orm_mode = True
    
@router.get("/api/py/items", response_model=List[ItemResponse], tags=["Items"], status_code=status.HTTP_200_OK)
async def get_items():
    items = await prisma.item.find_many()
    return items

@router.get("/api/py/items/{item_id}", response_model=ItemResponse, tags=["Items"])
async def get_item(item_id: int):
    item = await prisma.item.find_unique(where={"id": item_id})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/api/py/items", response_model=ItemResponse, tags=["Items"], status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    created_item = await prisma.item.create(data=item.model_dump())
    return created_item

@router.put("/api/py/items/{item_id}", response_model=ItemResponse, tags=["Items"])
async def update_item(item_id: int, item: Item):
    updated_item = await prisma.item.update(where={"id": item_id}, data=item.model_dump())
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/api/py/items/{item_id}", tags=["Items"])
async def delete_item(item_id: int):
    deleted_item = await prisma.item.delete(where={"id": item_id})
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
