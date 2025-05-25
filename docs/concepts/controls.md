# Controls

Controls are user interface elements that you can add to your map:

```python
-8<-- "concepts/controls.py"
```

> See [Controls API](../../api/controls/)

```python {marimo}
import micropip
await micropip.install("openlayers")
```

```python {marimo display_code=True}
import openlayers as ol

m = ol.MapWidget(
    controls=[
        ol.ZoomToExtentControl(),
        ol.ScaleLineControl()
    ]
)
m
```
