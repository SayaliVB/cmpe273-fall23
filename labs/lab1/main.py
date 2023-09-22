from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id:int
    name:str
    price:float

items = [
    Item(id=4840, name="Avocados", price=4.49),
    Item(id=7765, name="Cantaloupe", price=6.99),
    Item(id=4846, name="Nectarines", price=2.0),
    Item(id=7765, name="Apricot", price=3.45),
    Item(id=7765, name="Oranges", price=2.55)
]

@app.get("/")
def index():
    return "Hello World"


#the parameter name must be same in api path and function, i.e. 'item_id' in 'get("\item\{item_id}")' and 
#'item_id' in def get_by_id(item_id:int)
@app.get("/items/{item_id}")
def get_by_id(item_id:int) -> Item:
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(
        status_code = 404, detail=f"Item with id {item_id} does not exist!"
    )