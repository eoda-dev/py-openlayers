# from typing import Any

from pydantic import BaseModel



class MyBaseModel(BaseModel):
    def to_dict(self) -> dict:
        return self.model_dump()

    def model_dump(self) -> dict:
        return super().model_dump(exclude_none=True, by_alias=True)
