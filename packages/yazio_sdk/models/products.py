import datetime
from typing import Optional

from pydantic import BaseModel


class ProductSuggestion(BaseModel):
    product_id: str
    amount: float
    serving: str  # todo maybe enum?
    serving_quantity: float


class ProductSearchResult(BaseModel):
    name: str
    product_id: str
    serving: str  # todo maybe enum?
    serving_quantity: float
    amount: float
    base_unit: str  # todo maybe enum?
    producer: Optional[str]
    is_verified: bool
    is_favorite: bool
    is_frequently_consumed: bool
    # nutrients # todo


class ProductFavorite(BaseModel):
    id: str
    amount: float
    serving: Optional[str]
    serving_quantity: Optional[float]
    product_id: str


class CreateConsumedProductInput(BaseModel):
    product_id: str
    amount: float
    serving: Optional[str] = None
    serving_quantity: Optional[float] = None
    date: datetime.datetime
    daytime: str
