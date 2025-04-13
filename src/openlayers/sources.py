from pydantic import computed_field

from .abstracts import MyBaseModel


class OSM(MyBaseModel):
    @computed_field
    def type(self) -> str:
        return "OSM"
