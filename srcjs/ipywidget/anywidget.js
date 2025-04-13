import './style.css';

function render({ model, el }) {
	console.log("Welcome to anywidget", el);
	el.innerHTML = "Welcome to anywidget";
	// const calls = model.get("calls");
	// console.log(calls);
}

export { render }

