"""
https://docs.omniverse.nvidia.com/py/kit/source/extensions/omni.graph/docs/index.html
https://docs.omniverse.nvidia.com/py/kit/source/extensions/omni.graph/docs/controller.html#howto-omnigraph-controller
"""

import omni.graph.core as og
controller: og.Controller = og.Controller()
keys = og.Controller.Keys

# Create an Action Graph
# SPDX-License-Identifier: Apache-2.0

graph = controller.create_graph({
    "graph_path": "/World/CameraAim",
    "evaluator_name": "execution" # This makes it Action Graph
})

# Create some nodes
_, nodes, _, _ = controller.edit(graph, {keys.CREATE_NODES: ("OnTick", "omni.graph.action.OnTick")})
on_tick = nodes[0]
_, nodes, _, _ = controller.edit(graph, {keys.CREATE_NODES: ("SetCameraTarget", "omni.graph.ui.SetCameraTarget")})
set_cam_target = nodes[0]

# Edit an attribute
# /World/CameraAim/OnTick.inputs:onlyPlayback
controller.edit(graph, {keys.SET_VALUES: (on_tick.get_attribute("inputs:onlyPlayback"), False)})

# Connect two attributes
controller.connect(on_tick.get_attribute("outputs:tick"), set_cam_target.get_attribute("inputs:execIn"))
