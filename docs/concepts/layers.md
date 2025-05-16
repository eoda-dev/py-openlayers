# Layers and sources

Sources and layers are used to display _raster_ or _vector_ data on your map.  

## Sources

Sources state which data the map should display.

```python
-8<-- "concepts/sources.py"
```

> See [Sources API](../../api/layers/)

## Layers

 A layer defines how a source is displayed on the map:

```python
-8<-- "concepts/layers.py"
```

> See [Layers API](../../api/layers/)

## Styles

Vector layers can be styled with a style object containing properties for _stroke_, _fill_, etc.:

```python
style = ol.FlatStyle(
    stroke_color = "yellow",
    stroke_width = 1.5,
    fill_color = "orange" 
)
```

It is also possible to use a simple dictonary instead. In this case property names must use hyphens instead
of underscores:

```python
const style = {
  "stroke-color": "yellow",
  "stroke-width": 1.5,
  "fill-color": "orange",
}
```

> See [Styles API](../../api/styles/) and [ol/style/flat](https://openlayers.org/en/latest/apidoc/module-ol_style_flat.html) for details.
