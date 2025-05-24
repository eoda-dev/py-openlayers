# Controls

Controls are user interface elements that you can add to your map:

```python
-8<-- "concepts/controls.py"
```

> See [Controls API](../../api/controls/)

```python {marimo display_code=True}
import openlayers as ol
from openlayers.basemaps import CartoBasemapLayer

m = ol.MapWidget(
    layers=[CartoBasemapLayer()],
    controls=[ol.OverviewMapControl(collapsed=False)]
)
m
```
