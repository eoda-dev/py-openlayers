# Style expressions

<iframe src="https://marimo.app/l/5a5k2w?embed=true" width="100%" height=700 frameBorder="0"></iframe>

```python
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
```
