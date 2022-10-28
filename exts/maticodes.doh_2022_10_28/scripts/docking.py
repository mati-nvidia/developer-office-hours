# SPDX-License-Identifier: Apache-2.0

import omni.ui as ui

my_window = ui.Window("Example Window", width=300, height=300)
with my_window.frame:
	with ui.VStack():
		f = ui.FloatField()

		def clicked(f=f):
			print("clicked")
			f.model.set_value(f.model.get_value_as_float() + 1)

		ui.Button("Plus One", clicked_fn=clicked)

my_window.dock_in_window("Property", ui.DockPosition.SAME)
ui.dock_window_in_window(my_window.title, "Property", ui.DockPosition.RIGHT, 0.2)

my_window.deferred_dock_in("Content", ui.DockPolicy.TARGET_WINDOW_IS_ACTIVE)
