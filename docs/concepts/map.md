# Map

The [Map](../../api/map/#openlayers.Map) is the core component of your visualization, to which other components such as [controls](../controls), [layers](../layers) or overlays are added. Components can be added either during initialization or afterwards:

```python
-8<-- "concepts/basic_map.py"
```

## View state

Properties such as _center_, _zoom level_ and _projection_ are managed by the [View](../../api/map/#openlayers.view.View) instance:

```python
-8<-- "concepts/view.py"
```

```python {marimo display_code=true}
import marimo as mo
import openlayers as ol

m = ol.MapWidget(ol.View(center=(172.606201, -43.556510), zoom=12))

w = mo.ui.anywidget(m)
w
```

```python {marimo display_code=true}
w.value["view_state"]
```

## Basemaps

A basemap in openlayers consists of one or more layers from your layer stack:

```python
-8<-- "concepts/basemaps.py"
```

> See [BasemapLayer API](../../api/basemaps/#openlayers.Basemaps.BasemapLayer)

If you hand over an empty layer stack to your map, a blank background is displayed:

```python
m = ol.Map(layers=[])
```
