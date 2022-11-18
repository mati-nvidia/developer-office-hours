# SPDX-License-Identifier: Apache-2.0

import carb
import omni.ext
from omni.kit.viewport.utility import get_active_viewport_window
import omni.ui as ui



class MyExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        carb.log_info("[maticodes.doh_2022_11_18] Dev Office Hours Extension (2022-11-18) startup")
        self.custom_frame = None
        viewport_window = get_active_viewport_window()
        if viewport_window is not None:
            self.custom_frame: ui.Frame = viewport_window.get_frame(ext_id)
            with self.custom_frame:
                with ui.VStack():
                    ui.Spacer()
                    with ui.HStack(height=0):
                        ui.Spacer()
                        ui.Button("Hello", width=0, height=0)
        

    def on_shutdown(self):
        carb.log_info("[maticodes.doh_2022_11_18] Dev Office Hours Extension (2022-11-18) shutdown")
        self.custom_frame.destroy()
        self.custom_frame = None
        
