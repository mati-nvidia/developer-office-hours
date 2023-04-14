# SPDX-License-Identifier: Apache-2.0

import omni.kit.actions.core

action_registry = omni.kit.actions.core.get_action_registry()
action = action_registry.get_action("ext_id", "action_id")
action.execute()