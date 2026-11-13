"""Write one joke about AI coding agents to the entry output file.

Standard library only. Reads no input, uses no network.
"""

import os

JOKE = (
    "I asked my AI agent to fix one bug. It fixed the bug, rewrote the "
    "module, updated the docs, and deprecated me."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # The harness may point at a directory that does not exist yet.
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
