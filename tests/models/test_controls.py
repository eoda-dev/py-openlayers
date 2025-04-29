import openlayers.controls as ctrl

def test_scale_line_control():
    # Act
    scale_line = ctrl.ScaleLineControl(bar=True)
    json_def = scale_line.model_dump()

    # Assert
    print(scale_line)
    print(json_def)
    
    scale_line.bar == True
    scale_line.type == "ScaleLineControl"
    json_def["@@type"] == "ScaleLineControl"
