try:
    from .anywidget import MapWidget
    from .geopandas import *
except ImportError as e:
    ...

__all__ = [MapWidget]
