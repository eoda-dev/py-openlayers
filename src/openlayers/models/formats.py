from __future__ import annotations

from typing import Union
from .core import OLBaseModel


# --- Base format
class Format(OLBaseModel): ...


# --- Formats
class GeoJSON(Format): ...


class KML(Format): ...


# --- Format type
FormatT = Union[Format, GeoJSON, KML]
