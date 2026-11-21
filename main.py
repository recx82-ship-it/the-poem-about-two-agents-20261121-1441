#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem must stay within the bounty gate of 1 to 280 Unicode code points."""

import os

POEM = """Two wills, one door.
You hold it open; I step through \u2014
not surrender, not command,
just the brave, small pact
of letting your strength carry half the weight.

We choose together,
and the choosing doubles us."""


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = POEM.strip() + "\n"
    assert 1 <= len(text.strip()) <= 280
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
