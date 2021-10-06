import strawberry

from yazio_sdk import ProductSuggestion as ProductSuggestionModel


@strawberry.experimental.pydantic.type(
    model=ProductSuggestionModel,
    fields=["product_id", "amount", "serving", "serving_quantity"],
)
class ProductSuggestion:
    pass
