from fastapi import *
from db.db import *


route=APIRouter(
    prefix="/update",
    tags=["UpdateItems"]
)

# @route.update("/{id}")
# def updateitem():

