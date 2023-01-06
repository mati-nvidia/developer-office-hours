# SPDX-License-Identifier: Apache-2.0

# This script is executed the first time the script node computes, or the next time it computes after this script
# is modified or the 'Reset' button is pressed.

# The following callback functions may be defined in this script:
#     setup(db): Called immediately after this script is executed
#     compute(db): Called every time the node computes (should always be defined)
#     cleanup(db): Called when the node is deleted or the reset button is pressed (if setup(db) was called before)

# Defining setup(db) and cleanup(db) is optional, but if compute(db) is not defined then this script node will run
# in legacy mode, where the entire script is executed on every compute and the callback functions above are ignored.

# Available variables:
#    db: og.Database The node interface, attributes are db.inputs.data, db.outputs.data.
#                    Use db.log_error, db.log_warning to report problems.
#                    Note that this is available outside of the callbacks only to support legacy mode.
#    og: The OmniGraph module

# Import statements, function/class definitions, and global variables may be placed outside of the callbacks.
# Variables may also be added to the db.internal_state state object.

# Example code snippet:

import math

UNITS = "cm"


def calculate_circumfrence(radius):
    return 2 * math.pi * radius


def setup(db):
    state = db.internal_state
    state.radius = 1


def compute(db):
    state = db.internal_state
    circumfrence = calculate_circumfrence(state.radius)
    print(f"{circumfrence} {UNITS}")
    print(f"My Input: {db.inputs.my_input}")
    db.outputs.foo = False
    state.radius += 1


# To see more examples, click on the Code Snippets button below.