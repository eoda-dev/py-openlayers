import openlayers as ol

# Add components during initialization
m = ol.Map(controls=[ol.ZoomSliderControl()])

# Add components after initialization
m.add_control(ol.FullScreenControl())
