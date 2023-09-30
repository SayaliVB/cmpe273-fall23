import strawberry

import typing
from fastapi import FastAPI,HTTPException
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Item():
    id:int
    name:str


items = [
    Item(id=4840, name="Avocados"),
    Item(id=7465, name="Cantaloupe"),
    Item(id=4846, name="Nectarines"),
    Item(id=7765, name="Apricot"),
    Item(id=7745, name="Oranges")
]


def get_items():
    return items

def fetchItemByID(self, itemid: int) -> Item:
    for item in items:
        if item.id == itemid:
            return item
    raise HTTPException(
        status_code = 404, detail=f"Item with id {itemid} does not exist!"
    )

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"
    items: typing.List[Item] = strawberry.field(resolver=get_items)
    #name: returntype = where to get data from/ what to return
    @strawberry.field
    def fetchItems(self) -> typing.List[Item]:
        return items
    fetchItem: Item = strawberry.field(resolver=fetchItemByID)
    

@strawberry.type
class Mutation:
    @strawberry.mutation
    def createItem(self, id: int, name: str) -> Item:
        for item in items:
            if item.id == id:
                return item
        newItem = Item(id = id, name = name)
        items.append(newItem)
        return newItem
    @strawberry.mutation
    def updateItem(self, id: int, name: str) -> str:
        for item in items:
            if item.id == id:
                item.name = name
                return f"Item Updated: ID->{item.id}, Name-> {item.name}"
        return f"Item with id {id} not found"
    @strawberry.mutation
    def deleteItem(self, id: int) -> str:
        for item in items:
            if item.id == id:
                items.remove(item)
                return "Item removed successfully"
        return f"Item with id {id} not found"

schema = strawberry.Schema(query=Query, mutation=Mutation)


graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")