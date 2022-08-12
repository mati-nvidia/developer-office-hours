from pxr import Usd, UsdGeom
import omni.usd

stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath("/World/New/Hello")
print(prim)
print(prim.IsValid())

prim = stage.GetPrimAtPath("/World/New/Fake")
print(prim)
print(prim.IsValid())
