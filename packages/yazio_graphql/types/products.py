import strawberry

from yazio_sdk import (
    ProductSuggestion as ProductSuggestionModel,
    ProductSearchResult as ProductSearchResultModel,
    ProductFavorite as ProductFavoriteModel,
    CreateConsumedProductInput as CreateConsumedProductInputModel,
)


@strawberry.experimental.pydantic.type(
    model=ProductSuggestionModel,
    fields=["product_id", "amount", "serving", "serving_quantity"],
)
class ProductSuggestion:
    pass


@strawberry.experimental.pydantic.type(
    model=ProductSearchResultModel,
    fields=[
        "name",
        "product_id",
        "serving",
        "serving_quantity",
        "amount",
        "base_unit",
        "producer",
        "is_verified",
        "is_favorite",
        "is_frequently_consumed",
    ],
)
class ProductSearchResult:
    pass


@strawberry.experimental.pydantic.type(
    model=ProductFavoriteModel,
    fields=["id", "amount", "serving", "serving_quantity", "product_id"],
)
class ProductFavorite:
    pass


@strawberry.experimental.pydantic.input(
    model=CreateConsumedProductInputModel,
    fields=["product_id", "amount", "serving", "serving_quantity", "date", "daytime"],
)
class CreateConsumedProductInput:
    pass
