# SPDX-License-Identifier: Apache-2.0

import omni.ui as ui

my_window = ui.Window("Example Window", width=300, height=300)
model = ui.SimpleFloatModel()
sub = None
with my_window.frame:
    with ui.VStack():
        ui.FloatSlider(model=model)
        
        def body_moved(body, model):
            if body.offset_x.value > 100:
                body.offset_x.value = 100
            elif body.offset_x.value < 0:
                body.offset_x.value = 0
            
            model.set_value(body.offset_x.value / 100.0)

        body = ui.Placer(draggable=True, drag_axis=ui.Axis.X, offset_x=0)
        with body:
            rect = ui.Rectangle(width=25, height=25, style={"background_color": ui.color.red})
            body.set_offset_x_changed_fn(lambda _, b=body, m=model: body_moved(b, m))
        
        def slider_moved(model, body):
            body.offset_x.value = model.as_float * 100
        sub = model.subscribe_value_changed_fn(lambda m=model, b=body: slider_moved(m, b))
