# SPDX-License-Identifier: Apache-2.0

import omni.usd

stage = omni.usd.get_context().get_stage()
ctx = omni.usd.get_context()

selection: omni.usd.Selection = ctx.get_selection()
selection.set_selected_prim_paths(["/World/Cube", "/World/Sphere"], False)



import omni.kit.commands
import omni.usd
ctx = omni.usd.get_context()

selection: omni.usd.Selection = ctx.get_selection()
omni.kit.commands.execute('SelectPrimsCommand',
	old_selected_paths=selection.get_selected_prim_paths(),
	new_selected_paths=["/World/Cone"],
	expand_in_stage=True)
