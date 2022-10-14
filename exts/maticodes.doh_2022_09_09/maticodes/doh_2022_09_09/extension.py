# SPDX-License-Identifier: Apache-2.0

import carb
import omni.ext
import omni.kit.commands
import omni.ui as ui
import omni.usd
from pxr import Gf, Sdf

# Check out: USDColorModel
# C:\ext_projects\omni-dev-office-hours\app\kit\exts\omni.example.ui\omni\example\ui\scripts\colorwidget_doc.py
class MyWindow(ui.Window):
    def __init__(self, title: str = None, **kwargs):
        super().__init__(title, **kwargs)
        self._color_model = None
        self._color_changed_subs = []
        self._path_model = None
        self._change_info_path_subscription = None
        self._path_changed_sub = None
        self._stage = omni.usd.get_context().get_stage()
        self.frame.set_build_fn(self._build_window)

    def _build_window(self):
        with ui.ScrollingFrame():
            with ui.VStack(height=0):
                
                ui.Label("Property Path")
                self._path_model = ui.StringField().model
                self._path_changed_sub = self._path_model.subscribe_value_changed_fn(
                    self._on_path_changed
                )
                ui.Label("Color")
                with ui.HStack(spacing=5):
                    self._color_model = ui.ColorWidget(width=0, height=0).model
                    for item in self._color_model.get_item_children():
                        component = self._color_model.get_item_value_model(item)
                        self._color_changed_subs.append(component.subscribe_value_changed_fn(self._on_color_changed))
                        ui.FloatField(component)
    
    def _on_mtl_attr_changed(self, path):
        color_attr = self._stage.GetAttributeAtPath(path)
        color_model_items = self._color_model.get_item_children()
        if color_attr:
            color = color_attr.Get()
            for i in range(len(color)):
                component = self._color_model.get_item_value_model(color_model_items[i])
                component.set_value(color[i])

    def _on_path_changed(self, model):
        if Sdf.Path.IsValidPathString(model.as_string):
            attr_path = Sdf.Path(model.as_string)
            color_attr = self._stage.GetAttributeAtPath(attr_path)
            if color_attr:
                self._change_info_path_subscription = omni.usd.get_watcher().subscribe_to_change_info_path(
                    attr_path, 
                    self._on_mtl_attr_changed
                )

    def _on_color_changed(self, model):
        values = []
        for item in self._color_model.get_item_children():
            component = self._color_model.get_item_value_model(item)
            values.append(component.as_float)
        
        if Sdf.Path.IsValidPathString(self._path_model.as_string):
            attr_path = Sdf.Path(self._path_model.as_string)
            color_attr = self._stage.GetAttributeAtPath(attr_path)
            if color_attr:
                color_attr.Set(Gf.Vec3f(*values[0:3]))
    
    def destroy(self) -> None:
        self._change_info_path_subscription = None
        self._color_changed_subs = None
        self._path_changed_sub = None
        return super().destroy()


class MyExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        carb.log_info("[maticodes.doh_2022_09_09] Dev Office Hours Extension (2022-09-09) startup")
        self._window = MyWindow("MyWindow", width=300, height=300)

    def on_shutdown(self):
        carb.log_info("[maticodes.doh_2022_09_09] Dev Office Hours Extension (2022-09-09) shutdown")
        if self._window:
            self._window.destroy()
            self._window = None
