# SPDX-License-Identifier: Apache-2.0

import omni.ui as ui
from omni.ui import color as cl

my_window = ui.Window("Example Window", width=300, height=300)
with my_window.frame:
    with ui.VStack():
        ui.Label("AABBGGRR", style={"color": 0xFF00FFFF}) # STAY AWAY FROM
        
        ui.Label("Float RGB", style={"color": cl(1.0, 1.0, 0.0)})
        ui.Label("Float RGBA", style={"color": cl(1.0, 1.0, 0.0, 0.5)})
        
        ui.Label("Int RGB", style={"color": cl(255, 255, 0)})
        ui.Label("Int RGBA", style={"color": cl(255, 255, 0, 128)})
        ui.Label("Oops RGB", style={"color": cl(1, 1, 0)})
        
        ui.Label("Web Hex RGB", style={"color": cl("#FFFF00")})
        ui.Label("Web Hex rgb", style={"color": cl("#ffff00")})
        ui.Label("Web Hex RGBA", style={"color": cl("#FFFF0088")})
        
        ui.Label("Float RGB White", style={"color": cl(1.0, 1.0, 1.0)})
        ui.Label("Float RGB 50%", style={"color": cl(0.5, 0.5, 0.5)})
        ui.Label("Float Greyscale White", style={"color": cl(1.0)})
        ui.Label("Float Greyscale 50%", style={"color": cl(0.5)})
        ui.Label("Int Greyscale White", style={"color": cl(255)})
        ui.Label("Int Greyscale 50%", style={"color": cl(128)})

        ui.Label("Web Color Name", style={"color": cl.yellow})


