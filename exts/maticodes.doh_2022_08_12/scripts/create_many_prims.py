# SPDX-License-Identifier: Apache-2.0

from pxr import UsdGeom
import omni.kit.commands
import omni.usd

stage = omni.usd.get_context().get_stage()

cube_paths = []
for i in range(10):
    cube_path = omni.usd.get_stage_next_free_path(stage, "/World/Cube", prepend_default_prim=False)
    cube_paths.append(cube_path)
    omni.kit.commands.execute("CreatePrim", prim_type="Cube", prim_path=cube_path)
    # UsdGeom.Cube.Define(stage, cube_path)
