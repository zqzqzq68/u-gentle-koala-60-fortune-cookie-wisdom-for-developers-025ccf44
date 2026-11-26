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

FORTUNE = (
    "The legacy code you curse today was written by someone "
    "exactly as tired as you are."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(FORTUNE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
