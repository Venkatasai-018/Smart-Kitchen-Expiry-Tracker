from fastapi import *
from db.db import supabase

route=APIRouter()


@route.get('/all_items')
def all_items():
    response=supabase.table("SKET").select("*").execute()
    return response
