from __future__ import annotations

import base64
from pathlib import Path

from pyproj import CRS, Transformer


def create_icon_src_from_file(filename: str) -> bytes:
    with open(filename, "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode("utf-8")

    image_type = Path(filename).suffix.replace(".", "")
    return f"data:image/{image_type};base64," + encoded_image


def crs_transformer(src_epsg=3857, dest_epsg=4326) -> Transformer:
    crs_from = CRS.from_epsg(src_epsg)
    crs_to = CRS.from_epsg(dest_epsg)
    return Transformer.from_crs(crs_from=crs_from, crs_to=crs_to, always_xy=True)
