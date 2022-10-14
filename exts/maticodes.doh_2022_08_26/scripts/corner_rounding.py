# SPDX-License-Identifier: Apache-2.0

import omni.ui as ui

my_window = ui.Window("Example Window", width=300, height=300)
with my_window.frame:
    with ui.VStack():
        ui.Rectangle(style={
            "background_color": ui.color(1.0, 0.0, 0.0),
            "border_radius":20.0
        })
        ui.Rectangle(style={
            "background_color": ui.color(0.0, 1.0, 0.0),
            "border_radius":20.0,
            "corner_flag": ui.CornerFlag.BOTTOM
        })
        ui.Rectangle(style={
            "background_color": ui.color(0.0, 0.0, 1.0),
            "border_radius":20.0,
            "corner_flag": ui.CornerFlag.TOP
        })
        ui.Rectangle(style={
            "background_color": ui.color(1.0, 0.0, 1.0),
            "border_radius":20.0,
            "corner_flag": ui.CornerFlag.TOP_RIGHT
        })