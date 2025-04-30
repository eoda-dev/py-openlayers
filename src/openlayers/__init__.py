import importlib.metadata

try:
    from .anywidget import MapWidget
    from .geopandas import *
except ImportError as e:
    MapWidget = "undefined"

from . import controls
from . import layers
from .layers import *

__version__ = importlib.metadata.version(__package__)

__all__ = ["MapWidget", "controls", "layers"]
