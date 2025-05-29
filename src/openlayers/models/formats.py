from __future__ import annotations

from typing import Union

from pydantic import Field

from .core import OLBaseModel


# --- Base format
class Format(OLBaseModel): ...


# --- Formats
class GeoJSON(Format):
    """GeoJSON format"""

    ...


class TopoJSON(Format):
    """TopoJSON format"""

    ...


class KML(Format):
    """KML format"""

    extract_styles: bool = Field(True, serialization_alias="extractStyles")


class GPX(Format):
    """GPX format"""

    ...


class MVT(Format):
    """MVT format"""

    ...


# --- Format type
FormatT = Union[Format, GeoJSON, KML, GPX, TopoJSON, MVT]
