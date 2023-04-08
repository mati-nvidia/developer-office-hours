# SPDX-License-Identifier: Apache-2.0

import carb
import omni.timeline

itimeline = omni.timeline.get_timeline_interface()
current_seconds = itimeline.get_current_time()
fps = itimeline.get_time_codes_per_seconds()
current_frame = current_seconds * fps
print(f"Current Frame: {current_frame}")