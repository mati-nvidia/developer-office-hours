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
                ui.Label("My Label")

                def clicked():
                    carb.log_info("Button Clicked!")

                ui.Button("Click Me", clicked_fn=clicked)


class MyExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        carb.log_info("[maticodes.doh_2022_09_30] Dev Office Hours Extension (2022-09-30) startup")
        self._window = MyWindow("MyWindow", width=300, height=300)

    def on_shutdown(self):
        carb.log_info("[maticodes.doh_2022_09_30] Dev Office Hours Extension (2022-09-30) shutdown")
        if self._window:
            self._window.destroy()
            self._window = None
