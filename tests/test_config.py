from openlayers.config import config, Backend

def test_config() -> None:
    config.default_backend = Backend.STANDALONE

    print(config)
