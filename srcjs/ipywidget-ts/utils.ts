import type { Feature, MapBrowserEvent } from "ol";
import type { FeatureLike } from "ol/Feature";
import type { FeatureProps } from ".";
import type { View } from "ol";

import { GeoJSON } from "ol/format";

// import { toLonLat } from "ol/proj";

// TODO: get 'info' from 'parseView' 
function parseClickEvent(e: MapBrowserEvent): any {
    const view = e.target.getView();
    const projectionCode = view.getProjection().getCode();
    const info = {
        // center: view.getCenter(),
        coordinate: e.coordinate,
        projection: projectionCode,
        zoom: view.getZoom()
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
        extent: view.calculateExtent()
    };
}

function getFeatureProperties(feature: FeatureLike): FeatureProps {
    let { geometry, ...props } = feature.getProperties();
    return props;
}

function featureToGeoJSON(feature: Feature): any {
    return new GeoJSON().writeFeatureObject(feature);
}

export { parseClickEvent, getFeatureProperties, parseView, featureToGeoJSON }
