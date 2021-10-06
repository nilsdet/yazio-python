from typing import Optional

from starlette.requests import Request
from starlette.responses import Response

from yazio_sdk import YazioClient


def get_access_token(header: Optional[str]) -> Optional[str]:
    if header:
        return header[len("Bearer ") :]
    return None


class YazioContext:
    request: Request
    response: Optional[Response] = None

    def __init__(self, request: Request, response: Optional[Response] = None):
        self.request = request
        self.response = response
        access_token = get_access_token(self.request.headers.get("Authorization"))
        self.client = YazioClient(access_token=access_token)
