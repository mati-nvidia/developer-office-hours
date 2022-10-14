import asyncio

import carb
import omni.ext
import omni.ui as ui


class MyWindow(ui.Window):
    def __init__(self, title: str = None, **kwargs):
        super().__init__(title, **kwargs)
        self.frame.set_build_fn(self._build_window)

    def _build_window(self):
        def hello():
            print("Hello")
        ui.Button("Click Me", clicked_fn=hello)


        

class MyExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        carb.log_info("[maticodes.doh_2022_10_14] Dev Office Hours Extension (2022-10-14) startup")
        self._window = MyWindow("MyWindow", width=300, height=300)

    def on_shutdown(self):
        carb.log_info("[maticodes.doh_2022_10_14] Dev Office Hours Extension (2022-10-14) shutdown")
        if self._window:
            self._window.destroy()
            self._window = None
