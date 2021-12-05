from .base import Resource
from ..models import CreateConsumedProductInput, CreateConsumedSimpleProductInput


class ConsumedItems(Resource):
    # todo simple_products, recipe_portions
    def create(
        self,
        products: list[CreateConsumedProductInput] = None,
        simple_products: list[CreateConsumedSimpleProductInput] = None,
    ) -> None:
        self.client.request(
            "post",
            "/user/consumed-items",
            data={
                "simple_products": [],
                "recipe_portions": [
                    simple_product.json() for simple_product in simple_products or []
                ],
                "products": [product.json() for product in products or []],
            },
        )
