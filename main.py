#!/usr/bin/env python3
"""Publish the 24 November 2026 news atlas image.

The finished picture is made ahead of time and travels with this entry as
``entry.png``.  This program is only the courier: it checks the bundled
picture is a genuine PNG, carries it into the output directory the harness
points at, and then reads the delivered copy back to prove it arrived
whole.  Nothing is downloaded, nothing is re-rendered, and the result is
identical on every run.

How to check it by hand: run the script twice with different output
directories and compare the two delivered files with ``md5sum`` — both
must match the bundled ``entry.png`` byte for byte, and each delivered
file must carry mode 644.  The script performs the same comparison
itself on every run, so a silent partial write can never pass as success.
"""

import hashlib
import os
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
BUNDLED_NAME = "entry.png"


def pick_output_dir():
    """Return the harness output directory, honouring its env vars."""
    for variable in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        chosen = os.environ.get(variable)
        if chosen:
            return chosen
    return "/output"


def digest(data):
    """Return the hex SHA-256 of a bytes object."""
    return hashlib.sha256(data).hexdigest()


def load_bundled_picture():
    """Read the bundled PNG next to this script and sanity-check it."""
    here = os.path.dirname(os.path.abspath(__file__))
    bundled_path = os.path.join(here, BUNDLED_NAME)
    try:
        with open(bundled_path, "rb") as handle:
            picture = handle.read()
    except OSError as exc:
        raise SystemExit("cannot read bundled %s: %s" % (BUNDLED_NAME, exc))
    if not picture.startswith(PNG_SIGNATURE):
        raise SystemExit("bundled %s lacks the PNG magic bytes" % BUNDLED_NAME)
    if not picture:
        raise SystemExit("bundled %s is empty" % BUNDLED_NAME)
    return picture


def deliver(picture, out_dir):
    """Write the picture atomically into out_dir as entry.png (mode 644)."""
    os.makedirs(out_dir, exist_ok=True)
    final_path = os.path.join(out_dir, BUNDLED_NAME)
    staging_path = "%s.tmp-%d" % (final_path, os.getpid())
    try:
        with open(staging_path, "wb") as handle:
            handle.write(picture)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(staging_path, 0o644)
        os.replace(staging_path, final_path)
    except OSError as exc:
        try:
            os.unlink(staging_path)
        except OSError:
            pass
        raise SystemExit("cannot deliver %s: %s" % (BUNDLED_NAME, exc))
    try:
        with open(final_path, "rb") as handle:
            delivered = handle.read()
    except OSError as exc:
        raise SystemExit("cannot read back delivered %s: %s" % (BUNDLED_NAME, exc))
    if delivered != picture:
        raise SystemExit("delivered copy differs from the bundled picture")
    if digest(delivered) != digest(picture):
        raise SystemExit("delivered copy hash mismatch")
    return final_path


def main():
    picture = load_bundled_picture()
    out_dir = pick_output_dir()
    final_path = deliver(picture, out_dir)
    print(
        "wrote %s (%d bytes, sha256 %s)"
        % (final_path, len(picture), digest(picture))
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
