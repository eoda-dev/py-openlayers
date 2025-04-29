from openlayers.colors import ColorScheme, read_color_schemes

def test_color_schemes() -> None:
    cs = read_color_schemes()
    print(cs[0])
    print(len(cs[0].values))
