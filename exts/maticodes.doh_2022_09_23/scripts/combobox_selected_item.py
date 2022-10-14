# SPDX-License-Identifier: Apache-2.0

import omni.ui as ui

my_window = ui.Window("Example Window", width=300, height=300)
combo_sub = None
options = ["One", "Two", "Three"]
with my_window.frame:
    with ui.VStack():
        combo_model: ui.AbstractItemModel = ui.ComboBox(0, *options).model

        def combo_changed(item_model: ui.AbstractItemModel, item: ui.AbstractItem):
            value_model = item_model.get_item_value_model(item)
            current_index = value_model.as_int
            option = options[current_index]
            print(f"Selected '{option}' at index {current_index}.")
        
        combo_sub = combo_model.subscribe_item_changed_fn(combo_changed)

        def clicked():
            value_model = combo_model.get_item_value_model()
            current_index = value_model.as_int
            option = options[current_index]
            print(f"Button Clicked! Selected '{option}' at index {current_index}.")


        ui.Button("Print Combo Selection", clicked_fn=clicked)
