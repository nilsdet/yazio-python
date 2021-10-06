import datetime
from typing import Union

from .base import Resource
from ..enums import DayTime
from ..models import ProductSearchResult, ProductSuggestion


class Products(Resource):
    def search(
        self, date: datetime.date, daytime: Union[DayTime, str], query: str
    ) -> list[ProductSearchResult]:
        r = self.client.get(
            "/user/products/search",
            params={
                "date": date.strftime("%Y-%m-%d"),
                "daytime": daytime.value if isinstance(daytime, DayTime) else daytime,
                "query": query,
            },
        )
        return [ProductSearchResult(**result) for result in r.json()]

    def suggestions(
        self, date: datetime.date, daytime: Union[DayTime, str]
    ) -> list[ProductSuggestion]:
        r = self.client.get(
            "/user/products/suggested",
            params={
                "date": date.strftime("%Y-%m-%d"),
                "daytime": daytime.value if isinstance(daytime, DayTime) else daytime,
            },
        )
        return [ProductSuggestion(**suggestion) for suggestion in r.json()]
