from openlayers.config import Backend, config, defaults


def test_config() -> None:
    defaults.backend = Backend.STANDALONE

    print(config)
    print(defaults.model_dump())
