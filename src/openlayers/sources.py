from __future__ import annotations

from pydantic import computed_field
from typing import Optional

from .abstracts import Source


class OSM(Source): ...

class VectorSource(Source):
    url: str | None = None
    format: str | None = "geojson"

class GeoJSONSource(Source):
    url: str | None = None

    @computed_field
    def format(self) -> str:
        return "geojson"

    @property
    def type(self) -> str:
        return "VectorSource"
