__all__ = ["DayTime"]
import strawberry

from yazio_sdk import DayTime as BaseDayTime

DayTime = strawberry.enum(BaseDayTime)
