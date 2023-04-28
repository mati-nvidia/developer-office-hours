# SPDX-License-Identifier: Apache-2.0

# Docs: https://docs.omniverse.nvidia.com/kit/docs/omni.usd/latest/omni.usd/omni.usd.UsdContext.html#omni.usd.UsdContext.set_pickable

import omni.usd

ctx = omni.usd.get_context()
ctx.set_pickable("/", True)