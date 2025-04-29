from __future__ import annotations

from .core import OLBaseModel


# --- Base format
class Format(OLBaseModel): ...


# --- Formats
class GeoJSON(Format): ...
