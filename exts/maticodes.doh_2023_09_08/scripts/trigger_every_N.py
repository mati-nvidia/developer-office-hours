
# App/Subscribe to Update Events
import carb.events
import omni.kit.app
import omni.timeline

update_stream  = omni.kit.app.get_app().get_update_event_stream()

every_N = 5 # seconds
elapsed = 0
update_sub = None

def on_update(e: carb.events.IEvent):
    global elapsed
    elapsed += e.payload["dt"]
    if elapsed >= every_N:
        print(f"{every_N} seconds have passed. Fire!")
        elapsed = 0
    # print(f"Update: {elapsed}")


def on_play(e: carb.events.IEvent):
    global update_sub
    update_sub = update_stream.create_subscription_to_pop(on_update, name="My Subscription Name")

def on_stop(e: carb.events.IEvent):
    global update_sub
    update_sub = None

itimeline: omni.timeline.ITimeline = omni.timeline.get_timeline_interface()
play_sub = itimeline.get_timeline_event_stream().create_subscription_to_pop_by_type(omni.timeline.TimelineEventType.PLAY, on_play)
stop_sub = itimeline.get_timeline_event_stream().create_subscription_to_pop_by_type(omni.timeline.TimelineEventType.STOP, on_stop)

# Remember to unsub by setting variables to None.
update_sub = None
play_sub = None
stop_sub = None