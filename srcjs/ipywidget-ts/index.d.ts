import type { ViewOptions } from "ol/View";

declare type MyMapOptions = {
    viewOptions: ViewOptions;
    layers: JSONDef[] | undefined;
    controls: JSONDef[] | undefined;
};
