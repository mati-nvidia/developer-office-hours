# SPDX-License-Identifier: Apache-2.0

import omni.usd
from pxr import UsdGeom

stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath("/World/BasisCurves")
prim.GetAttribute("widths").Set([5, 10,5, 10,5, 10,5, 10,5, 10,5, 10,5])
curves: UsdGeom.BasisCurves = UsdGeom.BasisCurves(prim)
print(curves.GetWidthsInterpolation())