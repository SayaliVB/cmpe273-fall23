import strawberry


from fastapi import FastAPI, Depends, Request, WebSocket, BackgroundTasks
from strawberry.types import Info
from strawberry.fastapi import GraphQLRouter



#how to execute this with parameter??
def custom_context_dependency(name: str) -> str:
    return name




async def get_context(custom_value = Depends(custom_context_dependency)):
    return {
        "custom_value":custom_value 
    }

@strawberry.type
class Query:
    @strawberry.field
    def example(self, info: Info) -> str:
        return f"Hello {info.context['custom_value']}"




schema = strawberry.Schema(Query)


graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")