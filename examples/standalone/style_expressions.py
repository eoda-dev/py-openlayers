import openlayers as ol

polygons = ol.VectorLayer(
    background="#1a2b39",
    source=ol.VectorSource(
        url="https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_land.geojson"
    ),
    style=ol.FlatStyle(
        fill_color="darkgrey",
    ),
)

points = ol.VectorLayer(
    source=ol.VectorSource(
        url="https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_populated_places_simple.geojson"
    ),
    style=ol.FlatStyle(
        circle_radius=["get", "scalerank"],
        circle_fill_color="gray",
        circle_stroke_color="white",
    ),
)

# ---
advanced_style = [
    {
        "filter": [">", ["get", "pop_max"], 10000000],
        "style": {
            "text-value": [
                "concat",
                ["get", "adm1name"],
                ", ",
                ["get", "adm0name"],
            ],
            "text-font": "16px sans-serif",
            "text-fill-color": "white",
            "text-stroke-color": "gray",
            "text-stroke-width": 2,
        },
    },
    {
        "else": True,
        "filter": [">", ["get", "pop_max"], 5000000],
        "style": {
            "text-value": ["get", "nameascii"],
            "text-font": "12px sans-serif",
            "text-fill-color": "white",
            "text-stroke-color": "gray",
            "text-stroke-width": 2,
        },
    },
]
# ---

text = ol.VectorLayer(
    declutter = False,
    source=ol.VectorSource(
        url="https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_populated_places_simple.geojson"
    ),
    style=advanced_style
)

m = ol.Map(layers=[polygons, points, text])
m.save()
