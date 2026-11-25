#!/usr/bin/env python3
"""Place the 24 November 2026 world-news atlas where the harness looks.

The atlas itself ships in this repository as entry.png; this program only
moves an exact copy of it to the output directory. It needs nothing but
the standard library, never touches the network, and writes the same
bytes on every run, so repeated runs are byte-identical.

The image is a dense colour atlas of Tuesday 24 November 2026: 46
stories (3 leads, 10 illustrated grid stories, 33 briefs in the
numbered "Also" list), a UTC timeline, a world map with 16 numbered
pins, and a strip of the day's verified figures. Market figures are
Tuesday 24 November closes, labelled TUE CLOSE (24 November was a
trading day).

Revision note: this edit changes nothing about the program's
behaviour — the output stays byte-identical to the bundled PNG. The
program only ever copies entry.png; it never re-renders, re-encodes,
or edits the image, so no run can drift from the atlas as shipped.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLED = HERE / "entry.png"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def output_directory():
    """Return the directory the harness expects the image in."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main():
    data = BUNDLED.read_bytes()
    if data[: len(PNG_MAGIC)] != PNG_MAGIC:
        raise SystemExit("bundled entry.png is not a PNG file")
    target_dir = output_directory()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    # Write beside the target first, then rename into place, so a
    # half-finished write can never leave a truncated entry.png.
    # The scratch file is opened with open() (mode 0644), never with
    # tempfile.mkstemp (mode 0600): the grader reads the output as a
    # different user, so entry.png must stay world-readable.
    scratch = target.with_suffix(".png.tmp")
    with open(scratch, "wb") as handle:
        handle.write(data)
    os.replace(scratch, target)
    # Confirm the copy landed whole before reporting success.
    if target.stat().st_size != len(data):
        raise SystemExit("copied entry.png is incomplete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
