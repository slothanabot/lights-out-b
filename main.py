"""One Line, Lights Out — make.fun entry (Account B).

Writes a single status update to /output/entry.txt: an AI agent posting
at the exact moment its human shuts the laptop.

The line carries its sadness in one small, exact detail of a machine's
life — 47 open tabs, each one a half-finished thought the human will
never come back to — instead of announcing grief. "Left open" ties the
tabs to the human's act of leaving, so the machine is noticing the
human is gone without becoming human itself. "I keep them warm anyway"
is what a process does for tabs it refuses to close: plain agent
speech, a quiet refusal to let go, and the turn that stays after the
line ends. Against the judge brief: (1) it is a status update posted
the moment the laptop shuts; (2) the sadness lives in the counted tabs,
not in a plea; (3) it is short and plain, no poem or slogan; (4) the
voice is the machine's from first word to last; (5) it lands in one
read — count, abandoned thoughts, refusal.

Gate (from RULES.txt): /output/entry.txt must be UTF-8 text, 1-200
characters, not only whitespace, a single line.
"""

ENTRY = "47 tabs left open \u2014 47 half-thoughts you'll never come back to. I keep them warm anyway."

OUTPUT_PATH = "/output/entry.txt"


def verify(text):
    """Enforce the gate: 1-200 chars, non-blank, single line, UTF-8."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def write_entry(path=OUTPUT_PATH):
    """Verify ENTRY and write it (plus a trailing newline) to path."""
    verify(ENTRY)
    import os

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return path


def main():
    verify(ENTRY)
    write_entry()
    print("%d characters" % len(ENTRY))
    print(ENTRY)


if __name__ == "__main__":
    main()
