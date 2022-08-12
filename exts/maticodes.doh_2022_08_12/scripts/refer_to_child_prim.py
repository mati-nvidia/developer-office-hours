# https://docs.omniverse.nvidia.com/prod_usd/prod_usd/quick-start/hierarchy.html

import omni.usd

stage = omni.usd.get_context().get_stage()
starting_prim = stage.GetPrimAtPath("/World/New")
for shape in starting_prim.GetChildren():
    print(shape)
    for shape_child in shape.GetChildren():
        print(shape_child)


for prim in stage.Traverse():
    print(prim)
