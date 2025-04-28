import importlib.metadata

try:
    from .anywidget import MapWidget
    from .geopandas import *
except ImportError as e:
    ...

__version__ = importlib.metadata.version(__package__)

__all__ = [MapWidget]
