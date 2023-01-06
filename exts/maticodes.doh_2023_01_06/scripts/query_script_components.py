# SPDX-License-Identifier: Apache-2.0
from pxr import Sdf
import omni.usd

stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath("/World/Cube")
attr = prim.GetAttribute("omni:scripting:scripts")
if attr.IsValid():
    scripts = attr.Get()
    if scripts:
        for script in scripts:
            print(script)