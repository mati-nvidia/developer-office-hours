
# SPDX-License-Identifier: Apache-2.0

# Docs: https://docs.omniverse.nvidia.com/prod_kit/prod_kit/programmer_ref/usd/properties/create-attribute.html

import omni.usd
from pxr import Usd, Sdf

stage = omni.usd.get_context().get_stage()
prim: Usd.Prim = stage.GetPrimAtPath("/World/Cylinder")
attr: Usd.Attribute = prim.CreateAttribute("mySecondAttr", Sdf.ValueTypeNames.Bool)
attr.Set(False)
