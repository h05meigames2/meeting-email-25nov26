#!/usr/bin/env python3
"""Entry for the make.fun bounty "The Meeting That Should Have Been an Email".

Writes a single one-line joke about a meeting that should have been an email
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt). The joke's
punch lands in the last words: after an hour of reading the email aloud and
a follow-up to interpret it, nobody has actually read it yet.

Deterministic, stdlib only, no network, no randomness.
"""

import os

LINE = (
    "We spent an hour in a meeting reading the email out loud, then booked "
    "a follow-up to decide what it meant \u2014 nobody has actually read it yet."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
