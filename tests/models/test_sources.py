from openlayers.sources import OSM, VectorSource


def test_osm_source() -> None:
    # Act
    osm = OSM()
    json_def = osm.model_dump()

    # Assert
    print(json_def)
    assert json_def == {"@@type": "OSM"}


def test_vector_source() -> None:
    # Act
    populated_places = VectorSource(
        url="https://openlayers.org/data/vector/populated-places.json",
    )
    json_def = populated_places.model_dump()

    # Assert
    print(json_def)
    assert json_def["@@type"] == "VectorSource"
    assert json_def["format"] == {"@@type": "GeoJSON"}
