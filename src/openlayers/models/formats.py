from __future__ import annotations

from typing import Union

from pydantic import Field

from .core import OLBaseModel


# --- Base format
class Format(OLBaseModel): ...


# --- Formats
class GeoJSON(Format): ...


class TopoJSON(Format): ...


class KML(Format):
    extract_styles: bool = Field(True, serialization_alias="extractStyles")


class GPX(Format): ...


# --- Format type
FormatT = Union[Format, GeoJSON, KML, GPX, TopoJSON]
