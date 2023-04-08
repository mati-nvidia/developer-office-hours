# SPDX-License-Identifier: Apache-2.0
from omni.kit.viewport.utility import get_active_viewport_window
import omni.ui as ui
from omni.kit.scripting import BehaviorScript
from omni.ui import scene as sc
from omni.ui import color as cl


class NewScript(BehaviorScript):
    def on_init(self):
        print(f"{__class__.__name__}.on_init()->{self.prim_path}")
        self.viewport_window = get_active_viewport_window()
        self.frame = self.viewport_window.get_frame("Super Duper Cool!")

    def on_destroy(self):
        print(f"{__class__.__name__}.on_destroy()->{self.prim_path}")

    def test(self):
        print("Hello")

    def on_play(self):
        print(f"{__class__.__name__}.on_play()->{self.prim_path}")

        with self.frame:
            # Create a default SceneView (it has a default camera-model)
            self._scene_view = sc.SceneView()
            # Add the manipulator into the SceneView's scene
            with self._scene_view.scene:
                sc.Rectangle(5, 5, thickness=2, wireframe=False, color=cl.red)

            # Register the SceneView with the Viewport to get projection and view updates
            self.viewport_window.viewport_api.add_scene_view(self._scene_view)
        

    def on_pause(self):
        print(f"{__class__.__name__}.on_pause()->{self.prim_path}")

    def on_stop(self):
        print(f"{__class__.__name__}.on_stop()->{self.prim_path}")
        if self._scene_view:
            # Empty the SceneView of any elements it may have
            self._scene_view.scene.clear()
            # Be a good citizen, and un-register the SceneView from Viewport updates
            if self.viewport_window:
                self.viewport_window.viewport_api.remove_scene_view(self._scene_view)
        # Remove our references to these objects
        self._scene_view = None
        self.frame.destroy()

    def on_update(self, current_time: float, delta_time: float):
        # print(f"{__class__.__name__}.on_update(current_time={current_time}, delta_time={delta_time})->{self.prim_path}")
        pass


