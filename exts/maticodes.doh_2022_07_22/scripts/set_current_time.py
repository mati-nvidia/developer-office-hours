# https://docs.omniverse.nvidia.com/py/kit/source/extensions/omni.timeline/docs/index.html

import omni.timeline
timeline = omni.timeline.get_timeline_interface()
# set in using seconds
timeline.set_current_time(1)

# set using frame number
fps = timeline.get_time_codes_per_seconds()
timeline.set_current_time(48 / fps)

