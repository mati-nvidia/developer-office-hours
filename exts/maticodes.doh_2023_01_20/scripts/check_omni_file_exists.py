# SPDX-License-Identifier: Apache-2.0

import omni.client

result, list_entry = omni.client.stat("omniverse://localhost/Users/test/helloworld_py.usd")
if result == omni.client.Result.OK:
    # Do things
    print(list_entry)

# When a file doesn't exist, the result is omni.client.Result.ERROR_NOT_FOUND
result, list_entry = omni.client.stat("omniverse://localhost/Users/test/fake.usd")
print(result, list_entry)