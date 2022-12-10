# SPDX-License-Identifier: Apache-2.0

from omni.kit.viewport.utility import get_active_viewport, capture_viewport_to_file

vp_api = get_active_viewport()
capture_viewport_to_file(vp_api, r"C:\temp\screenshot.png")