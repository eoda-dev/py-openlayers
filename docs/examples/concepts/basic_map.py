import openlayers as ol

# Add components during initialization
m = ol.Map(controls=[ol.ZoomSliderControl()])

# Add components after initialization
m.add_control(ol.FullScreenControl())

# m.add_view_call("setZoom", 5)
m.set_zoom(12)
m.set_center(lonlat=(-122.4, 37.74))
m.save()
