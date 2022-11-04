# SPDX-License-Identifier: Apache-2.0

import omni.ui as ui


style = {
    "color": ui.color.red,
    "background_color": ui.color.blue,
    "secondary_color": ui.color.white,
}

class CustomProgressValueModel(ui.AbstractValueModel):
    """An example of custom float model that can be used for progress bar"""

    def __init__(self, value: float):
        super().__init__()
        self._value = value

    def set_value(self, value):
        """Reimplemented set"""
        try:
            value = float(value)
        except ValueError:
            value = None
        if value != self._value:
            # Tell the widget that the model is changed
            self._value = value
            self._value_changed()

    def get_value_as_float(self):
        return self._value

    def get_value_as_string(self):
        return f"{self._value*100:.0f}%"


my_window = ui.Window("Example Window", width=300, height=300)
with my_window.frame:
    with ui.VStack():
        model = CustomProgressValueModel(0.0)
        pb = ui.ProgressBar(model, style=style, height=0)
        # pb = ui.ProgressBar(style=style, height=0)


        def clicked():
            print("clicked")
            value = pb.model.as_float
            pb.model.set_value(value + 0.1)

        ui.Button("Plus One", clicked_fn=clicked)




