# SPDX-License-Identifier: Apache-2.0
import asyncio
from pathlib import Path

import carb
import omni.ext
import omni.ui as ui
import omni.usd

test_stage_path = Path(__file__).parent.parent.parent / "data" / "test_stage.usd"

class MyWindow(ui.Window):
    def __init__(self, title: str = None, **kwargs):
        super().__init__(title, **kwargs)
        self.frame.set_build_fn(self._build_window)

    def _build_window(self):
        with ui.ScrollingFrame():
            with ui.VStack(height=0):
                ui.Label("My Label")

                def clicked():
                    carb.log_info(test_stage_path)
                    # Synch option
                    # omni.usd.get_context().open_stage(str(test_stage_path))

                    # Async Option
                    # asyncio.ensure_future(self.open_stage())

                    # Async with Callback
                    omni.usd.get_context().open_stage_with_callback(str(test_stage_path), self.on_stage_open_finished)

                ui.Button("Click Me", clicked_fn=clicked)

    async def open_stage(self):
        (result, error) = await omni.usd.get_context().open_stage_async(str(test_stage_path))
        #Now that we've waited for the scene to open, we should be able to get the stage
        stage = omni.usd.get_context().get_stage()

        print (f"opened stage {stage} with result {result}")
    
    def on_stage_open_finished(self, result: bool, path: str):
        stage = omni.usd.get_context().get_stage()
        print (f"opened stage {stage} with result {result}")



class MyExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        carb.log_info("[maticodes.doh_2023_08_18] Dev Office Hours Extension (2023-08-18) startup")
        self._window = MyWindow("MyWindow", width=300, height=300)

    def on_shutdown(self):
        carb.log_info("[maticodes.doh_2023_08_18] Dev Office Hours Extension (2023-08-18) shutdown")
        if self._window:
            self._window.destroy()
            self._window = None
