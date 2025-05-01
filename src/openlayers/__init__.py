import importlib.metadata

try:
    from .anywidget import MapWidget
    from .geopandas import *
except ImportError as e:
    ...

from . import controls
from . import layers
from .layers import *
from .map import Map

__version__ = importlib.metadata.version(__package__)

__all__ = ["Map", "MapWidget", "controls", "layers"]
