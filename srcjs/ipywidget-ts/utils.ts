import type { MapBrowserEvent } from "ol";
import type { FeatureLike } from "ol/Feature";
import type { FeatureProps } from ".";

import { transform as transformProj, toLonLat } from "ol/proj";

function parseClickEvent(e: MapBrowserEvent): any {
    const view = e.target.getView();
    const projectionCode = view.getProjection().getCode();
    const info = {
        center: view.getCenter(),
        projection: projectionCode,
        zoom: view.getZoom(),
        // lnglat: transformProj(e.coordinate, projectionCode, "EPSG:4326")
        lonLat: toLonLat(e.coordinate)
    };
    return info;
}

function getFeatureProperties(feature: FeatureLike): FeatureProps {
    let { geometry, ...props } = feature.getProperties();
    return props;
}

export { parseClickEvent, getFeatureProperties }
