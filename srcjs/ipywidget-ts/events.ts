import { DrawControl } from "./custom-controls/draw";

import type MapWidget from "./map";

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
    // const features = mapWidget._features;
    const model = mapWidget.getAnywidgetModel();

    const updateModel = (): void => {
        if (model) {
            model.set("metadata", metadata);
            model.save_changes();
        }
    }

    // --- Layers
    map.getLayers().on("add", (e) => {
        const layer = e.element;
        const props = filter(layer.getProperties());
        metadata.layers.push(props);
        console.log("layer", layer.get("id"), "added", metadata);
        updateModel();
    });

    map.getLayers().on("remove", (e) => {
        const layer = e.element;
        const layerId = layer.get("id");
        metadata.layers = metadata.layers.filter(item => item.id != layerId);
        console.log("layer", layerId, "removed", metadata);
        updateModel();
    });

    // --- Controls
    map.getControls().on("add", (e) => {
        const control = e.element;
        // if (control.get("type") === "DrawControl")
        if (control instanceof DrawControl) {
            control.onAdd();
            for (const event of ["addfeature", "changefeature"]) {
                const layer = control.getLayer();
                // @ts-expect-error
                layer.getSource()?.on(event, (e) => {
                    const features = control.getGeoJSONFeatures();
                    console.log(features);
                    if (model) {
                        model.set("features", { [layer.get("id")]: features });
                        model.save_changes();
                    }
                });
            }
        }

        metadata.controls.push(control.getProperties());
        console.log("control", control.get("id"), "added", metadata);
        updateModel();
    });

    map.getControls().on("remove", (e) => {
        const control = e.element;
        const controlId = control.get("id");
        metadata.controls = metadata.controls.filter(item => item.id != controlId);
        console.log("control", controlId, "removed", metadata);
        updateModel();
    });
}

export { addEventListernersToMapWidget };
