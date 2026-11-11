"""make.fun ai-joke-02 entry: one original joke about AI coding agents.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output),
UTF-8, one line, deterministic (same bytes on every run).
Python 3.13, standard library only. No network, no randomness, no clock.
"""

import os

JOKE = (
    "My coding agent apologized for the bug, fixed it, apologized for the fix, "
    "then reintroduced the same bug under a different variable name."
)

assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
