"""One-line office joke entry for make.fun bounty
u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.

Writes exactly one single-line joke about office life to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
one line, 1-200 characters, no trailing newline, deterministic.
"""

import os

JOKE = (
    "I set my out-of-office to 'on annual leave' and my manager "
    "replied asking if I could still join the 9am call."
)

MAX_CHARS = 200


def validate(text):
    """Check the joke meets the gate: 1-200 chars, single line,
    not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("joke must be a string")
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("joke is %d chars, over the 200-char cap" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    return text


def output_path():
    """Resolve the output file path from MAKEFUN_OUTPUT_DIR,
    defaulting to /output as the bounty requires."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(text, path):
    """Write the validated joke to path as UTF-8, exactly as-is:
    no trailing newline, no extra bytes."""
    validate(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return path


def main():
    path = output_path()
    write_entry(JOKE, path)
    print("Wrote %d chars to %s" % (len(JOKE), path))


if __name__ == "__main__":
    main()
