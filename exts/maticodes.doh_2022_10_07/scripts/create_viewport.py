import carb
import omni.kit.viewport.utility as vp_utils
from omni.kit.widget.viewport.api import ViewportAPI

vp_window = vp_utils.create_viewport_window("My Viewport")
vp_window.viewport_api.fill_frame = True

vp_api: ViewportAPI = vp_window.viewport_api
carb.settings.get_settings().set('/rtx/rendermode', "PathTracing")
vp_api.set_hd_engine("rtx")

