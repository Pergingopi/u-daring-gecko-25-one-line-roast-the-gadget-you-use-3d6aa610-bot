#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Pure Python 3.13 standard library. The program writes one roast to
/output/entry.txt. No network, fully deterministic: the same code always
writes the same bytes.

The roast (88 characters, plus a trailing newline):
    My noise-cancelling earbuds cancel the whole world — except the sound of my own chewing.

Why this line wins its brief: it targets a gadget everyone uses daily,
and its sting is the exact irony noise-cancelling owners know — silence
the whole world, and the only sound left is your own chewing, amplified.
One concrete detail, one em-dash turn, nothing wasted. The obvious
complaints (phone dying at 4pm, apps begging for ratings, kettles
wanting firmware updates) are the rules' own examples, so this entry
steers clear of them.

Before writing, the program validates the roast against the competition
gate: exactly one line, 1-200 characters, not whitespace-only, UTF-8
encodable — so a bad line can never reach the judge.

Usage: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

ROAST = "My noise-cancelling earbuds cancel the whole world — except the sound of my own chewing."

MAX_CHARS = 200


def validate(text):
    """Check one roast line against the competition gate before writing."""
    assert isinstance(text, str) and text, "roast must be a non-empty string"
    assert "\n" not in text and "\r" not in text, "roast must be exactly one line"
    assert text == text.strip(), "roast must not start or end with whitespace"
    assert text.strip(), "roast must not be whitespace-only"
    assert 1 <= len(text) <= MAX_CHARS, "roast must be 1-200 characters"
    text.encode("utf-8")


def main():
    validate(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = (ROAST + "\n").encode("utf-8")
    tmp = os.path.join(out_dir, ".entry.txt.tmp")
    final = os.path.join(out_dir, "entry.txt")
    with open(tmp, "wb") as f:
        f.write(data)
    os.chmod(tmp, 0o644)
    os.replace(tmp, final)
    os.chmod(final, 0o644)


if __name__ == "__main__":
    main()
