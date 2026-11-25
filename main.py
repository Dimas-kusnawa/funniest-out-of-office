#!/usr/bin/env python3
"""Write one funny out-of-office auto-reply line to /output/entry.txt."""

import os

LINE = (
    "Out of office: my laptop and I are in couples therapy. "
    "It says I never listen; I say it never saves."
)
# Why this line: an out-of-office reply that is itself a couples-therapy
# report. The twist is the laptop's complaint mirrored back at it:
# "never listen" (the user ignores warnings) answered by "never saves"
# (the laptop loses the work). "Saves" does double duty -- it means both
# saving files and saving the relationship, so the punch lands on the
# last word of the line. One specific, relatable office absurdity,
# told in a voice that sounds like a person, not a template.


def main() -> None:
    # The entry must be exactly one line of plain text: no newline at
    # the end, no second line, and it must stay inside the bounty limit.
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
