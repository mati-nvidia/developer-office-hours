# SPDX-License-Identifier: Apache-2.0
import omni.kit.commands
from pxr import Sdf
import omni.usd

# Create the Python Scripting Component property
omni.kit.commands.execute('ApplyScriptingAPICommand',
	paths=[Sdf.Path('/World/Cube')])
omni.kit.commands.execute('RefreshScriptingPropertyWindowCommand')

# Add your script to the property
stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath("/World/Cube")
attr = prim.GetAttribute("omni:scripting:scripts")
scripts = attr.Get()
# Property with no script paths returns None
if scripts is None:
	scripts = []
else:
	# Property with scripts paths returns VtArray.
	# Convert to list to make it easier to work with.
	scripts = list(scripts)
scripts.append(r"C:\Users\mcodesal\Downloads\new_script.py")
attr.Set(scripts)

