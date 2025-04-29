from pydantic import BaseModel, ConfigDict, computed_field


class OLBaseModel(BaseModel):
    model_config = ConfigDict(extra="allow")

    def model_dump(self, **kwargs) -> dict:
        return super().model_dump(exclude_none=True, by_alias=True, **kwargs)

    @computed_field(alias="@@type")
    def type(self) -> str:
        return type(self).__name__
