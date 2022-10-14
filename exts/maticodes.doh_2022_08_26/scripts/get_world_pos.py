# SPDX-License-Identifier: Apache-2.0

import omni.usd
from pxr import Usd, Gf

stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath("/World/Xform/Cube")
matrix:Gf.Matrix4d = omni.usd.get_world_transform_matrix(prim, time_code=Usd.TimeCode.Default())
translation = matrix.ExtractTranslation()
print(translation)