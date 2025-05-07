from __future__ import annotations

from pydantic import Field

from typing import Union
from .core import OLBaseModel


# --- Base format
class Format(OLBaseModel): ...


# --- Formats
class GeoJSON(Format): ...


class KML(Format):
    extract_styles: bool = Field(True, serialization_alias="extractStyles")
    


# --- Format type
FormatT = Union[Format, GeoJSON, KML]
