# SPDX-License-Identifier: Apache-2.0

from pxr import Gf, UsdGeom, Usd
import omni.usd

stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath("/World/Camera")
xform = UsdGeom.Xformable(prim)
local_transformation: Gf.Matrix4d = xform.GetLocalTransformation()
# Apply the local matrix to the start and end points of the camera's default forward vector (-Z)
a: Gf.Vec4d = Gf.Vec4d(0,0,0,1) * local_transformation
b: Gf.Vec4d = Gf.Vec4d(0,0,-1,1) * local_transformation
# Get the vector between those two points to get the camera's current forward vector
cam_fwd_vec = b-a
# Convert to Vec3 and then normalize to get unit vector
cam_fwd_unit_vec = Gf.Vec3d(cam_fwd_vec[:3]).GetNormalized()
# Multiply the forward direction vector with how far forward you want to move
forward_step = cam_fwd_unit_vec * 100
# Create a new matrix with the translation that you want to perform
offset_mat = Gf.Matrix4d()
offset_mat.SetTranslate(forward_step)
# Apply the translation to the current local transform
new_transform = local_transformation * offset_mat
# Extract the new translation
translate: Gf.Vec3d = new_transform.ExtractTranslation()
# Update the attribute
prim.GetAttribute("xformOp:translate").Set(translate)