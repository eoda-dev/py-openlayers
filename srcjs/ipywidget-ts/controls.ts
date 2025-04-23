import ScaleLineControl from 'ol/control/ScaleLine.js';
import FullScreenControl from 'ol/control/FullScreen.js';

const controls: Controls = {
    ScaleLineControl: ScaleLineControl,
    FullScreenControl: FullScreenControl
};

function newControl(type: any, options: any): any {
    return new controls[type](options);
}

export { newControl, controls }
