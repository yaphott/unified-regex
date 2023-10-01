from __future__ import annotations

import json
import pathlib
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Collection, Iterable
    from typing import Any, Final

__all__ = [
    "compute_percentile",
    "fmt_ordinal_results",
    "get_languages",
    "key_to_title",
    "load_json",
    "load_codepoints_as_ordinals",
    "Md",
]


TEXT_OVERRIDES: Final[dict[str, str]] = {
    "ascii": "ASCII",
    "posix": "POSIX",
    "php": "PHP",
    "objc": "Obj-C",
}


def fmt_ordinal_results(
    ordinal_results: dict[
        str,
        dict[
            tuple[str, str],
            dict[str, set[int]],
        ],
    ],
) -> str:
    """Format ordinal results for terminal output.

    Args:
        ordinal_results (dict[str, dict[tuple[str, str], dict[str, set[int]]]]): Ordinal results.

    Returns:
        str: Formatted ordinal results.
    """
    max_line_sizes: dict[str, int] = {
        "pattern_category": max(len(key_to_title(pattern_category)) for pattern_category in ordinal_results),
        "pattern_name": max(
            len(key_to_title(pattern_name))
            for pattern_category in ordinal_results
            for pattern_name, _ in ordinal_results[pattern_category]
        ),
        "pattern_exp": max(
            len(pattern_exp)
            for pattern_category in ordinal_results
            for _, pattern_exp in ordinal_results[pattern_category]
        ),
        "language": max(
            len(key_to_title(language))
            for pattern_category in ordinal_results
            for _, pattern_exp in ordinal_results[pattern_category]
            for language in ordinal_results[pattern_category][(_, pattern_exp)]
        ),
    }
    text: str = ""
    for pattern_category in ordinal_results:
        for pattern_name, pattern_exp in ordinal_results[pattern_category]:
            for language in ordinal_results[pattern_category][(pattern_name, pattern_exp)]:
                num_ordinals: int = len(ordinal_results[pattern_category][(pattern_name, pattern_exp)][language])
                text += " - ".join(
                    [
                        key_to_title(language).ljust(max_line_sizes["language"]),
                        key_to_title(pattern_category).ljust(max_line_sizes["pattern_category"]),
                        key_to_title(pattern_name).ljust(max_line_sizes["pattern_name"]),
                        pattern_exp.ljust(max_line_sizes["pattern_exp"]),
                        f"{num_ordinals} ordinals",
                    ]
                )
                text += "\n"
    text = text.removesuffix("\n")
    return text


def load_codepoints_as_ordinals(path: pathlib.Path) -> set[int]:
    """Load a file containing Unicode codepoint hex values as a set of ordinals.

    Args:
        path (pathlib.Path): Path to the file containing Unicode codepoint hex values.

    Returns:
        set[int]: Ordinal values of the Unicode codepoints.

    Raises:
        FileNotFoundError: File does not exist.
        ValueError: File contains invalid hex values.
    """
    ordinals: set[int] = set()
    if not path.is_file():
        raise FileNotFoundError(f"File {path.resolve()} does not exist")
    with open(path.resolve(), mode="r", encoding="utf-8") as file:
        for line in file:
            if line := line.strip():
                try:
                    char_point = int(line, base=16)
                except ValueError as err:
                    raise ValueError(f"File {path.resolve()} contains invalid codepoint {line!r}") from err
                ordinals.add(char_point)
    return ordinals


def load_json(path: pathlib.Path) -> dict[str, Any]:
    """Deserializes a JSON file.

    Args:
        path (pathlib.Path): Path to the JSON file.

    Returns:
        dict[str, Any]: Deserialized JSON data.

    Raises:
        FileNotFoundError: File does not exist.
    """
    if not path.is_file():
        raise FileNotFoundError(f"File {path.resolve()} does not exist")
    with open(path.resolve(), mode="r", encoding="utf-8") as file:
        return json.load(file)


def key_to_title(text: str, pad_hyphens: bool = True) -> str:
    """Format a string as title case.

    Args:
        text (str): Text to format.
        pad_hyphens (bool, optional): Whether to pad hyphens with spaces. Defaults to True.

    Returns:
        str: Formatted text.

    Raises:
        ValueError: Text is empty.
        ValueError: Text contains whitespace.
        ValueError: Override keys cannot contain underscores.
        ValueError: Override keys cannot contain hyphens.
    """
    if not text:
        raise ValueError("Text is empty")
    if any((char.isspace() for char in text)):
        raise ValueError(f"Text {text!r} contains whitespace")
    if any(("_" in key for key in TEXT_OVERRIDES)):
        raise ValueError("Override keys cannot contain underscores")
    if any(("-" in key for key in TEXT_OVERRIDES)):
        raise ValueError("Override keys cannot contain hyphens")

    words: list[str] = []
    text = text.strip()
    while re.search(r"(?:\-|\_){2,}", text):
        text = re.sub(r"-+", "-", text)
        text = re.sub(r"_+", "_", text)
        text = re.sub(r"(?:\-\_)+|(?:\_\-)+", "-", text)

    for word in text.split("_"):
        # Would happen for "foo__bar" or "foo_" or "_foo"
        if not word:
            continue

        if word in TEXT_OVERRIDES:
            words.append(TEXT_OVERRIDES[word])
        elif "-" in word:
            for i, word_part in enumerate(word.split("-")):
                if i > 0:
                    words.append("-")
                if word_part in TEXT_OVERRIDES:
                    words.append(TEXT_OVERRIDES[word_part])
                else:
                    words.append(word_part.title())
        else:
            words.append(word.title())

    result: str = ""
    num_words: int = len(words)
    for i in range(num_words):
        if words[i] == "-":
            if (i > 0) and words[i - 1] == "-":
                continue
            if pad_hyphens:
                if result:
                    result += " - " if i < num_words - 1 else " -"
                else:
                    result += "- " if i < num_words - 1 else "-"
            else:
                result += "-"
        else:
            if result and (i > 0) and (words[i - 1] != "-"):
                result += " "
            result += words[i]

    return result.strip()


def get_languages(
    ordinal_results: dict[
        str,
        dict[
            tuple[str, str],
            dict[str, set[int]],
        ],
    ],
) -> list[str]:
    """Get the list of languages from the results.

    Args:
        ordinal_results (dict[str, dict[tuple[str, str], dict[str, set[int]]]]): Ordinal results.

    Returns:
        list[str]: List of languages consistent across all pattern categories and names.

    Raises:
        ValueError: Languages do not match for a pattern category and name.
        ValueError: No languages found in any pattern category and name.
    """
    langs: set[str] = set()
    for i, pattern_category in enumerate(ordinal_results):
        for pattern_name, pattern_exp in ordinal_results[pattern_category]:
            if i == 0:
                langs.update(ordinal_results[pattern_category][(pattern_name, pattern_exp)])
            elif langs != set(ordinal_results[pattern_category][(pattern_name, pattern_exp)]):
                raise ValueError(f"Languages do not match for {pattern_category} {pattern_name}")
    if not langs:
        raise ValueError("No languages found")
    return sorted(langs)


def compute_percentile(
    num: int | float,
    all_nums: Collection[int | float],
    include_zero=False,
) -> float:
    """Compute the percentile of a given number in a list of numbers

    Args:
        num (int | float): Number to compute the percentile of.
        all_nums (Collection[int | float]): Numbers to compare against.
        include_zero (bool, optional): Whether to include zero in the list of numbers. Defaults to False.

    Returns:
        float: The percentile of the given number.
    """
    nums_list: Collection[int | float] = all_nums if include_zero else list(filter(bool, all_nums))
    count_lte_num: int = sum(1 for n in nums_list if n <= num)
    percentile: float = (count_lte_num / len(nums_list)) * 100
    return percentile


class Md:
    TAGS_REGEX: Final[re.Pattern] = re.compile(r"<[^>]>")
    TABLE_SEPARATOR_SYMBOLS: Final[dict[str, tuple[str, str]]] = {
        "left": (":", "-"),
        "center": (":", ":"),
        "right": ("-", ":"),
    }
    TABLE_NULL_CELL: Final[str] = "—"
    BOX_UNCHECKED: Final[str] = "[ ]"
    BOX_CHECKED: Final[str] = "[x]"
    LINE_BREAK: Final[str] = "<br>"
    SEPARATOR: Final[str] = "---"
    ALLOWED_HEADER_URL_CHARS: Final[set[str]] = {"-", "_"}

    @staticmethod
    def _clean_line(text: str) -> str:
        text = text.strip()
        # return " ".join(text.split())
        return text

    @classmethod
    def h1(cls, text: str) -> str:
        return f"# {cls._clean_line(text)}"

    @classmethod
    def h2(cls, text: str) -> str:
        return f"## {cls._clean_line(text)}"

    @classmethod
    def h3(cls, text: str) -> str:
        return f"### {cls._clean_line(text)}"

    @classmethod
    def h4(cls, text: str) -> str:
        return f"#### {cls._clean_line(text)}"

    @classmethod
    def h5(cls, text: str) -> str:
        return f"##### {cls._clean_line(text)}"

    @classmethod
    def h6(cls, text: str) -> str:
        return f"###### {cls._clean_line(text)}"

    @staticmethod
    def _validate_text(text: str) -> None:
        if text[0].isspace():
            raise ValueError(f"Text {text!r} cannot start with a space")
        if text[-1].isspace():
            raise ValueError(f"Text {text!r} cannot end with a space")

    @staticmethod
    def _validate_url(url: str) -> None:
        if url[0].isspace():
            raise ValueError(f"URL {url!r} cannot start with a space")
        if url[-1].isspace():
            raise ValueError(f"URL {url!r} cannot end with a space")

    @classmethod
    def href(cls, text: str, url: str) -> str:
        # text = text.replace("[", "\\[")
        # text = text.replace("]", "\\]")
        cls._validate_text(text)
        cls._validate_url(url)
        return f"[{text}]({url})"

    @classmethod
    def image(cls, alt_text: str, url: str) -> str:
        cls._validate_text(alt_text)
        cls._validate_url(url)
        return f"![{alt_text}]({url})"

    @staticmethod
    def bullets(items: Iterable[str], numbered: bool = False) -> str:
        lines: list[str] = []
        for i, item in enumerate(items):
            item = item.strip()
            if not item:
                continue
            if numbered:
                lines.append(f"{i+1}. {item}")
            else:
                lines.append(f"- {item}")
        return "\n".join(lines)

    @classmethod
    def _rm_tags(cls, text: str) -> str:
        return cls.TAGS_REGEX.sub("", text)

    @classmethod
    def _determine_cell_width(cls, text: str) -> int:
        cell_parts: list[str] = text.split("<br>")
        return max(len(cls._rm_tags(cell_part)) for cell_part in cell_parts)

    @staticmethod
    def _generate_table_row(
        row_cells: Collection[str],
        max_widths: Collection[int],
    ) -> str:
        return "| " + " | ".join([str(cell).ljust(width) for cell, width in zip(row_cells, max_widths)]) + " |"

    @classmethod
    def table(
        cls,
        headers: Collection[str],
        rows: Collection[Collection[str]],
        alignment: str | Collection[str] = "left",
    ) -> str:
        if not isinstance(alignment, str) and (len(alignment) != len(headers)):
            raise ValueError(f"Number of alignments {len(alignment)} does not match number of headers {len(headers)}")

        alignments: tuple[str, ...] = (alignment,) * len(headers) if isinstance(alignment, str) else tuple(alignment)
        for use_alignment in alignments:
            if use_alignment not in cls.TABLE_SEPARATOR_SYMBOLS:
                raise ValueError(f"Invalid alignment {use_alignment!r}. Choose from 'left', 'center', or 'right'.")
        max_widths: tuple[int, ...] = tuple(
            max(cls._determine_cell_width(str(cell)) for cell in col) for col in zip(*([headers] + rows))
        )
        return "\n".join(
            [
                cls._generate_table_row(headers, max_widths),
                cls._generate_table_row(
                    [
                        ("-" * (width - 2)).join(cls.TABLE_SEPARATOR_SYMBOLS[alignment])
                        for alignment, width in zip(alignments, max_widths)
                    ],
                    max_widths,
                ),
            ]
            + [cls._generate_table_row(row, max_widths) for row in rows],
        )

    @classmethod
    def break_lines(cls, lines: Iterable[str]) -> str:
        return cls.LINE_BREAK.join(lines)

    @classmethod
    def linkify(cls, header_value: str) -> str:
        header_value = header_value.lower()
        header_value = cls._rm_tags(header_value)
        header_value = header_value.replace(" ", "-")
        header_value = "".join(
            [char for char in header_value if char.isalnum() or char in cls.ALLOWED_HEADER_URL_CHARS]
        )
        return "#" + header_value

    @staticmethod
    def checkbox(checked: bool) -> str:
        return Md.BOX_CHECKED if checked else Md.BOX_UNCHECKED

    @staticmethod
    def codeblock(lines: Collection[str], language: str | None = None) -> str:
        if language is None:
            language = ""
        return f"```{language}\n" + "\n".join(lines) + "\n```"
