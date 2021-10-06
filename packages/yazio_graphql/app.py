from typing import Union, Optional

from starlette.requests import Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from strawberry.asgi import GraphQL

from .context import YazioContext


class YazioGraphQL(GraphQL):
    async def get_context(
        self, request: Union[Request, WebSocket], response: Optional[Response] = None
    ) -> YazioContext:
        return YazioContext(request=request, response=response)
