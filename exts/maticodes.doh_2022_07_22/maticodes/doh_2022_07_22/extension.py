import omni.ext
import omni.ui as ui
from omni.kit.widget.searchable_combobox import build_searchable_combo_widget


class MyWindow(ui.Window):
    def __init__(self, title: str = None, delegate=None, **kwargs):
        super().__init__(title, **kwargs)
        self.frame.set_build_fn(self._build_window)

    def _build_window(self):
        with ui.ScrollingFrame():
            with ui.VStack(height=0):
                ui.Label("My Label")
                self.proj_scale_model = ui.SimpleFloatModel()
                self.proj_scale_model_sub = (
                    self.proj_scale_model.subscribe_value_changed_fn(
                        self.slider_value_changed
                    )
                )
                ui.FloatSlider(model=self.proj_scale_model, min=0, max=100)

                def do_rebuild():
                    self.frame.rebuild()

                ui.Button("Rebuild", clicked_fn=do_rebuild)

                def clicked():
                    # Example showing how to retreive the value from the model.
                    print(
                        f"Button Clicked! Slider Value: {self.proj_scale_model.as_float}"
                    )
                    self.proj_scale_model.set_value(1.0)

                ui.Button("Set Slider", clicked_fn=clicked)

                def on_combo_click_fn(model):
                    component = model.get_value_as_string()
                    print(f"{component} selected")

                component_list = ["Synthetic Data", "USD", "Kit", "UX", "UX / UI"]
                component_index = -1
                self._component_combo = build_searchable_combo_widget(
                    component_list,
                    component_index,
                    on_combo_click_fn,
                    widget_height=18,
                    default_value="Kit",
                )

    def slider_value_changed(self, model):
        # Example showing how to get the value when it changes.
        print("Slider Value:", model.as_float)

    def destroy(self) -> None:
        del self.proj_scale_model_sub
        return super().destroy()


class MyExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print(
            "[maticodes.doh_2022_07_22] Dev Office Hours Extension (2022-07-22) startup"
        )
        self._window = MyWindow("MyWindow", width=300, height=300)

    def on_shutdown(self):
        print(
            "[maticodes.doh_2022_07_22] Dev Office Hours Extension (2022-07-22) shutdown"
        )
        if self._window:
            self._window.destroy()
            self._window = None
