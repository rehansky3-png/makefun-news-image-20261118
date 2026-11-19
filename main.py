#!/usr/bin/env python3
"""Publish the 18 November 2026 front page.

The artwork itself — a 1024x1024 PNG newspaper page titled "THE WORLD —
WEDNESDAY 18 NOVEMBER 2026" — sits beside this script as entry.png.
This script does nothing creative: it checks the picture is present and
within the competition's size cap, then places an exact copy of it in the
output directory so the harness can collect it. Running it twice over the
same entry.png always yields the same bytes.
"""

import os
import shutil
import sys

# Where the picture lives: the same folder as this script.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PICTURE_NAME = "entry.png"

# Competition cap: the front page must fit in one mebibyte.
SIZE_CAP = 1024 * 1024

# The harness tells us where to put the result; fall back to /output.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def fail(message):
    """Print an error and stop with a non-zero exit code."""
    print("news-image-20261118: " + message, file=sys.stderr)
    raise SystemExit(1)


def publish():
    picture_path = os.path.join(SCRIPT_DIR, PICTURE_NAME)

    if not os.path.isfile(picture_path):
        fail(
            "entry.png is missing — expected it at %s; nothing to publish."
            % picture_path
        )

    picture_bytes = os.path.getsize(picture_path)
    if picture_bytes > SIZE_CAP:
        fail(
            "entry.png is %d bytes, over the %d-byte limit."
            % (picture_bytes, SIZE_CAP)
        )

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    destination = os.path.join(OUTPUT_DIR, PICTURE_NAME)
    shutil.copyfile(picture_path, destination)
    print("Published %s (%d bytes) to %s" % (PICTURE_NAME, picture_bytes, destination))


if __name__ == "__main__":
    publish()
