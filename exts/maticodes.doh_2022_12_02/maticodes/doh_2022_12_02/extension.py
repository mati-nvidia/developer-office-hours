# SPDX-License-Identifier: Apache-2.0

import carb
import omni.ext
import omni.ui as ui


class MyWindow(ui.Window):
    def __init__(self, title: str = None, **kwargs):
        super().__init__(title, **kwargs)
        self.frame.set_build_fn(self._build_window)

    def _build_window(self):
        with ui.ScrollingFrame():
            with ui.VStack(height=0):
                with ui.HStack(height=0):
                    ui.Label("My Label")
                    MyCoolComponent()

                def clicked():
                    carb.log_info("Button Clicked!")

                ui.Button("Click Me", clicked_fn=clicked)

class MyCoolComponent:
    def __init__(self):
        with ui.VStack():
            ui.Label("Moar labels- asdfasdfasdf")
            ui.Label("Even moar labels")
            with ui.HStack():
                ui.Button("Ok")
                ui.Button("Cancel")

class MyExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        """_summary_

        Args:
            ext_id (_type_): _description_
        """
        carb.log_info("[maticodes.doh_2022_12_02] Dev Office Hours Extension (2022-12-02) startup")
        self._window = MyWindow("MyWindow", width=300, height=300)

    def on_shutdown(self):
        carb.log_info("[maticodes.doh_2022_12_02] Dev Office Hours Extension (2022-12-02) shutdown")
        if self._window:
            self._window.destroy()
            self._window = None
