# SPDX-License-Identifier: Apache-2.0

import argparse
import csv
from pathlib import Path


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Convert DOH CSV to MD")
    parser.add_argument(
        "csvfile", help="The CSV file to convert"
    )
    args = parser.parse_args()
    csvfile = Path(args.csvfile)
    mdfile = csvfile.with_suffix(".md")
    rows = []
    with open(csvfile) as f:
        with open(mdfile, "w") as out:
            for row in csv.reader(f):
                if row[2] and not row[5]:
                    out.write(f"1. [{row[1]}]({row[2]})\n")
            
    


    
    
    print("Success!")
