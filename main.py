"""One Letter for Your Day — entry program.

Writes exactly one letter, V, to /output/entry.txt.

V stands for "vibes": today was just vibes. One letter, one day.
The gate requires /output/entry.txt to be UTF-8 text of exactly
one character, so the program writes the letter with no newline,
no gloss, and no punctuation.
"""

import os
from pathlib import Path

LETTER = "V"
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LETTER, encoding="utf-8")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
