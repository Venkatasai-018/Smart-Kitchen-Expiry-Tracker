from fastapi import *
from db.db import *
from datetime import *


route=APIRouter(
    prefix="/delete",
    tags=["DeleteItems"]
)

def daysdiff(d1):
    today=datetime.today().date()
    d1=datetime.strptime(d1, "%Y-%m-%d").date()
        
    return (d1 - today).days



@route.delete("/{id}")
def deleteItemId(id:int):
    response = supabase.table("SKET").delete().eq("id", id).execute()
    print(response)
    return response.data

@route.delete("/all_expired")
def deleteExpired():
    expiry_items=[]
    response=supabase.table("SKET").select("*").execute()
    response=response.data
    for i in response:
        if daysdiff(i["Expiry_date"])==0:
            expiry_items.append(int(i["id"]))
    res=supabase.table("SKET").delete().in_("id",expiry_items).execute()
    return res

    