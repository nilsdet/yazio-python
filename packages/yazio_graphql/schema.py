import datetime
from typing import Optional

import strawberry
from strawberry import Schema
from strawberry.arguments import UNSET

from .enums import DayTime
from .info import Info
from .types import (
    ProductSuggestion,
    ProductSearchResult,
    ProductFavorite,
    CreateConsumedProductInput,
)


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

    @strawberry.field
    def productFavorites(self, info: Info) -> list[ProductFavorite]:
        return info.context.client.products.favorites()


@strawberry.type
class Mutation:
    @strawberry.field
    def create_consumed_items(
        self, info: Info, products: Optional[list[CreateConsumedProductInput]] = UNSET
    ) -> bool:
        info.context.client.consumed_items.create(products)
        return True


schema = Schema(query=Query, mutation=Mutation)
