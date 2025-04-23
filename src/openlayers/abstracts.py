from pydantic import BaseModel


class MyBaseModel(BaseModel):
    def to_dict(self) -> dict:
        return self.model_dump(exclude_none=True, by_alias=True)

class Source(MyBaseModel): ...

