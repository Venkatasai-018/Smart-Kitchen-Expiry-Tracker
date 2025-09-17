from fastapi import FastAPI,status,HTTPException,APIRouter
from db.db import supabase
from schema.add_item import Add_Item

route=APIRouter()

@route.post("/add_item")
async def add_item(items:Add_Item,status_code=status.HTTP_200_OK):
    # print(items)
    print(items.dict)
    # response =supabase.table("SKET").insert(items.dict()).execute()
    # if len(response["data"])>0:
    #     raise HTTPException