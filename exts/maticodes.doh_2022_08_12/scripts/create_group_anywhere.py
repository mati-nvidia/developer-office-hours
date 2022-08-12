from pxr import Sdf
import omni.kit.commands
import omni.usd

stage = omni.usd.get_context().get_stage()

children = []
for i in range(3):
    child = omni.usd.get_stage_next_free_path(stage, "/World/Cube", prepend_default_prim=False)
    children.append(child)
    omni.kit.commands.execute("CreatePrim", prim_type="Cube", prim_path=child)

group_path = Sdf.Path("/World/New/Hello")
omni.kit.commands.execute("CreatePrimWithDefaultXformCommand", prim_type="Scope", prim_path=str(group_path))
for child in children:
    prim = stage.GetPrimAtPath(child)
    name = prim.GetName()
    omni.kit.commands.execute("MovePrim", path_from=child, path_to=group_path.AppendPath(name))
