# SPDX-License-Identifier: Apache-2.0

import carb.events
import omni.kit.app

MY_CUSTOM_EVENT = carb.events.type_from_string("omni.my.extension.MY_CUSTOM_EVENT")

bus = omni.kit.app.get_app().get_message_bus_event_stream()
bus.push(MY_CUSTOM_EVENT, payload={"prim_path": "/World/Cube", "x": 1})