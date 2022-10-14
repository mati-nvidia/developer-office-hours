# SPDX-License-Identifier: Apache-2.0

import omni.ui as ui

my_window = ui.Window("Example Window", width=300, height=300)
with my_window.frame:
    with ui.VStack():
        with ui.CollapsableFrame():
            with ui.VStack():
                ui.FloatField()
                ui.FloatField()

        ui.Button("Button 1")