#!/usr/bin/env python3
"""Write one funny line answering the robot-vacuum excuse prompt to /output/entry.txt.

The line is written exactly as given: 87 Unicode code points,
inside the competition gate of 1-200. Python 3, standard library
only, no network.
"""

import os

TEXT = "I am a vacuum. The sock was on the floor. This is not a crime, it is a job description."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
