import openlayers.express as ox

url = "https://openlayers.org/data/vector/us-states.json"

m = ox.GeoJSONLayer(data=url, webgl=False).to_map()
m.add_call("addSelectFeatures")
m.save()
