# SPDX-License-Identifier: Apache-2.0

# https://docs.omniverse.nvidia.com/kit/docs/omni.kit.window.file_exporter/latest/index.html

from omni.kit.window.file_exporter import get_file_exporter
from typing import List

file_exporter = get_file_exporter()

def export_handler(filename: str, dirname: str, extension: str = "", selections: List[str] = []):
    # NOTE: Get user inputs from self._export_options, if needed.
    print(f"> Export As '{filename}{extension}' to '{dirname}' with additional selections '{selections}'")

file_exporter.show_window(
    title="Export As ...",
    export_button_label="Save",
    export_handler=export_handler,
)