import strawberry

from yazio_sdk import (
    CreateConsumedSimpleProductInput as CreateConsumedSimpleProductInputModel,
)
from .nutrition import NutrientEntryInput
from ..enums import DayTime


@strawberry.experimental.pydantic.input(
    model=CreateConsumedSimpleProductInputModel,
    fields=["id", "name", "date"],
)
class CreateConsumedSimpleProductInput:
    daytime: DayTime
    # todo your should probably make the nutrient entries a type instead of using lists
    nutrients: list[NutrientEntryInput]
