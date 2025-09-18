from fastapi import FastAPI,status,HTTPException,APIRouter
from db.db import supabase
from schema.add_item import Add_Item

route=APIRouter()

@route.post("/add_item")
async def add_item(items:Add_Item,status_code=status.HTTP_200_OK):
    # print(items)
    items=items.dict()
    items['Expiry_date']=str(items['Expiry_date'])
    items['Purchase_date']=str(items['Purchase_date'])

    print(items)
    response =supabase.table("SKET").insert(items).execute()
    if response.data and len(response.data) > 0:
        return {status_code:"success"}
    else:
        raise HTTPException