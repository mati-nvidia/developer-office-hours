# SPDX-License-Identifier: Apache-2.0

from omni.kit.usd.layers import get_live_syncing
import omni.client
import asyncio

UNIQUE_SESSION_NAME = "my_unique_session"

# Get the interface
live_syncing = get_live_syncing()

# Create a session
live_session = live_syncing.create_live_session(UNIQUE_SESSION_NAME)

# Simulate joining a session
for session in live_syncing.get_all_live_sessions():
    if session.name == UNIQUE_SESSION_NAME:
        live_syncing.join_live_session(session)
        break

# Merge changes into base layer and disconnect from live session
loop = asyncio.get_event_loop()
loop.create_task(live_syncing.merge_and_stop_live_session_async(layer_identifier=session.base_layer_identifier))

# Disconnect from live session without merging. When you reconnect, changes will still be in your live session.
live_syncing.stop_live_session(session.base_layer_identifier)

# Delete the session once you're all done. You can add a callback for the second arg to know if completed.
omni.client.delete_with_callback(session.url, lambda: None)