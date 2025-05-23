import openlayers as ol

# Add controls during initialization
m = ol.Map(controls=[ol.ZoomSliderControl(), ol.OverviewMapControl()])

# Add components after initialization
m.add_control(ol.ScaleLineControl(units="degrees"))
