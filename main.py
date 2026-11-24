"""Everyday Things, Two Lines — entrypoint.

Writes a two-line explanation of a zipper to /output/entry.txt.

Line 1 explains the everyday thing to a 10-year-old in one vivid
sentence built on a single analogy (a row of tiny teeth holding hands).
Line 2 says why the analogy works: what it maps (teeth locking
together, the slider pulling them shut or apart) and what it leaves
out (real teeth chew and grow back; a zipper's teeth only hold on
and never let go by themselves).

Standard library only. No network, no files outside this repo.
"""

import os
from pathlib import Path

ENTRY = (
    "A zipper is a row of tiny teeth holding hands so tight your jacket stays shut.\n"
    "The teeth really do lock together and the slider pulls them shut or apart, "
    "but real teeth chew and grow back, while a zipper's teeth only hold on "
    "and never let go by themselves.\n"
)


def main() -> None:
    # Self-check against the sealed gate: UTF-8 text, 1 to 400 chars,
    # not only whitespace, exactly two non-empty lines.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars, gate is 1-400"
    lines = text.splitlines()
    assert len(lines) == 2, f"expected 2 lines, got {len(lines)}"
    assert all(line.strip() for line in lines)
    out_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} chars to {out_path}")


if __name__ == "__main__":
    main()
