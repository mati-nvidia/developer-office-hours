import omni.ui as ui
from omni.ui import color as cl
# import omni.ui.color as color


my_window = ui.Window("Example Window", width=300, height=300)
with my_window.frame:
    with ui.VStack():
        ui.Label("Hello World!", style={"color": cl(0.0, 1.0, 0.0)})

