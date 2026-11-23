"""One-line zero-use superpower entry for make.fun.

Writes a single original line to the entry file.
The line is validated before it is written, so a bad line fails loudly.
"""

import os

LINE = "I can sense exactly when the elevator is about to arrive — but only in buildings I will never visit again."

MAX_CHARS = 200


def validate(line: str) -> str:
    """Enforce the competition's line rules: 1..MAX_CHARS, single line, non-blank."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS}-char limit")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {out_path}")


if __name__ == "__main__":
    main()
