from starlette.applications import Starlette

from .app import YazioGraphQL
from .schema import schema

api = Starlette()

app = YazioGraphQL(schema)

api.add_route("/graphql", app)
api.add_websocket_route("/graphql", app)
