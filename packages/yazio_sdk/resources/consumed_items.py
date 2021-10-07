from .base import Resource
from ..models import CreateConsumedProductInput


class ConsumedItems(Resource):
    # todo simple_products, recipe_portions
    def create(self, products: list[CreateConsumedProductInput] = None) -> None:
        self.client.request(
            "post",
            "/user/consumed-items",
            data={
                "simple_products": [],
                "recipe_portions": [],
                "products": [product.json() for product in products or []],
            },
        )
