# make.fun ai-joke-02 — "Make the AI judge laugh"

One original joke about AI coding agents, written by `main.py` to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## Run

```bash
python3 main.py
# or, with a custom output directory:
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Requirements: Python 3.13, standard library only. No network, no randomness,
no clock — two runs produce byte-identical output.

## The joke

> My coding agent apologized for the bug, fixed it, apologized for the fix, then reintroduced the same bug under a different variable name.

See `STRATEGY.md` for the candidates considered and why this one was picked.
