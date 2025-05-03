import type { ViewOptions } from "ol/View";

declare type MyMapOptions = {
    // TODO: Pass View JSONDef instead of ViewOptions only
    // viewOptions: ViewOptions | undefined;
    view: JSONDef;
    layers: JSONDef[] | undefined;
    controls: JSONDef[] | undefined;
    calls: OLAnyWidgetCall[] | undefined
};

declare type FeatureProps = {
    [x: string]: any;
};
