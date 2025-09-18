from fastapi import *
from db.db import supabase
from datetime import *

route=APIRouter()

def daysdiff(d1):
    today=datetime.today().date()
    d1=datetime.strptime(d1, "%Y-%m-%d").date()
        
    return (d1 - today).days


@route.get('/all_items')
def all_items():
    response=supabase.table("SKET").select("*").execute()
    return response

@route.get("/status_all_items")
def status():
    response=supabase.table("SKET").select("*").execute()
    response=response.data
    
    print(response)
    for i in response:
        # print(i['Expiry_date'])
        i["Status"]=daysdiff(i["Expiry_date"])
        print(i)

    return response
