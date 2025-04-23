from pydantic import Field

from .abstracts import MyBaseModel
from .view import View

class MapOptions(MyBaseModel):
    view: View = Field(serialization_alias="viewOptions")
    controls: list[dict] | None = None
    layers: list[dict] | None = None
