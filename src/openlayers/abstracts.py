from __future__ import annotations

from abc import ABC, abstractmethod
from pydantic import BaseModel


class LayerLike(ABC):
    @abstractmethod
    def model_dump(self): ...


class MyBaseModel(BaseModel):
    def to_dict(self) -> dict:
        return self.model_dump()

    def model_dump(self) -> dict:
        return super().model_dump(exclude_none=True, by_alias=True)


# TODO: check if this class is still needed
"""
class BaseType(BaseModel):
    model_config = ConfigDict(extra="allow")

    def model_dump(self) -> dict:
        return dict(
            type=self.type, options=super().model_dump(exclude_none=True, by_alias=True)
        )

    @property
    def type(self) -> str:
        return type(self).__name__
"""
