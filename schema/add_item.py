from pydantic import BaseModel
from datetime import date


class Add_Item(BaseModel):
    Item_Name: str
    Purchase_date: date
    Expiry_date: date
