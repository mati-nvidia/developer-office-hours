# SPDX-License-Identifier: Apache-2.0

import omni.kit.commands
from pxr import Sdf

omni.kit.commands.execute('LockSpecs',
	spec_paths=['/Desk'],
	hierarchy=False)