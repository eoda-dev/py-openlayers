import { render } from "./anywidget";

const model = {
   get: function(x) {
	   return("x");
   }
};
// const el = document.createElement("div");
const el = document.getElementById("map");

render({model, el});

