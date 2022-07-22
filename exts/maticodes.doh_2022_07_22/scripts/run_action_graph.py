# https://docs.omniverse.nvidia.com/py/kit/source/extensions/omni.graph/docs/index.html

import omni.graph.core as og

keys = og.Controller.Keys
og.Controller.edit("/World/ActionGraph", { keys.SET_VALUES: ("/World/ActionGraph/on_impulse_event.state:enableImpulse", True) })

