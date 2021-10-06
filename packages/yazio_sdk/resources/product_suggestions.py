__all__ = ["ProductSuggestions"]
from datetime import date
from typing import Union

from .base import Resource
from ..enums import DayTime
from ..models import ProductSuggestion


class ProductSuggestions(Resource):
    def __call__(
        self, date: date, daytime: Union[DayTime, str]
    ) -> list[ProductSuggestion]:
        r = self.client.get(
            "/user/products/suggested",
            params={
                "date": date.strftime("%Y-%m-%d"),
                "daytime": daytime.value if isinstance(daytime, DayTime) else daytime,
            },
        )
        return [ProductSuggestion(**suggestion) for suggestion in r.json()]
