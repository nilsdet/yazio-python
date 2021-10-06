__all__ = ["YazioClient"]

import requests

from .resources import *


class YazioClient:
    USER_AGENT = "YAZIO/7.4.0 (com.yazio.ios.YAZIO; build:1153; iOS 14.7.1) Alamofire/5.4.3"  # noqa: E501

    def __init__(self, access_token: str):
        self.access_token = access_token
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.access_token}",
                "User-Agent": self.USER_AGENT,
            }
        )
        # Resources
        self.products = Products(self)

    def get(self, path: str, *args, **kwargs):
        return self.session.get("https://yzapi.yazio.com/v10" + path, *args, **kwargs)
