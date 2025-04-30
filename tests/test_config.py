from openlayers.config import Backend, config


def test_config() -> None:
    print(config)
    print(config.model_dump())
