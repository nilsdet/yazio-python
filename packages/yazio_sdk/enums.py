__all__ = ["DayTime"]

from enum import Enum


class DayTime(Enum):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"
