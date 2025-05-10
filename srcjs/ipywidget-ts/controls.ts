import ScaleLineControl from 'ol/control/ScaleLine.js';
import FullScreenControl from 'ol/control/FullScreen.js';
import ZoomSliderControl from 'ol/control/ZoomSlider.js';
import MousePositionControl from 'ol/control/MousePosition.js';
import OverviewMapControl from 'ol/control/OverviewMap.js';
import Zoom from 'ol/control/Zoom';
import Rotate from 'ol/control/Rotate';
import Attribution from 'ol/control/Attribution.js';

import { InfoBox } from './custom-controls';

const zoom = new Zoom();
zoom.setProperties({ id: "zoom", type: "ZoomControl" });

const rotate = new Rotate();
rotate.setProperties({ id: "rotate", type: "RotateControl" });

const attribution = new Attribution();
attribution.setProperties({ id: "attribution", type: "AttributionControl" });

const defaultControls = [zoom, rotate, attribution];

const controlCatalog: ControlCatalog = {
    ScaleLineControl: ScaleLineControl,
    FullScreenControl: FullScreenControl,
    ZoomSliderControl: ZoomSliderControl,
    MousePositionControl: MousePositionControl,
    OverviewMapControl: OverviewMapControl,
    ZoomControl: Zoom,
    RotateControl: Rotate,
    AttributionControl: Attribution,
    InfoBox: InfoBox
};

export { controlCatalog, defaultControls };
