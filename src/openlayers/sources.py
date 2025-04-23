from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, computed_field


class Source(BaseModel):
    model_config = ConfigDict(extra="allow")

    def model_dump(self) -> dict:
        return dict(
            type=self.type, options=super().model_dump(exclude_none=True, by_alias=True)
        )

    @property
    def type(self) -> str:
        return type(self).__name__


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


class GeoTIFFSource(Source):
    sources: list[dict]

    @property
    def type(self) -> str:
        return "GeoTIFFSource"

SourceT = Union[OSM | VectorSource | GeoJSONSource | GeoTIFFSource]
