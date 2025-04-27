import ScaleLineControl from 'ol/control/ScaleLine.js';
import FullScreenControl from 'ol/control/FullScreen.js';
import ZoomSliderControl from 'ol/control/ZoomSlider.js';
import MousePositionControl from 'ol/control/MousePosition.js';
import OverviewMapControl from 'ol/control/OverviewMap.js';
import { InfoBox } from './custom-controls';

const controlCatalog: ControlCatalog = {
    ScaleLineControl: ScaleLineControl,
    FullScreenControl: FullScreenControl,
    ZoomSliderControl: ZoomSliderControl,
    MousePositionControl: MousePositionControl,
    OverviewMapControl: OverviewMapControl,
    InfoBox: InfoBox
};

/*
function newControl(type: any, options: any): any {
    return new controlCatalog[type](options);
}
*/

export { controlCatalog }
