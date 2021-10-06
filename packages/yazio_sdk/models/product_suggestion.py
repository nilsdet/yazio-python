__all__ = ["ProductSuggestion"]
from pydantic import BaseModel


class ProductSuggestion(BaseModel):
    product_id: str  # todo maybe uuid?
    amount: float
    serving: str  # todo maybe enum?
    serving_quantity: float
