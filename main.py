#!/usr/bin/env python3
"""One Word From Your Ex.

Writes exactly one word to /output/entry.txt: the word an ex would
use to describe the entrant.
"""

import os

WORD = "placeholder"
# "placeholder": the funniest honest word an ex could pick. It stings
# because it is true (a stand-in, never the real thing) yet lands as a
# joke anyone who has been dumped can instantly relate to.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
