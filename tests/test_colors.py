from openlayers.colors import ColorScheme, read_color_schemes, Color

def test_color_schemes() -> None:
    cs = read_color_schemes()
    print(cs[0])
    print(len(cs[0].values))

def test_random_hex_colors() -> None:
    n = 6

    hex_colors = Color.random_hex_colors(n)
    print(hex_colors)

    rgb_colors = Color.random_rgb_colors(n)
    print(rgb_colors)

def test_color_by_cat() -> None:
    import pandas as pd

    id = [1, 2, 3, 4, 5, 6]
    letter = ["a", "b", "c", "a", "a", "b"]
    df = pd.DataFrame(dict(id=id, letter=letter))

    # codes = pd.Categorical(df["letter"]).codes
    # colors = Color.random_hex_colors(len(codes))
    # df["_color"] = [colors[code] for code in codes]
    # print(df)
    colors = Color.random_hex_colors_by_category(df["letter"])
    print(colors)