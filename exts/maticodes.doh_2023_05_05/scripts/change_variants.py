# SPDX-License-Identifier: Apache-2.0

from pxr import Usd, UsdGeom
import omni.usd

stage = omni.usd.get_context().get_stage()
world_prim = stage.GetPrimAtPath("/World")
vset = world_prim.GetVariantSets().AddVariantSet('shapes')
vset.AddVariant('cube')
vset.AddVariant('sphere')
vset.AddVariant('cone')
vset.SetVariantSelection('cube')
with vset.GetVariantEditContext():
    UsdGeom.Cube.Define(stage, "/World/Cube")

vset.SetVariantSelection('sphere')
with vset.GetVariantEditContext():
    UsdGeom.Sphere.Define(stage, "/World/Sphere")

vset.SetVariantSelection('cone')
with vset.GetVariantEditContext():
    UsdGeom.Cone.Define(stage, "/World/Cone")



stage = omni.usd.get_context().get_stage()
world_prim = stage.GetPrimAtPath("/World")
vsets = world_prim.GetVariantSets()
vset = vsets.GetVariantSet("shapes")
vset.SetVariantSelection("cone")