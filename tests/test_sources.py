from openlayers.sources import OSM, GeoJSONSource, VectorSource


def test_osm_source() -> None:
    osm = OSM()

    print(osm.model_dump())


def test_vector_source() -> None:
    populated_places = GeoJSONSource(
        url="https://openlayers.org/data/vector/populated-places.json",
    )
    print(populated_places.model_dump())
