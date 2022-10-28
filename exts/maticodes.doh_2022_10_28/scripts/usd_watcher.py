# SPDX-License-Identifier: Apache-2.0

import omni.usd
from pxr import Gf

stage = omni.usd.get_context().get_stage()
cube = stage.GetPrimAtPath("/World/Cube")

def print_size(changed_path):
    print("Size Changed:", changed_path)

def print_pos(changed_path):
    print(changed_path)
    if changed_path.IsPrimPath():
        prim_path = changed_path
    else:
        prim_path = changed_path.GetPrimPath()
    
    prim = stage.GetPrimAtPath(prim_path)
    local_transform = omni.usd.get_local_transform_SRT(prim)
    print("Translation: ", local_transform[3])

def print_world_pos(changed_path):
    world_transform: Gf.Matrix4d = omni.usd.get_world_transform_matrix(prim)
    translation: Gf.Vec3d = world_transform.ExtractTranslation()
    print(translation)

size_attr = cube.GetAttribute("size")
cube_sub = omni.usd.get_watcher().subscribe_to_change_info_path(cube.GetPath(), print_world_pos)
cube_size_sub = omni.usd.get_watcher().subscribe_to_change_info_path(size_attr.GetPath(), print_size)
cube_sub = None
cube_size_sub = None