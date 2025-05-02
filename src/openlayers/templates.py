html_template = """<!DOCTYPE html>
<html lang="en">
    
<head>
    <meta charset="UTF-8">
    <title>{{ title|default('openlayers')}}</title>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    {% for header in headers|default([]) -%}
    {{ header }}
    {% endfor -%}
    <style>
        body {
            font-family: 'Open Sans', sans-serif;
        }
        #map {
            height: {{ height|default('500px')}};
        }
    </style>
</head>

<body>
    <div id="map"></div>
    {% for script in scripts|default([]) -%}
    <script>{{ script|safe }}</script>
    {% endfor -%}
</body>

</html>"""

js_template = """// ...
(() => {
    var data = {{ data|safe }};
    renderOLMapWidget(data);
})();"""
