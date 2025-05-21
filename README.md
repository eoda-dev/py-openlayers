# py-openlayers: OpenLayers for Python

[![Release](https://img.shields.io/github/v/release/eoda-dev/py-openlayers)](https://img.shields.io/github/v/release/eoda-dev/py-openlayers)
[![pypi](https://img.shields.io/pypi/v/openlayers.svg)](https://pypi.python.org/pypi/openlayers)
[![License](https://img.shields.io/github/license/eoda-dev/py-openlayers)](https://img.shields.io/github/license/eoda-dev/py-openlayers)
[![OpenLayers JS](https://img.shields.io/badge/OpenLayers-v10.5.0-blue.svg)](https://github.com/openlayers/openlayers/releases//tag/v10.5.0)

Provides Python bindings for [Openlayers](https://openlayers.org/), a high-performance, full-featured web mapping library that displays maps from various sources and formats. It makes it a easy to create interactive maps in [Marimo](https://marimo.io/) and [Jupyter](https://jupyter.org/) notebbooks with a few lines of code in a pydantic way.

## Features

### Tiled Layers

Pull tiles from OSM, CartoDB, MapTiler and any other XYZ source.


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

## Installation

```bash
uv init

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

## Note

The documentation is still in an early stage, more examples will be added as soon as possible.
