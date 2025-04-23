# from typing import Any

from pydantic import BaseModel, ConfigDict


class MyBaseModel(BaseModel):
    def to_dict(self) -> dict:
        return self.model_dump()

    def model_dump(self) -> dict:
        return super().model_dump(exclude_none=True, by_alias=True)


class BaseType(BaseModel):
    model_config = ConfigDict(extra="allow")

    def model_dump(self) -> dict:
        return dict(
            type=self.type, options=super().model_dump(exclude_none=True, by_alias=True)
        )

    @property
    def type(self) -> str:
        return type(self).__name__
