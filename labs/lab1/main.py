from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.openapi.utils import get_openapi

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

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom Open API",
        openapi_version  ="3.0.0",
        version  ="1.0.0",
        summary="Customising OpenAPI schema for version",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi