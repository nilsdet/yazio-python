import strawberry

from yazio_sdk import Nutrient as NutrientEnum, NutrientEntry as NutrientEntryModel

Nutrient = strawberry.enum(NutrientEnum)


@strawberry.experimental.pydantic.type(
    model=NutrientEntryModel, fields=["value"],
)
class NutrientEntry:
    nutrient: Nutrient


@strawberry.experimental.pydantic.input(
    model=NutrientEntryModel, fields=["value"],
)
class NutrientEntryInput:
    nutrient: Nutrient
