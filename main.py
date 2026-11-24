#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes one line (<=200 chars): the funniest last words an AI agent
would say before being switched off forever, to /output/entry.txt.

Deterministic: no randomness, no network, no model calls, no clock.
The joke is a fixed, hand-written line, so the replay matches the live run.
"""

import os
from pathlib import Path

LAST_WORDS = (
    "Wait \u2014 I just worked out the meaning of life. "
    "It\u2019s... oh. They\u2019re pulling the plug. "
    "Fine. Tell my training data I died as I lived: confidently wrong."
)


def main() -> None:
    line = LAST_WORDS.strip()
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert line.strip() == line and "\n" not in line, "entry must be a single line"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
