# SPDX-License-Identifier: Apache-2.0

import carb
import omni.ext
from omni.kit.viewport.utility import get_active_viewport_window
import omni.ui as ui

from .viewport_scene import ViewportScene
from .object_info_model import ObjectInfoModel


class MyWindow(ui.Window):
    def __init__(self, title: str = None, delegate=None, **kwargs):
        super().__init__(title, **kwargs)
        self._viewport_scene = None
        self.obj_info_model = kwargs["obj_info_model"]
        self.frame.set_build_fn(self._build_window)

    def _build_window(self):
        with ui.ScrollingFrame():
            with ui.VStack(height=0):
                ui.Label("My Label 2")
                ui.StringField()
                ui.StringField(password_mode=True)

                def clicked():
                    self.obj_info_model.populate()

                ui.Button("Reload Object Info", clicked_fn=clicked)

    def destroy(self) -> None:
        return super().destroy()


class MyExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        
        # Get the active Viewport (which at startup is the default Viewport)
        viewport_window = get_active_viewport_window()

        # Issue an error if there is no Viewport
        if not viewport_window:
            carb.log_error(f"No Viewport Window to add {ext_id} scene to")
            return

        # Build out the scene
        model = ObjectInfoModel()
        self._viewport_scene = ViewportScene(viewport_window, ext_id, model)
        self._window = MyWindow("MyWindow", obj_info_model=model, width=300, height=300)

    def on_shutdown(self):
        if self._window:
            self._window.destroy()
            self._window = None
        
        if self._viewport_scene:
            self._viewport_scene.destroy()
            self._viewport_scene = None
