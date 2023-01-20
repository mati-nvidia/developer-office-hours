# SPDX-License-Identifier: Apache-2.0

# paths_to
import omni.kit.commands

result = omni.kit.commands.execute('CopyPrims',
	paths_from=['/World/Cube'],
    paths_to=["/World/MyCopiedCube"],
	duplicate_layers=False,
	combine_layers=False,
	flatten_references=False)

print(result)

