# SPDX-License-Identifier: Apache-2.0

from pxr import Gf, UsdGeom, Usd
import omni.usd

def decompose_matrix(mat: Gf.Matrix4d):
    reversed_ident_mtx = reversed(Gf.Matrix3d())

    translate = mat.ExtractTranslation()
    scale = Gf.Vec3d(*(v.GetLength() for v in mat.ExtractRotationMatrix()))
    #must remove scaling from mtx before calculating rotations
    mat.Orthonormalize()
    #without reversed this seems to return angles in ZYX order
    rotate = Gf.Vec3d(*reversed(mat.ExtractRotation().Decompose(*reversed_ident_mtx)))
    return translate, rotate, scale

stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath("/World/Cube")
xform = UsdGeom.Xformable(prim)
local_transformation: Gf.Matrix4d = xform.GetLocalTransformation()
print(decompose_matrix(local_transformation))


def get_local_rot(prim: Usd.Prim):
    return prim.GetAttribute("xformOp:rotateXYZ").Get()

print(get_local_rot(prim))
