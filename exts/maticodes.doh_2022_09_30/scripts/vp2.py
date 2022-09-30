
# DON'T DO THIS ANYMORE
import omni.kit.viewport_legacy
viewport_interface = omni.kit.viewport_legacy.acquire_viewport_interface()
vp_win = viewport_interface.get_viewport_window()
print(vp_win)

# DO THIS
import omni.kit.viewport.utility as vp_util
vp_win = vp_util.get_active_viewport_window()
print(vp_win)

