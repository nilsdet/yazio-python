from strawberry.types import Info as BaseInfo

from .context import YazioContext

Info = BaseInfo[YazioContext, None]
