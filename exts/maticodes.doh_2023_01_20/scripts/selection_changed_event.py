# SPDX-License-Identifier: Apache-2.0

import carb
import omni.usd

usd_ctx = omni.usd.get_context()

def on_selection_changed(event: carb.events.IEvent):
    print("Selection Changed")
    # https://docs.omniverse.nvidia.com/prod_kit/prod_kit/python-snippets/selection/get-current-selected-prims.html
    selection = usd_ctx.get_selection().get_selected_prim_paths()
    print(f"New selection: {selection}")

sel_sub = usd_ctx.get_stage_event_stream().create_subscription_to_pop_by_type(omni.usd.StageEventType.SELECTION_CHANGED, on_selection_changed)

# Don't forget to unsubscribe when you're done with it or when your extension shuts down.
sel_sub.unsubscribe()

