# SPDX-License-Identifier: Apache-2.0


from pathlib import Path

import carb
import numpy as np
import omni.ext
import omni.kit.app
import omni.ui as ui
from PIL import Image


class MyWindow(ui.Window):
    def __init__(self, ext_path, title: str = None, **kwargs):
        super().__init__(title, **kwargs)
        data_dir = Path(ext_path) / "data"
        files = list(data_dir.glob("*"))
        self.images = []
        for f in files:
            with Image.open(f) as img:
                np_data = np.asarray(img).data
                data = img.getdata()
                self.images.append((np_data, data, img.size))
        
        self.provider = ui.ByteImageProvider()
        if hasattr(self.provider, "set_data_array"):
            self.provider.set_data_array(self.images[0][0], self.images[0][2])
        else:
            self.provider.set_bytes_data(self.images[0][1], self.images[0][2])
        self.frame.set_build_fn(self._build_window)
        
        

    def _build_window(self):
        with ui.ScrollingFrame():
            with ui.VStack(height=0):
                ui.ImageWithProvider(self.provider, width=100, height=100)

                def clicked():
                    img = self.images.pop()
                    self.images.insert(0, img)
                    if hasattr(self.provider, "set_data_array"):
                        self.provider.set_data_array(img[0], img[2])
                    else:
                        self.provider.set_bytes_data(img[1], img[2])

                ui.Button("Click Me", clicked_fn=clicked)


class MyExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        carb.log_info("[maticodes.doh_2022_11_04] Dev Office Hours Extension (2022-11-04) startup")
        manager = omni.kit.app.get_app().get_extension_manager()
        ext_path = manager.get_extension_path(ext_id)
        self._window = MyWindow(ext_path, "MyWindow", width=300, height=300)

    def on_shutdown(self):
        carb.log_info("[maticodes.doh_2022_11_04] Dev Office Hours Extension (2022-11-04) shutdown")
        if self._window:
            self._window.destroy()
            self._window = None
