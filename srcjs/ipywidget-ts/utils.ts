import type { MapBrowserEvent } from "ol";
import type { FeatureLike } from "ol/Feature";
import type { FeatureProps } from ".";
import type { View } from "ol";

import { toLonLat } from "ol/proj";

// TODO: get 'info' from 'parseView' 
function parseClickEvent(e: MapBrowserEvent): any {
    const view = e.target.getView();
    const projectionCode = view.getProjection().getCode();
    const info = {
        center: view.getCenter(),
        projection: projectionCode,
        zoom: view.getZoom(),
        centerLonLat: toLonLat(e.coordinate)
    };
    return info;
}

function parseView(view: View): any {
    const center = view.getCenter() || [];
    const projectionCode = view.getProjection().getCode();
    return {
        center: center,
        projection: projectionCode,
        zoom: view.getZoom(),
        center_lonlat: toLonLat(center)
    };
}

function getFeatureProperties(feature: FeatureLike): FeatureProps {
    let { geometry, ...props } = feature.getProperties();
    return props;
}

export { parseClickEvent, getFeatureProperties, parseView }
