"""Entry for make.fun bounty: Make the AI Judge Laugh: Office Jokes.

Writes one single-line office joke to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
from pathlib import Path

LINE = "The meeting could have been an email, the email could have been one sentence, and the sentence was just: 'Per my last email \u2014 no.'"
MAX_CHARS = 199


def write_entry(out_dir):
    """Validate the entry line and write it with no trailing newline."""
    if not LINE or not LINE.strip():
        raise ValueError("entry must be non-empty")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if len(LINE) > MAX_CHARS:
        raise ValueError("entry exceeds the character limit")
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
