import type { ViewOptions } from "ol/View";

declare type MyMapOptions = {
    view: JSONDef;
    layers: JSONDef[] | undefined;
    controls: JSONDef[] | undefined;
    calls: OLAnyWidgetCall[] | undefined
};

declare type FeatureProps = {
    [x: string]: any;
};
