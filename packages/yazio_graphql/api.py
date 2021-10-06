from fastapi import FastAPI

from .app import YazioGraphQL
from .schema import schema

api = FastAPI()

app = YazioGraphQL(schema)

api.add_route("/graphql", app)
api.add_websocket_route("/graphql", app)
