# SPDX-License-Identifier: Apache-2.0


from pxr import UsdGeom
import omni.usd

stage = omni.usd.get_context().get_stage()
cube = stage.GetPrimAtPath("/World/Xform/Cube")
cube_xformable = UsdGeom.Xformable(cube)
transform = cube_xformable.GetLocalTransformation()
print(transform)
transform2 = cube_xformable.GetLocalTransformation()
print(transform2)


