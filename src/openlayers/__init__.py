import importlib.metadata

try:
    from .anywidget import MapWidget
    from .geopandas import *
except ImportError as e:
    ...

from . import controls, layers
from .controls import *
from .layers import *
from .models import formats
from .sources import *
from .map import Map
from .styles import FlatStyle
from .view import View

__version__ = importlib.metadata.version(__package__)

__all__ = ["Map", "View", "MapWidget", "FlatStyle", "controls", "layers", "formats"]
