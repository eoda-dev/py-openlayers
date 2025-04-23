from __future__ import annotations

from pydantic import BaseModel, ConfigDict, field_validator

from .sources import Source


class Layer(BaseModel):
    model_config = ConfigDict(extra="allow")

    source: Source | dict

    @field_validator("source")
    def validate_source(cls, source) -> dict:
        if isinstance(source, Source):
            return source.model_dump()
        
        return source

    def model_dump(self) -> dict:
        
        return dict(
            type=self.type,
            options=super().model_dump(exclude_none=True, by_alias=True)
        )

    @property
    def type(self) -> str:
        return type(self).__name__


class TileLayer(Layer): ...


class VectorLayer(Layer):
    style: dict | None = None

class WebGLVectorLayer(Layer):
    style: dict | None = None

class WebGLTileLayer(Layer): ...
