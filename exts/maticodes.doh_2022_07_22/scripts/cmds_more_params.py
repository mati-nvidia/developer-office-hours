# SPDX-License-Identifier: Apache-2.0

import omni.kit.commands
from pxr import Gf, Usd

omni.kit.commands.execute('SetAnimCurveKey',
	paths=['/World/toy_drummer.xformOp:translate'],
	value=Gf.Vec3d(0.0, 0.0, 18))

omni.kit.commands.execute('SetAnimCurveKey',
	paths=['/World/toy_drummer.xformOp:translate'],
	value=Gf.Vec3d(0.0, 0.0, 24),
	time=Usd.TimeCode(72))

