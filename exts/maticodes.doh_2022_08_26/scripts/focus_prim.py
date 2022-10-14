# SPDX-License-Identifier: Apache-2.0

#######################################
# MUST ENABLE omni.kit.viewport.utility
#######################################

from omni.kit.viewport.utility import get_active_viewport, frame_viewport_selection
import omni.usd

# Select what you want to focus on
selection = omni.usd.get_selection()
selection.set_selected_prim_paths(["/World/Cube"], True)

# focus on selection
active_viewport = get_active_viewport()
if active_viewport:
    frame_viewport_selection(active_viewport)