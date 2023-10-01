"""Load a result file and check that the contents are anything but the literal pattern."""

import sys
import argparse
import pathlib

from enum import Enum
from typing import Final


CURRENT_DIR: Final[pathlib.Path] = pathlib.Path(__file__).resolve().parent

class ResultStatus(Enum):
    """Exit statuses for the result validator."""
    VALID = "valid"
    INVALID = "invalid"
    MISSING = "missing"
    EMPTY = "empty"

if (CURRENT_DIR / "helper.py").is_file():
    # Running from the root of the repo
    from helper import load_codepoints_as_ordinals
elif (CURRENT_DIR.parent / "helper.py").is_file():
    # Running from the result_validator directory
    sys.path.append(str(CURRENT_DIR.parent))
    from helper import load_codepoints_as_ordinals
elif (CURRENT_DIR.parent.parent / "helper.py").is_file():
    # Running from the result_validator/tests directory
    sys.path.append(str(CURRENT_DIR.parent.parent))
    from helper import load_codepoints_as_ordinals
else:
    raise ImportError("Could not find helper.py")

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern", type=str, help="Pattern to check")
    parser.add_argument("file_path", type=pathlib.Path, help="File to check")
    return parser.parse_args()

def main() -> None:
    pargs: argparse.Namespace = parse_args()

    pattern: str = pargs.pattern
    if not pattern:
        raise ValueError("Pattern cannot be empty")
    if not pattern.startswith("["):
        raise ValueError(f"Pattern {pattern} does not start with '['")
    if not pattern.endswith("]"):
        raise ValueError(f"Pattern {pattern} does not end with ']'")

    file_path: pathlib.Path = pargs.file_path
    if not file_path.is_file():
        print(ResultStatus.MISSING.value)
        sys.exit(0)

    file_ordinals: set[int] = load_codepoints_as_ordinals(file_path)

    if not file_ordinals:
        print(ResultStatus.EMPTY.value)
        sys.exit(0)

    pattern_ordinals: set[int] = {ord(c) for c in pattern.removeprefix("[").removesuffix("]")}

    # Check as if the "\\" in "\p{...}" matches "\\" literally
    if pattern_ordinals == file_ordinals:
        print(ResultStatus.INVALID.value)
        sys.exit(0)

    # Check as if the "\\p" in "\\p{...}" matches "p" literally
    pattern_ordinals = pattern_ordinals.difference({ord("\\")})
    if pattern_ordinals == file_ordinals:
        print(ResultStatus.INVALID.value)
        sys.exit(0)

    print(ResultStatus.VALID.value)
    sys.exit(0)

if __name__ == "__main__":
    main()
