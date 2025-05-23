from __future__ import annotations

from pydantic import Field

from .core import OLBaseModel


# TODO: Use pyproj instead
class Projection(object):
    MERCATOR = "EPSG:4326"
    WEB_MERCATOR = "EPSG:3857"

    @staticmethod
    def from_epsg(code: int) -> str:
        return f"EPSG:{code}"


class View(OLBaseModel):
    """A View object represents a simple 2D view of the map

    Note:
        See [module-ol_View-View.html](https://openlayers.org/en/latest/apidoc/module-ol_View-View.html) for details.

    Attributes:
        center (tuple[float, float]): The center for the view as (lon, lat) pair
        zoom (float | int): The Zoom level used to calculate the resolution for the view
        projection (str): The projection
        rotation (float | int): The rotation for the view in radians (positive rotation clockwise, 0 means north).
        extent (tuple[float, float, float, float] | list[float, float, float, float]): The extent that constrains the view,
            in other words, nothing outside of this extent can be visible on the map
        min_zoom (float | int): The minimum zoom level used to determine the resolution constraint
        max_zoom (float | int): The maximum zoom level used to determine the resolution constraint
    """

    center: tuple[float, float] | None = (0, 0)
    zoom: float | int | None = 0
    projection: str | None = Projection.WEB_MERCATOR
    rotation: float | int | None = None
    extent: (
        tuple[float, float, float, float] | list[float, float, float, float] | None
    ) = None
    min_zoom: int | float | None = Field(None, serialization_alias="minZoom")
    max_zoom: int | float | None = Field(None, serialization_alias="maxZoom")
