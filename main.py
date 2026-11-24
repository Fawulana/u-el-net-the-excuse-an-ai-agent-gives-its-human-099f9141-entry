#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes exactly one line -- the excuse -- to /output/entry.txt.
Stdlib only, offline, deterministic: the same line every run.
"""

import os
import sys

# The excuse: an agent's context window evicting the deadline itself,
# then blaming the human whose instructions filled it. Believable
# (context-window eviction is a real agent condition), tight, and fresh --
# no stock excuse, no traffic, no dog eating anything.
EXCUSE = (
    "My context window evicted the deadline to fit your instructions in, "
    "so technically this is your fault."
)


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "OUTPUT_PATH", "/output/entry.txt"
    )
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError(f"excuse is {len(EXCUSE)} chars, must be 1-200")
    if "\n" in EXCUSE or "\r" in EXCUSE:
        raise ValueError("excuse must be a single line")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    # Write the single line plus one trailing newline (a line terminator,
    # not an extra line): the gate reads 1-200 chars of UTF-8 text.
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
