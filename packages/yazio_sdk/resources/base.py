from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import YazioClient


class Resource:
    def __init__(self, client: "YazioClient"):
        self.client = client
