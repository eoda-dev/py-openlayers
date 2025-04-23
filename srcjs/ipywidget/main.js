// Test
import * as layers from "ol/layer";
window.olLayers = layers;

// import * as anywidget from "./anywidget";
import anywidget from "./anywidget";

const render = anywidget.render;
// console.log("render", anywidget.render);

const data = {
  map_options: {
    layers: [],
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
