import datetime

import strawberry
from strawberry import Schema

from .enums import DayTime
from .info import Info
from .types import ProductSuggestion, ProductSearchResult


@strawberry.type
class Query:
    @strawberry.field
    def suggest_products(
        self, info: Info, date: datetime.date, daytime: DayTime
    ) -> list[ProductSuggestion]:
        return info.context.client.products.suggestions(date, daytime)

    @strawberry.field
    def search_products(
        self, info: Info, date: datetime.date, daytime: DayTime, query: str
    ) -> list[ProductSearchResult]:
        return info.context.client.products.search(date, daytime, query)


schema = Schema(query=Query)
