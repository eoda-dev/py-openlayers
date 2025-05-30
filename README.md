# py-openlayers: OpenLayers for Python

[![Release](https://img.shields.io/github/v/release/eoda-dev/py-openlayers)](https://img.shields.io/github/v/release/eoda-dev/py-openlayers)
[![pypi](https://img.shields.io/pypi/v/openlayers.svg)](https://pypi.python.org/pypi/openlayers)
[![Build status](https://img.shields.io/github/actions/workflow/status/eoda-dev/py-openlayers/pytest.yml?branch=main)](https://img.shields.io/github/actions/workflow/status/eoda-dev/py-openlayers/pytest.yml?branch=main)
[![License](https://img.shields.io/github/license/eoda-dev/py-openlayers)](https://img.shields.io/github/license/eoda-dev/py-openlayers)
[![OpenLayers JS](https://img.shields.io/badge/OpenLayers-v10.5.0-blue.svg)](https://github.com/openlayers/openlayers/releases//tag/v10.5.0)

Provides Python bindings for [OpenLayers](https://openlayers.org/), a high-performance, full-featured web mapping library that displays maps from various sources and formats. It makes it easy to create interactive maps in [Marimo](https://marimo.io/) and [Jupyter](https://jupyter.org/) notebooks with a few lines of code in a pythonic way.

## Features

### Tiled Layers

Pull tiles from OSM, [Carto](https://github.com/CartoDB/basemap-styles), [MapTiler](https://www.maptiler.com/) and any other XYZ source.

### Vector Layers

Render vector data from GeoJSON, TopoJSON, KML, GML and other formats. 

### Controls

Add geocoding, draw, full screen and other controls to your map.

### WebGL

Render large data sets using WebGL.

### PMTiles

Render PMTiles from vector and raster sources.

### Interactions

Drag and drop GPX, GeoJSON, KML or TopoJSON files on to the map. Modify, draw and select features.

### GeoPandas Extension

```python
import openlayers as ol

data = "zip+https://github.com/Toblerity/Fiona/files/11151652/coutwildrnp.zip"

gdf = ol.GeoDataFrame.from_file(data)
gdf.ol.color_category("STATE").explore()
```

## Installation

```bash
uv init

uv add openlayers

uv add "git+https://github.com/eoda-dev/py-openlayers@main"
```

## Quickstart

```python
import openlayers as ol

# Jupyter or Marimo
m = ol.MapWidget()
m # Display map

# Standalone
m = ol.Map()
m.save()
```

## Marimo Example Notebooks

* [Get started](https://eoda-dev.github.io/py-openlayers/marimo/getting-started.html)
* [PMTiles](https://eoda-dev.github.io/py-openlayers/marimo/pmtiles-vector.html)
* [Drag and drop](https://eoda-dev.github.io/py-openlayers/marimo/drag-and-drop.html)
* [Style expressions](https://marimo.app/l/ig7brp)
* [Heatmap](https://eoda-dev.github.io/py-openlayers/marimo/earthquakes-heatmap.html)


## Shiny Example Apps

* [Get started](https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMASxlWICcyACAKwGdSAdCXgM0bEYLABZkYAGzLFikjizoNmYgIwChIjqJoRsAdxoATAOZwyCpU1aM4UQmRoA3OAH1bUI3ha2IRuIyuhqbmvLxWKsSolJJQ2AEKUApyGsIs2rrYivTWPnYOznCpWjp6GHAAHqi2HJY5KrqoAK5k3r7+jN5NNGEQhDRk2K6ElBSMCgC8LCC8LHMs3GAAMqRGPEgsABQArKoY2wAMAOwALN4HGKoATEcAHACUeLPziwAKUIw0HIuIWye3GFu2wAbMDvFcMABmbZXK6PZ5zRYAOTg+hYAE0mABrH5-C5Ha63bwAWlOGAOB2BB3hEAAvr1RKpNoscGRRKRiVEYnEEot7r1uhhGi1XBw4JI4A5mURRgFFt5FgBhWWMeUsQjsmgjDgTSRfMibfqDYYqjgYLFwbAcTb3W29XgAAXaASCxjMZF4-n4LDkrhgaBtiARLFirRDpBYUyNQxG5ASwEWKz86wAusGRFM5BgALJoADqbvMzIg81LPskGAAajRUYaVRNNpJSN5Q48WAAvWQwCYPJ4lstzEjkITyCbALMAeRcjCcNf0udQitIZBHhrksVQYqMEwAYlB5HB7im+6X+f25rYyE1GCWYPaIE7KB0MCR-J64N7dPxiIHg7PUaKZBQBQkZ5PYjguO4dhGJsvr+pgwTugqYD-vogHAUUYBnqWl7XiWnCkBgRhNPQ1qoehFDeLo-jkBMcL3o+4GFOU-D8JKHp+B+LCuL+54hsBLYRlGAwxqawDCmQL4qjaaZ8XBaAYIh5gYGKZAmnGjCNs2-FkGeYC0ng4DQPA1C2AAjt0tjwOQZpkBUZD4EQy6jNQXIQLE8TjLw+kpkAA)

## Documentation

[python-openlayers docs](https://eoda-dev.github.io/py-openlayers/)

## Note

The documentation is still in an early stage, more examples will be added as soon as possible.
