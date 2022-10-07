import omni.usd
from pxr import UsdGeom, Gf

stage = omni.usd.get_context().get_stage()
cube = stage.GetPrimAtPath("/World/Cube")

def print_pos(changed_path):
    print(changed_path)
    if changed_path.IsPrimPath():
        prim_path = changed_path
    else:
        prim_path = changed_path.GetPrimPath()
    prim = stage.GetPrimAtPath(prim_path)
    world_transform = omni.usd.get_world_transform_matrix(prim)
    translation: Gf.Vec3d = world_transform.ExtractTranslation()
    rotation: Gf.Rotation = world_transform.ExtractRotation()
    scale: Gf.Vec3d = Gf.Vec3d(*(v.GetLength() for v in world_transform.ExtractRotationMatrix()))
    print(translation, rotation, scale)
cube_move_sub = omni.usd.get_watcher().subscribe_to_change_info_path(cube.GetPath(), print_pos)