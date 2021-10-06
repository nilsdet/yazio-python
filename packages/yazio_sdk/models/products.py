from typing import Optional

from pydantic import BaseModel


class ProductSuggestion(BaseModel):
    product_id: str  # todo maybe uuid?
    amount: float
    serving: str  # todo maybe enum?
    serving_quantity: float


class ProductSearchResult(BaseModel):
    name: str
    product_id: str  # todo maybe uuid?
    serving: str  # todo maybe enum?
    serving_quantity: float
    amount: float
    base_unit: str  # todo maybe enum?
    producer: Optional[str]
    is_verified: bool
    is_favorite: bool
    is_frequently_consumed: bool
    # nutrients # todo
