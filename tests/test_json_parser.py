from pydantic import BaseModel, ConfigDict


class VectorSource:
    url: str

    def __init__(self, url):
        self.url = url


class VectorLayer(object):
    # model_config = ConfigDict(arbitrary_types_allowed=True)

    # style: dict
    # source: VectoreSource | None = None

    def __init__(self, style: dict, source: VectorSource = None):
        self.style = style
        self.source = source


TypeCatalog = dict(VectorLayer=VectorLayer, VectorSource=VectorSource)


class Identifier(BaseModel):
    TYPE: str = "@@type"
    ARGS: str = "@@args"
    GEOJSON: str = "@@geojson"


identifier = Identifier()


def istype(key: str) -> bool:
    return key == identifier.TYPE


def isargs(key: str) -> bool:
    return key == identifier.ARGS


# def isgeojson(key: str) -> bool:
#     return key == identifier.GEOJSON


def skip(key: str) -> bool:
    return key in identifier.model_dump().keys()


class JSONParser(object):
    def __init__(self) -> None: ...

    def parse(self, JSONDef: dict):
        # print("parse", JSONDef)
        type = JSONDef[identifier.TYPE]
        # print("type detected", TypeCatalog[type])
        values = {k: v for k, v in JSONDef.items() if not istype(k)}
        # print("values", values)
        args = self.parse_args(values)
        # print("args", args)
        return TypeCatalog[type](**args)

    def parse_args(self, kwargs: dict) -> dict:
        parsed_kwargs = dict()
        for k, v in kwargs.items():
            if k == identifier.TYPE:
                ...
            #  Is new type
            if isinstance(v, dict) and identifier.TYPE in v.keys():
                parsed_kwargs[k] = self.parse(v)
            else:
                parsed_kwargs[k] = v

        return parsed_kwargs


def test_JSONParser():
    JSONDef = {
        "@@type": "VectorLayer",
        "style": {"a": 10, "b": 20},
        "source": {"@@type": "VectorSource", "url": "myUrl.de"},
    }

    parser = JSONParser()
    result = parser.parse(JSONDef)
    print(type(result), result, result.source)
