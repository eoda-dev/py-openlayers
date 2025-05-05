from openlayers.models.map_options import MapOptions, View
from openlayers.express import IconLayer

def test_map_options() -> None:
    express_layer = IconLayer(data="http://xyz.de", icon_src="icon.png")

    options = MapOptions(view=View(), layers=[express_layer])

    print(options.model_dump())
