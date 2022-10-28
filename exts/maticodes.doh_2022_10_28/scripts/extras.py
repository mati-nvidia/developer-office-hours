# SPDX-License-Identifier: Apache-2.0

import omni.usd

stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath("/World/Cube")
if prim:
    print("Prim Exists")
    
from pxr import UsdGeom

# e.g., find all prims of type UsdGeom.Mesh
mesh_prims = [x for x in stage.Traverse() if x.IsA(UsdGeom.Mesh)]
mesh_prims = []
for x in stage.Traverse():
    if x.IsA(UsdGeom.Mesh):
        mesh_prims.append(x)
print(mesh_prims)