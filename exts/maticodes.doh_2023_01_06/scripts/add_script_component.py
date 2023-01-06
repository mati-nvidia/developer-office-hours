# SPDX-License-Identifier: Apache-2.0
import omni.kit.commands
from pxr import Sdf
import omni.usd

omni.kit.commands.execute('ApplyScriptingAPICommand',
	paths=[Sdf.Path('/World/Cube')])
omni.kit.commands.execute('RefreshScriptingPropertyWindowCommand')

stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath("/World/Cube")
attr = prim.GetAttribute("omni:scripting:scripts")
scripts = attr.Get()
attr.Set([r"C:\Users\mcodesal\Downloads\new_script2.py"])
# attr.Set(["omniverse://localhost/Users/mcodesal/new_script2.py"])

omni.kit.commands.execute('ChangeProperty',
	prop_path=Sdf.Path('/World/Cube.omni:scripting:scripts'),
	value=Sdf.AssetPathArray(1, (Sdf.AssetPath('C:\\mcodesal\\Downloads\\new_script2.py'))),
	prev=None)


attr = prim.GetAttribute("omni:scripting:scripts")
scripts = list(attr.Get())
scripts.append(r"C:\mcodesal\Downloads\new_script.py")
attr.Set(scripts)

