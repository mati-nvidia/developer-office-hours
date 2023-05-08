# SPDX-License-Identifier: Apache-2.0

# RTX Path Tracing
import omni.kit.actions.core
action_registry = omni.kit.actions.core.get_action_registry()
action = action_registry.get_action("omni.kit.viewport.actions", "set_renderer_rtx_pathtracing")
action.execute()

# RTX Real-Time
import omni.kit.actions.core
action_registry = omni.kit.actions.core.get_action_registry()
action = action_registry.get_action("omni.kit.viewport.actions", "set_renderer_rtx_realtime")
action.execute()

# Storm
import omni.kit.actions.core
action_registry = omni.kit.actions.core.get_action_registry()
action = action_registry.get_action("omni.kit.viewport.actions", "set_renderer_pxr_storm")
action.execute()

# Iray
import omni.kit.actions.core
action_registry = omni.kit.actions.core.get_action_registry()
action = action_registry.get_action("omni.kit.viewport.actions", "set_renderer_iray")
action.execute()