#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes the chosen one-sentence review to entry.txt: a one-star review
of Earth by an alien tourist that still compliments the food.
Standard library only; deterministic — every run writes the same bytes.
"""

import os

TEXT = (
    "One star: Earth's gravity dragged my third eye shut by noon and the "
    "locals queue politely for misery, but the ramen broth alone was worth "
    "the nine-light-year flight."
)


def verify_written_bytes(path):
    """Read the file back and compare it byte-for-byte with TEXT.

    The comparison is done on the SHA-256 digest of the landed bytes
    and raises SystemExit on mismatch, so the check also holds under
    `python -O` (where plain asserts are stripped).
    """
    import hashlib

    with open(path, "rb") as fh:
        data = fh.read()
    landed = hashlib.sha256(data).hexdigest()
    expected = hashlib.sha256(TEXT.encode("utf-8")).hexdigest()
    if landed != expected:
        raise SystemExit("read-back verification failed: entry.txt digest mismatch")
    return data


def main():
    if os.path.isdir("/output"):
        target = "/output/entry.txt"
    else:
        here = os.path.dirname(os.path.abspath(__file__))
        target = os.path.join(here, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)
    verify_written_bytes(target)
    print(TEXT)


if __name__ == "__main__":
    main()
