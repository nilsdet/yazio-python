from dataclasses import asdict
from typing import Optional

import strawberry
from strawberry.arguments import UNSET

from yazio_sdk import (
    CreateConsumedProductInput as CreateConsumedProductInputModel,
    CreateConsumedSimpleProductInput as CreateConsumedSimpleProductInputModel,
)
from ..info import Info
from ..types import CreateConsumedProductInput, CreateConsumedSimpleProductInput


@strawberry.field
def create_consumed_items(
    info: Info,
    products: Optional[list[CreateConsumedProductInput]] = UNSET,
    simple_products: Optional[list[CreateConsumedSimpleProductInput]] = UNSET,
) -> bool:
    info.context.client.consumed_items.create(
        products=[
            CreateConsumedProductInputModel(**asdict(product)) for product in products
        ],
        simple_products=[
            # todo utility for conversion? or just use dataclasses instead?
            CreateConsumedSimpleProductInputModel(**asdict(simple_product))
            for simple_product in simple_products
        ],
    )
    return True


mutations = (create_consumed_items,)
