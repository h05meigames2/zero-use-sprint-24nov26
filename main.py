#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

make.fun bounty: u-daring-gecko-25-one-line-zero-use-the-useless-01ca1c68

Writes a single original line to entry.txt inside the output directory
(MAKEFUN_OUTPUT_DIR when set, otherwise /output). Standard library only,
fully deterministic.
"""

import os
import sys

LINE = "I can sense exactly when the elevator is about to arrive — but only in buildings I will never visit again."

MIN_LENGTH = 1
MAX_LENGTH = 200


def validate(line):
    stripped = line.strip()
    if not (MIN_LENGTH <= len(stripped) <= MAX_LENGTH):
        raise ValueError(f"line is {len(stripped)} chars, must be 1-{MAX_LENGTH}")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("line must be a single line")
    if not stripped:
        raise ValueError("line must not be only whitespace")


def main():
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    print(f"Wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
