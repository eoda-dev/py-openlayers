from pydantic import BaseModel, ConfigDict, computed_field


class OLBaseModel(BaseModel):
    model_config = ConfigDict(extra="allow", validate_default=True)

    def model_dump(self, **kwargs) -> dict:
        return super().model_dump(exclude_none=True, by_alias=True, **kwargs)

    def to_dict(self, *args, **kwargs) -> dict:
        return super().model_dump(*args, **kwargs)

    @computed_field(alias="@@type")
    def type(self) -> str:
        return type(self).__name__
