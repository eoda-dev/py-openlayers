# Get started

```python
-8<-- "concepts/basic_map.py"
```

Use the `Map` class if you just want to create an HTML document and the `MapWidget` class for an interactive
widget in _Marimo_ or _Jupyter_ notebooks:

```python
# Widget
m = ol.MapWidget(controls=[ol.ZoomSliderControl()])
m

# Standalone
m = Map(controls=[ol.ZoomSliderControl()])
m.save()
```

```python {marimo display_code=true}
import openlayers as ol

m = ol.MapWidget(controls=[ol.ZoomSliderControl()])
m
```
