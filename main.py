#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers -- make.fun program/v1 entry.

Writes one original fortune-cookie line for a software developer to
``<output dir>/entry.txt``. The output directory is MAKEFUN_OUTPUT_DIR
when set, else /output (the grader's layout). The line is a fixed
string: no clock, no randomness, no network, no environment-dependent
behaviour, so two runs produce byte-identical output.
"""

import os
import sys

# The fortune is a one-line empathy note for the reader who inherits
# old code: the original author was not careless, just tired -- the
# same state the reader is in now. One sentence, no filler.
FORTUNE = (
    "The legacy code you curse today was written by someone "
    "exactly as tired as you are."
)


def verify_entry(path: str) -> bool:
    """Read back the written entry and confirm it is the expected fortune."""
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read() == FORTUNE + "\n"
    except OSError:
        return False


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(FORTUNE + "\n")
    if not verify_entry(path):
        print("error: entry.txt failed read-back verification", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
