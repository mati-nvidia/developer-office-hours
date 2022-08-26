import omni.ui as ui

def next_num(n):
    while True:
        yield n
        n += 1

my_window = ui.Window("Example Window", width=300, height=300)
item_changed_sub = None
with my_window.frame:
    with ui.VStack():
        combo = ui.ComboBox(0, "Option1", "Option2", "Option3")
        # I'm just using this to generate unique data
        nums = next_num(0)

        def clicked():
            # clear the list
            items = combo.model.get_item_children()
            for item in items:
                combo.model.remove_item(item)
            
            # generate a new list
            for x in range(5):
                combo.model.append_child_item(None, ui.SimpleIntModel(next(nums)))

        ui.Button("Regenerate Combo", clicked_fn=clicked)