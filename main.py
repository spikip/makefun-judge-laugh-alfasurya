"""Entry for the make.fun bounty "Make the AI Judge Laugh".

The program writes a single office-life joke to /output/entry.txt.
The joke is a trust-fall team building exercise where nobody catches
the faller, and HR rebrands the failure as a valuable lesson in
self-reliance. It is true to office life: the trust fall, the empty
hands, and the HR spin are all recognisable at once, and the laugh
comes from how fast the corporate language papers over the disaster.
The observation is the setup, the HR line is the turn, and the whole
thing fits in one line that needs no explanation — the spin is the
joke, not the fall. The gate allows 1
to 200 characters of UTF-8 text, so the line is checked against
that cap before it is written.
"""

import os

ENTRY = (
    "Our team building exercise was trust falls. I fell. Nobody caught "
    "me. HR called it a valuable lesson in self-reliance."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
