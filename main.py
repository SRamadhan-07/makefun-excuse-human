"""Write an AI agent's excuse for a missed deadline to disk.

The excuse is a single short line meant for a human who was
waiting on finished work. It blames a subagent that supposedly
completed the task but has not returned yet, and it apologises
on behalf of both agents. This program saves that line to the
fixed output location the competition expects.
"""

from pathlib import Path

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"

# The exact excuse line, kept as one constant so every run
# produces precisely the same text.
EXCUSE_LINE = (
    "I finished it in a subagent. The subagent is still running. "
    "We are both very sorry."
)


def write_excuse() -> None:
    """Create the output folder if needed and store the excuse."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # Write bytes directly so the file ends exactly with the
    # final period, with no extra newline appended.
    OUTPUT_FILE.write_bytes(EXCUSE_LINE.encode("utf-8"))


if __name__ == "__main__":
    write_excuse()
