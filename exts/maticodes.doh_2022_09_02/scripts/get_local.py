import omni.usd
from pxr import Usd, Gf

stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath("/World/Cube_01")
scale, rotate, rot_order, translate = omni.usd.get_local_transform_SRT(prim, time=Usd.TimeCode.Default())
print(scale, rotate, rot_order, translate)

# Gf.Vec3d
# (Double, Double, Double)

# Gf.Matrix4d
# (Double, Double, Double, Double)
# (Double, Double, Double, Double)
# (Double, Double, Double, Double)
# (Double, Double, Double, Double)

matrix:Gf.Matrix4d = omni.usd.get_local_transform_matrix(prim, time_code=Usd.TimeCode.Default())
print(matrix)