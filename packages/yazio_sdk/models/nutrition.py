from enum import Enum
from types import DynamicClassAttribute

from pydantic import BaseModel


class Nutrient(Enum):
    # macros
    CARBOHYDRATES = "nutrient.carb"
    FAT = "nutrient.fat"
    PROTEIN = "nutrient.protein"
    # energy
    CALORIES = "energy.energy"


class NutrientEntry(BaseModel):
    nutrient: Nutrient
    value: float


class NutrientMapping(BaseModel):
    internal: str
    yazio: Nutrient


NUTRIENT_MAPPINGS = (
    NutrientMapping(internal="carbohydrates", yazio="nutrient.carb"),
    NutrientMapping(internal="fat", yazio="nutrient.fat"),
    NutrientMapping(internal="protein", yazio="nutrient.protein"),
)


class Nutrients(BaseModel):
    # macros
    carbohydrates: float
    fat: float
    protein: float

    # energy
    calories: float

    __mapping__ = {
        "carbohydrates": Nutrient.CARBOHYDRATES
    }

    def yazio_value(self, ):

    @property
    def mapping(self):
        print(self.__annotations__)
        return {self.carbohydrates: Nutrient.CARBOHYDRATES}
