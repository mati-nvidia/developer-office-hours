import omni.kit.context_menu

def show_menu(objects):
    print("show it?")
    return True

def hello_world(objects):
    print(f"Hello Objects: {objects}")

menu_item_config = {
    "name": "Hello World!",
    "glyph": "menu_search.svg",
    "show_fn": [show_menu],
    "onclick_fn": hello_world,
}

# You must keep a reference to the menu item. Set this variable to None to remove the item from the menu
hello_world_menu_item = omni.kit.context_menu.add_menu(menu_item_config, "MENU", "omni.kit.window.viewport")
hello_world_menu_item = None