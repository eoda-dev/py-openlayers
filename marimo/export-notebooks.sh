#!/bin/bash
files=("getting-started.py", "pmtiles-vector.py")

for file in "${files[@]}"; do
  without_extension="${file%.*}"
  marimo export html-wasm "$file" -o dist/"$without_extension".html --mode edit
done

