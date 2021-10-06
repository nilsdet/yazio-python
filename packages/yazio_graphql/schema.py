import datetime

import strawberry
from strawberry import Schema

from .enums import DayTime
from .info import Info
from .types import ProductSuggestion


@strawberry.type
class Query:
    @strawberry.field
    def product_suggestions(
        self, info: Info, date: datetime.date, daytime: DayTime
    ) -> list[ProductSuggestion]:
        return info.context.client.product_suggestions(date, daytime)


schema = Schema(query=Query)
