# SPDX-License-Identifier: Apache-2.0

# https://docs.omniverse.nvidia.com/kit/docs/omni.kit.window.file_importer/latest/Overview.html

from omni.kit.window.file_importer import get_file_importer
from typing import List

file_importer = get_file_importer()

def import_handler(filename: str, dirname: str, selections: List[str] = []):
    # NOTE: Get user inputs from self._import_options, if needed.
    print(f"> Import '{filename}' from '{dirname}' or selected files '{selections}'")

file_importer.show_window(
    title="Import File",
    import_handler=import_handler
)

