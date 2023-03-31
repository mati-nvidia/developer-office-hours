# SPDX-License-Identifier: Apache-2.0

from omni.kit.scripting import BehaviorScript
from omni.kit.viewport.utility import get_active_viewport_window
import omni.ui as ui

class ViewportUi(BehaviorScript):
    def on_init(self):
        # print(f"{__class__.__name__}.on_init()->{self.prim_path}")
        self.frame = None
    
    def on_destroy(self):
        print(f"{__class__.__name__}.on_destroy()->{self.prim_path}")
        if self.frame is not None:
            self.frame.destroy()
            self.frame = None

    def test(self):
        print("Hello World!")

    def on_play(self):
        print(f"{__class__.__name__}.on_play()->{self.prim_path}")
        self.viewport_window = get_active_viewport_window()
        self.frame = self.viewport_window.get_frame("Really cool id")
        with self.frame:
            with ui.Placer(offset_x=10, offset_y=50):
                with ui.HStack():
                    ui.Button("Test", width=50, height=50, clicked_fn=self.test)


    def on_pause(self):
        print(f"{__class__.__name__}.on_pause()->{self.prim_path}")

    def on_stop(self):
        print(f"{__class__.__name__}.on_stop()->{self.prim_path}")
        if self.frame is not None:
            self.frame.destroy()
            self.frame = None

    def on_update(self, current_time: float, delta_time: float):
        # print(f"{__class__.__name__}.on_update(current_time={current_time}, delta_time={delta_time})->{self.prim_path}")
        pass
