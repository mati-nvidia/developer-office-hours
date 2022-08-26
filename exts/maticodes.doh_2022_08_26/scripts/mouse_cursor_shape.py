####################################
# MUST ENABLE omni.kit.window.cursor
####################################

import carb
import omni.kit.window.cursor

cursor = omni.kit.window.cursor.get_main_window_cursor()
# OPTIONS:
# carb.windowing.CursorStandardShape.ARROW
# carb.windowing.CursorStandardShape.IBEAM
# carb.windowing.CursorStandardShape.VERTICAL_RESIZE
# carb.windowing.CursorStandardShape.HORIZONTAL_RESIZE
# carb.windowing.CursorStandardShape.HAND
# carb.windowing.CursorStandardShape.CROSSHAIR
cursor.override_cursor_shape(carb.windowing.CursorStandardShape.CROSSHAIR)

# clear back to arrow
cursor.clear_overridden_cursor_shape()