# SPDX-License-Identifier: Apache-2.0

import asyncio
from omni.kit.tool.collect.collector import Collector

async def collect_async(input_usd, output_dir, usd_only, flat_collection, mtl_only, prog_cb, finish_cb):
    """Collect input_usd related assets to output_dir.

    Args:
        input_usd (str): The usd stage to be collected.
        output_dir (str): The target dir to collect the usd stage to.
        usd_only (bool): Collects usd files only or not. It will ignore all asset types.
        flat_collection (bool): Collects stage without keeping the original dir structure.
        mtl_only (bool): Collects material and textures only or not. It will ignore all other asset types.
        prog_cb: Progress callback function
        finish_cb: Finish callback function
    """
    collector = Collector(input_usd, output_dir, usd_only, flat_collection, mtl_only)
    await collector.collect(prog_cb, finish_cb)
    
def finished():
    print("Finished!")

asyncio.ensure_future(collect_async(r"C:\temp\bookcase.usd", r"C:\temp\test_collect",
    False, False, False, None, finished))