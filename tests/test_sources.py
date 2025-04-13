from openlayers.sources import OSM


def test_osm_source():
    osm = OSM()

    print(osm.to_dict())
