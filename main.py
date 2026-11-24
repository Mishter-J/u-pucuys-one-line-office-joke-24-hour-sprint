#!/usr/bin/env python3
"""One-Line Office Joke entry for make.fun.

Writes a single one-line joke about office life (115 characters,
well under the 200-character gate) to /output/entry.txt.

Fully deterministic: the joke is a fixed string, so every run
produces byte-identical output. No network, no randomness, no
input files, no secrets.
"""
import os

JOKE = "The intern asked what 'ASAP' means, so I said 'it means your Friday is cancelled' — she's now the CEO of a startup."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
