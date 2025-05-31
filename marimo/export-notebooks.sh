#!/bin/bash
output_folder=${1:-dist}
files=("getting-started.py" "pmtiles-vector.py" "drag-and-drop.py" "draw-control.py" "earthquakes-heatmap.py" "airport-icons.py")

for file in "${files[@]}"; do
  without_extension="${file%.*}"
  marimo export html-wasm "$file" -o $output_folder/"$without_extension".html --mode edit
done

