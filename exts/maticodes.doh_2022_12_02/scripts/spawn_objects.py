# SPDX-License-Identifier: Apache-2.0


import carb.events
import omni.kit.app
import omni.kit.commands
import logging

time_since_last_create = 0

update_stream = omni.kit.app.get_app().get_update_event_stream()

def on_update(e: carb.events.IEvent):
    global time_since_last_create
    carb.log_info(f"Update: {e.payload['dt']}")
    time_since_last_create += e.payload['dt']
    carb.log_info(f"time since: {time_since_last_create}")
    if time_since_last_create > 2:
        carb.log_info("Creating cube")
        omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
            prim_type='Cube')
        time_since_last_create = 0


sub = update_stream.create_subscription_to_pop(on_update, name="My Subscription Name")
sub = None