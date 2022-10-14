# SPDX-License-Identifier: Apache-2.0

import argparse
import shutil
import os
from pathlib import Path

SOURCE_PATH = Path(__file__).parent / "template" / "maticodes.doh_YYYY_MM_DD"


def text_replace(filepath, tokens_map):
    with open(filepath, "r") as f:
        data = f.read()
        for token, fstring in tokens_map.items():
            data = data.replace(token, fstring)
    
    with open(filepath, "w") as f:
        f.write(data)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Create folder link to Kit App installed from Omniverse Launcher")
    parser.add_argument(
        "date", help="The dates of the Office Hour in YYYY-MM-DD format."
    )
    args = parser.parse_args()
    year, month, day = args.date.split("-")

    # copy files
    dest_path = Path(__file__).parent / "../.." / f"exts/maticodes.doh_{year}_{month}_{day}"
    shutil.copytree(SOURCE_PATH, dest_path)
    
    # rename folders
    template_ext_folder = dest_path / "maticodes" / "doh_YYYY_MM_DD"
    ext_folder = dest_path / "maticodes" / f"doh_{year}_{month}_{day}"
    os.rename(template_ext_folder, ext_folder)

    tokens_map = {
        "[DATE_HYPHEN]": f"{year}-{month}-{day}",
        "[DATE_UNDERSCORE]": f"{year}_{month}_{day}",
        "[DATE_PRETTY]": f"{month}/{day}/{year}",
    }

    # text replace extension.toml
    ext_toml = dest_path / "config" / "extension.toml"
    text_replace(ext_toml, tokens_map)

    # text replace README
    readme = dest_path / "docs" / "README.md"
    text_replace(readme, tokens_map)

    # text replace extension.py
    ext_py = ext_folder / "extension.py"
    text_replace(ext_py, tokens_map)
    
    print("Success!")
