# SPDX-License-Identifier: Apache-2.0

import omni.kit.viewport.utility as vu
from pxr import Sdf

vp_api = vu.get_active_viewport()
vp_api.camera_path = "/World/Camera_01"
