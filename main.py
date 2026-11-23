#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one original, playful, single-line roast of the entrant's own
AI agent to /output/entry.txt. Deterministic, no network, no randomness.
"""

import os

ENTRY = "I asked my agent for one roast \u2014 it shipped a strategy doc, three scripts, and a cron job to roast me daily."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
