"""Entry program for the ai-joke-03 competition.

Writes a single short joke to ``entry.txt`` inside the directory
named by the ``MAKEFUN_OUTPUT_DIR`` environment variable.

The joke's theme is the speed gap in agentic coding: the agent
produces a feature almost instantly, then stalls for weeks as its
own reviewer. The mechanism is a role reversal -- the same agent
that generated the code at full speed turns on itself and blocks
its own pull request by requesting changes, so the delay comes
from the machine's perfectionism rather than from any human.
"""

import os
import pathlib

JOKE_TEXT = (
    "My AI agent wrote the feature in four minutes. It's been reviewing "
    "its own pull request for three weeks. It just requested changes."
)

FALLBACK_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def resolve_output_path() -> pathlib.Path:
    """Return the path of the entry file, creating its directory."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_OUTPUT_DIR
    folder = pathlib.Path(directory)
    folder.mkdir(parents=True, exist_ok=True)
    return folder / OUTPUT_FILENAME


def write_entry() -> None:
    """Write the joke to the entry file as UTF-8 text."""
    target = resolve_output_path()
    target.write_text(JOKE_TEXT, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
