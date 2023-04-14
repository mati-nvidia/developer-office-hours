# SPDX-License-Identifier: Apache-2.0

import omni.kit.actions.core

action_registry = omni.kit.actions.core.get_action_registry()
action = action_registry.get_action("omni.kit.ui.editor_menu_bridge", "action_editor_menu_bridge_window_fullscreen_mode")
action.execute()