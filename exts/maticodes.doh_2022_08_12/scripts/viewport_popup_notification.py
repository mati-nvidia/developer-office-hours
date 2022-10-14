# SPDX-License-Identifier: Apache-2.0
# https://docs.omniverse.nvidia.com/py/kit/source/extensions/omni.kit.notification_manager/docs/index.html?highlight=omni%20kit%20notification_manager#
import carb


def clicked_ok():
    carb.log_info("User clicked ok")


def clicked_cancel():
    carb.log_info("User clicked cancel")


import omni.kit.notification_manager as nm

ok_button = nm.NotificationButtonInfo("OK", on_complete=clicked_ok)
cancel_button = nm.NotificationButtonInfo("CANCEL", on_complete=clicked_cancel)
notification_info = nm.post_notification(
    "Notification Example",
    hide_after_timeout=False,
    duration=0,
    status=nm.NotificationStatus.WARNING,
    button_infos=[ok_button, cancel_button],
)
