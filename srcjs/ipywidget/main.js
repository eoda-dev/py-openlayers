// Test
import * as layers from "ol/layer";
window.olLayers = layers;

import render from "./anywidget";

const data = {
  map_options: {
    layers: []
  },
  view_options: {
    center: [0, 0],
    zoom: 4,
  },
};

const model = {
  get: function (key) {
    return data[key];
  },
};
const el = document.getElementById("map");
// el.style.height = "600px";

render({ model, el });
