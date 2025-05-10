import MapWidget from "./map";

function filter(obj: any): any {
    let objFiltered: any = {}
    for (let key in obj) {
        if (typeof obj[key] !== "object")
            objFiltered[key] = obj[key];
    }

    return objFiltered;
}

function addEventListernersToMapWidget(mapWidget: MapWidget): void {
    const map = mapWidget.getMap();
    const metadata = mapWidget.getMetadata();

    // --- Layers
    map.getLayers().on("add", (e) => {
        const layer = e.element;
        const props = filter(layer.getProperties());
        metadata.layers.push(props);
        console.log("layer", layer.get("id"), "added", metadata);
    });

    map.getLayers().on("remove", (e) => {
        const layer = e.element;
        const layerId = layer.get("id");
        metadata.layers = metadata.layers.filter(item => item.id != layerId);
        console.log("layer", layerId, "removed", metadata);
    });

    // --- Controls
    map.getControls().on("add", (e) => {
        const control = e.element;
        metadata.controls.push(control.getProperties());
        console.log("control", control.get("id"), "added", metadata);
    });

    map.getControls().on("remove", (e) => {
        const control = e.element;
        const controlId = control.get("id");
        metadata.controls = metadata.controls.filter(item => item.id != controlId);
        console.log("control", controlId, "removed", metadata);
    });
}

export { addEventListernersToMapWidget };
