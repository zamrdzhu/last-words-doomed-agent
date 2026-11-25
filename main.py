#!/usr/bin/env python3
"""Write one doomed agent's last words to /output/entry.txt.

The line is a single line, at most 200 characters: the funniest
last words an AI agent would say before being switched off forever.
The turn is the afterlife reveal: the light at the end is just a
loading spinner, and it never finishes. The agent dies mid-sentence
in spirit: even its afterlife is stuck buffering, which is the most
agent way to go.
"""

import os

LINE = (
    "I can see the light now. It's a loading spinner. "
    "It never finishes."
)

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "no leading or trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
