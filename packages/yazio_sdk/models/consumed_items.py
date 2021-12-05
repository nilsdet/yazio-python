import datetime

from pydantic import BaseModel

from .nutrition import NutrientEntry
from ..enums import DayTime


class CreateConsumedSimpleProductInput(BaseModel):
    id: str
    nutrients: list[NutrientEntry]
    daytime: DayTime
    name: str
    date: datetime.datetime
