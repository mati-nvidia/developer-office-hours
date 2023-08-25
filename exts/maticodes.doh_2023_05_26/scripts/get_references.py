# SPDX-License-Identifier: Apache-2.0

import omni.usd

stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath("/World/Xform")
refs = prim.GetMetadata("references").ApplyOperations([])
for ref in refs:
	print(ref.primPath)
	print(ref.assetPath)
