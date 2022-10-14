# SPDX-License-Identifier: Apache-2.0

import omni.kit.ui

menu_path = "File/Foo"
menu_path2 = "File/Foo/Bar"

def on_menu_click(menu_path, toggled):
    print(menu_path)
    print(toggled)

menu = omni.kit.ui.get_editor_menu().add_item(menu_path, on_menu_click)
menu = omni.kit.ui.get_editor_menu().add_item(menu_path2, on_menu_click, True)

omni.kit.ui.get_editor_menu().remove_item(menu)


import omni.kit.menu.utils
from omni.kit.menu.utils import MenuItemDescription

menu_item = MenuItemDescription(
    name="Hello World!",
    glyph="save.svg",
    onclick_fn=lambda: print("Hello World!"),
    # hotkey=(
    #    carb.input.KEYBOARD_MODIFIER_FLAG_CONTROL | carb.input.KEYBOARD_MODIFIER_FLAG_ALT,
    #    carb.input.KeyboardInput.S,
    #),
)
menus = [menu_item]
omni.kit.menu.utils.add_menu_items([menu_item], "File")

omni.kit.menu.utils.remove_menu_items([menu_item], "File", rebuild_menus=True)

# omni.kit.ui.get_editor_menu().convert_to_new_menu

