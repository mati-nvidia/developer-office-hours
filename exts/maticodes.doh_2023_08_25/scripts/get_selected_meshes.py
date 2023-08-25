# SPDX-License-Identifier: Apache-2.0

import omni.usd
from pxr import Usd, UsdGeom

stage = omni.usd.get_context().get_stage()
selection = omni.usd.get_context().get_selection().get_selected_prim_paths()

meshes = []
for path in selection:
    prim = stage.GetPrimAtPath(path)
    if prim.IsA(UsdGeom.Mesh):
        meshes.append(prim)

print("Selected meshes:")
print(meshes)