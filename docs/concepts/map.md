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
