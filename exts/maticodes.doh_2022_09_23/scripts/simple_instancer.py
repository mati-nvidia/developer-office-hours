import omni.usd
from pxr import Usd, UsdGeom, Sdf, Gf


stage: Usd.Stage = omni.usd.get_context().get_stage()
prim_path = Sdf.Path("/World/MyInstancer")
instancer: UsdGeom.PointInstancer = UsdGeom.PointInstancer.Define(stage, prim_path)
proto_container = UsdGeom.Scope.Define(stage, prim_path.AppendPath("Prototypes"))
shapes = []
shapes.append(UsdGeom.Cube.Define(stage, proto_container.GetPath().AppendPath("Cube")))
shapes.append(UsdGeom.Sphere.Define(stage, proto_container.GetPath().AppendPath("Sphere")))
shapes.append(UsdGeom.Cone.Define(stage, proto_container.GetPath().AppendPath("Cone")))
instancer.CreatePositionsAttr([Gf.Vec3f(0, 0, 0), Gf.Vec3f(2, 0, 0), Gf.Vec3f(4, 0, 0)])
instancer.CreatePrototypesRel().SetTargets([shape.GetPath() for shape in shapes])
instancer.CreateProtoIndicesAttr([0, 1, 2])