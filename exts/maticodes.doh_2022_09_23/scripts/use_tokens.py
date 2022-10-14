# SPDX-License-Identifier: Apache-2.0
# https://docs.omniverse.nvidia.com/py/kit/docs/guide/tokens.html

import carb.tokens
from pathlib import Path

path = Path("${shared_documents}") / "maticodes.foo"
resolved_path = carb.tokens.get_tokens_interface().resolve(str(path))
print(resolved_path)