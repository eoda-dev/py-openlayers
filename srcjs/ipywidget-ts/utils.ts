import { MapBrowserEvent } from "ol";
import { transform as transformProj } from "ol/proj";

function parseClickEvent(e: MapBrowserEvent): any {
    const view = e.target.getView();
    const projectionCode = view.getProjection().getCode();
    const info = {
        center: view.getCenter(),
        projection: projectionCode,
        zoom: view.getZoom(),
        lnglat: transformProj(e.coordinate, projectionCode, "EPSG:4326")
    };
    return info;
}

export { parseClickEvent }
