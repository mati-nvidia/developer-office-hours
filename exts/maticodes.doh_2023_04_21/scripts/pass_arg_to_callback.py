# SPDX-License-Identifier: Apache-2.0

from functools import partial
import omni.ui as ui

def do_something(p1, p2):
   print(f"Hello {p1} {p2}")

window = ui.Window("My Window", width=300, height=300)
with window.frame:
    ui.Button("Click Me", clicked_fn=partial(do_something, "a", "b"))