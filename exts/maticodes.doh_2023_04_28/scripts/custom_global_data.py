# SPDX-License-Identifier: Apache-2.0

import omni.usd

stage = omni.usd.get_context().get_stage()
layer = stage.GetRootLayer()
print(type(layer))
layer.SetCustomLayerData({"Hello": "World"})


stage.DefinePrim("/World/Hello", "HelloWorld")
stage.DefinePrim("/World/MyTypeless")