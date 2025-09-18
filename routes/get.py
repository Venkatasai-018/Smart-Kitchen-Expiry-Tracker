from fastapi import *
from db.db import supabase
from datetime import *

route=APIRouter(
    prefix="/items",
    tags=["Get-Items"]
)

def daysdiff(d1):
    today=datetime.today().date()
    d1=datetime.strptime(d1, "%Y-%m-%d").date()
        
    return (d1 - today).days


@route.get('/all')
def all_items():
    response=supabase.table("SKET").select("*").execute()
    return response

@route.get("/status")
def status():
    response=supabase.table("SKET").select("*").execute()
    response=response.data
    
    print(response)
    for i in response:
        # print(i['Expiry_date'])
        i["Status"]=daysdiff(i["Expiry_date"])
        print(i)

    return response
@route.get("/expired")
def expired():
    expiry_items=[]
    response=supabase.table("SKET").select("*").execute()
    response=response.data
    for i in response:
        if daysdiff(i["Expiry_date"])==0:
            i['Status']=0
            expiry_items.append(i)
    return expiry_items

@route.get("/fresh")
def fresh():
    fresh_items=[]
    response=supabase.table("SKET").select("*").execute().data
    for i in response:
        if daysdiff(i["Expiry_date"])>3:
            i["Status"]=daysdiff(i["Expiry_date"])
            fresh_items.append(i)
    return fresh_items

@route.get("/expiring_soon")
def expiring_soon():
    es=[]
    response=supabase.table("SKET").select("*").execute().data
    for i in response:
        if daysdiff(i["Expiry_date"])!=0 and daysdiff(i["Expiry_date"])<=3:
            i["Status"]=daysdiff(i["Expiry_date"])
            es.append(i)
    return es