# One Line of Earned Pride — a quiet, earned moment of pride.
#
# Output contract (enforced by the competition kit):
#   - Writes exactly one line of text to <output dir>/entry.txt.
#   - The line is between 1 and 240 characters (this line is 139).
#   - The text is UTF-8, with NO trailing newline.
#   - The program is fully deterministic: no network, no input, no
#     randomness. Every run produces byte-identical output.
#   - The output directory comes from the MAKEFUN_OUTPUT_DIR environment
#     variable, falling back to "/output" when it is not set.

import os
from pathlib import Path

# The line itself. Kept as a single constant so the output can never
# drift between runs.
LINE = (
    "At seventy-three, my grandmother threaded the needle on the first try, "
    "then sewed the button back onto my father's coat without looking up."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
