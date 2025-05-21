import openlayers as ol

ctrl = ol.MapTilerGeocodingControl(
    collapsed=True,
    country="de",
    limit=2
    )

m = ol.Map()
m.add_control(ctrl)
m.save()

# print(ctrl.model_dump())