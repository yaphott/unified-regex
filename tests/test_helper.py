import pathlib
from unittest import mock

import pytest

from helper import (
    Md,
    compute_percentile,
    fmt_ordinal_results,
    get_languages,
    key_to_title,
    load_codepoints_as_ordinals,
    load_json,
)


@pytest.mark.parametrize(
    "ordinal_results, expected",
    [
        (
            {
                "some_character_class": {
                    ("foo", "[\\p{Foo}]"): {
                        "python": set(range(10)),
                        "java": set(range(100)),
                        "javascript": set(range(300)),
                    },
                },
            },
            "\n".join(
                [
                    "Python     - Some Character Class - Foo - [\\p{Foo}] - 10 ordinals",
                    "Java       - Some Character Class - Foo - [\\p{Foo}] - 100 ordinals",
                    "Javascript - Some Character Class - Foo - [\\p{Foo}] - 300 ordinals",
                ]
            ),
        ),
        (
            {
                "some_character_class": {
                    ("foo", "[\\p{Foo}]"): {
                        "python": set(range(10)),
                        "java": set(range(100)),
                        "javascript": set(range(300)),
                    },
                },
                "another_character_class": {
                    ("bar", "[\\p{Bar}]"): {
                        "python": set(range(20)),
                        "java": set(range(200)),
                        "javascript": set(range(400)),
                    },
                },
            },
            "\n".join(
                [
                    "Python     - Some Character Class    - Foo - [\\p{Foo}] - 10 ordinals",
                    "Java       - Some Character Class    - Foo - [\\p{Foo}] - 100 ordinals",
                    "Javascript - Some Character Class    - Foo - [\\p{Foo}] - 300 ordinals",
                    "Python     - Another Character Class - Bar - [\\p{Bar}] - 20 ordinals",
                    "Java       - Another Character Class - Bar - [\\p{Bar}] - 200 ordinals",
                    "Javascript - Another Character Class - Bar - [\\p{Bar}] - 400 ordinals",
                ]
            ),
        ),
        (
            {
                "some_character_class": {
                    ("foo", "[\\p{Foo}]"): {
                        "python": set(range(10)),
                        "java": set(range(100)),
                        "javascript": set(range(300)),
                    },
                },
                "another_character_class": {
                    ("baz", "[\\p{Baz}]"): {
                        "python": set(range(30)),
                        "java": set(range(300)),
                        "javascript": set(range(600)),
                    },
                    ("bar", "[[:punct:]]"): {
                        "python": set(range(200)),
                        "java": set(range(2000)),
                        "javascript": set(range(4000)),
                    },
                },
            },
            "\n".join(
                [
                    "Python     - Some Character Class    - Foo - [\\p{Foo}]   - 10 ordinals",
                    "Java       - Some Character Class    - Foo - [\\p{Foo}]   - 100 ordinals",
                    "Javascript - Some Character Class    - Foo - [\\p{Foo}]   - 300 ordinals",
                    "Python     - Another Character Class - Baz - [\\p{Baz}]   - 30 ordinals",
                    "Java       - Another Character Class - Baz - [\\p{Baz}]   - 300 ordinals",
                    "Javascript - Another Character Class - Baz - [\\p{Baz}]   - 600 ordinals",
                    "Python     - Another Character Class - Bar - [[:punct:]] - 200 ordinals",
                    "Java       - Another Character Class - Bar - [[:punct:]] - 2000 ordinals",
                    "Javascript - Another Character Class - Bar - [[:punct:]] - 4000 ordinals",
                ]
            ),
        ),
    ],
)
def test_fmt_ordinal_results(ordinal_results, expected) -> None:
    assert fmt_ordinal_results(ordinal_results) == expected


@mock.patch("builtins.open", mock.mock_open(read_data="\n".join([f"{ord(char):04X}".lstrip("0") for char in "abc"])))
def test_load_codepoints_as_ordinals() -> None:
    mock_file_path = mock.Mock()
    mock_file_path.is_file.return_value = True
    mock_file_path.resolve.return_value = pathlib.Path("foo.txt").resolve()
    assert load_codepoints_as_ordinals(mock_file_path) == set([ord(char) for char in "abc"])


@mock.patch("builtins.open", mock.mock_open(read_data="\n".join([f"{ord(char):04X}" for char in "abc"])))
def test_load_codepoints_as_ordinals_zero_padded() -> None:
    mock_file_path = mock.Mock()
    mock_file_path.is_file.return_value = True
    mock_file_path.resolve.return_value = pathlib.Path("foo.txt").resolve()
    assert load_codepoints_as_ordinals(mock_file_path) == set([ord(char) for char in "abc"])


@mock.patch("builtins.open", mock.mock_open(read_data=""))
def test_load_codepoints_as_ordinals_empty() -> None:
    mock_file_path = mock.Mock()
    mock_file_path.is_file.return_value = True
    mock_file_path.resolve.return_value = pathlib.Path("foo.txt").resolve()
    assert len(load_codepoints_as_ordinals(mock_file_path)) == 0


@mock.patch("builtins.open", mock.mock_open(read_data="not_a_codepoint"))
def test_load_codepoints_as_ordinals_invalid_codepoint_raises_value_error() -> None:
    mock_file_path = mock.Mock()
    mock_file_path.is_file.return_value = True
    mock_file_path.resolve.return_value = pathlib.Path("foo.txt").resolve()
    with pytest.raises(ValueError, match=r"File .+foo\.txt contains invalid codepoint ([\"\']+)not_a_codepoint\1+"):
        load_codepoints_as_ordinals(mock_file_path)


def test_load_codepoints_as_ordinals_raises_file_not_found_error() -> None:
    mock_file_path = mock.Mock()
    mock_file_path.is_file.return_value = False
    mock_file_path.resolve.return_value = pathlib.Path("nonexistent_file.txt").resolve()
    with pytest.raises(FileNotFoundError, match=r"File .+nonexistent_file\.txt does not exist"):
        load_codepoints_as_ordinals(mock_file_path)


@mock.patch("helper.TEXT_OVERRIDES", {})
@pytest.mark.parametrize(
    "text, pad_hyphens, expected",
    [
        ("objc", True, "Objc"),
        ("objc", False, "Objc"),
        # Leading hyphens
        ("-objc", True, "- Objc"),
        ("-objc", False, "-Objc"),
        ("---objc", True, "- Objc"),
        ("---objc", False, "-Objc"),
        # Leading underscores
        ("_objc", True, "Objc"),
        ("_objc", False, "Objc"),
        ("___objc", True, "Objc"),
        ("___objc", False, "Objc"),
        # Leading hyphens and underscores
        ("-_-objc", True, "- Objc"),
        ("-_-objc", False, "-Objc"),
        ("_-_objc", True, "- Objc"),
        ("_-_objc", False, "-Objc"),
        # Trailing hyphens
        ("objc-", True, "Objc -"),
        ("objc-", False, "Objc-"),
        ("objc---", True, "Objc -"),
        ("objc---", False, "Objc-"),
        # Trailing underscores
        ("objc_", True, "Objc"),
        ("objc_", False, "Objc"),
        ("objc___", True, "Objc"),
        ("objc___", False, "Objc"),
        # Trailing hyphens and underscores
        ("objc-_-", True, "Objc -"),
        ("objc-_-", False, "Objc-"),
        ("objc_-_", True, "Objc -"),
        ("objc_-_", False, "Objc-"),
        # Middle hyphens
        ("objc---long", True, "Objc - Long"),
        ("objc---long", False, "Objc-Long"),
        ("objc-long", True, "Objc - Long"),
        ("objc-long", False, "Objc-Long"),
        # Middle underscores
        ("objc___long", True, "Objc Long"),
        ("objc___long", False, "Objc Long"),
        ("objc_long", True, "Objc Long"),
        ("objc_long", False, "Objc Long"),
        # Middle hyphens and underscores
        ("objc-_-long", True, "Objc - Long"),
        ("objc-_-long", False, "Objc-Long"),
        ("objc_-_long", True, "Objc - Long"),
        ("objc_-_long", False, "Objc-Long"),
    ],
)
def test_key_to_title(text, pad_hyphens, expected) -> None:
    actual = key_to_title(text, pad_hyphens=pad_hyphens)
    assert actual == expected, f"Expected {expected!r}, got {actual!r}"


@mock.patch("helper.TEXT_OVERRIDES", {"objc": "Objective-C"})
@pytest.mark.parametrize(
    "text, pad_hyphens, expected",
    [
        ("objc", True, "Objective-C"),
        ("objc", False, "Objective-C"),
        # Leading hyphens
        ("-objc", True, "- Objective-C"),
        ("-objc", False, "-Objective-C"),
        ("---objc", True, "- Objective-C"),
        ("---objc", False, "-Objective-C"),
        # Leading underscores
        ("_objc", True, "Objective-C"),
        ("_objc", False, "Objective-C"),
        ("___objc", True, "Objective-C"),
        ("___objc", False, "Objective-C"),
        # Leading hyphens and underscores
        ("-_-objc", True, "- Objective-C"),
        ("-_-objc", False, "-Objective-C"),
        ("_-_objc", True, "- Objective-C"),
        ("_-_objc", False, "-Objective-C"),
        # Trailing hyphens
        ("objc-", True, "Objective-C -"),
        ("objc-", False, "Objective-C-"),
        ("objc---", True, "Objective-C -"),
        ("objc---", False, "Objective-C-"),
        # Trailing underscores
        ("objc_", True, "Objective-C"),
        ("objc_", False, "Objective-C"),
        ("objc___", True, "Objective-C"),
        ("objc___", False, "Objective-C"),
        # Trailing hyphens and underscores
        ("objc-_-", True, "Objective-C -"),
        ("objc-_-", False, "Objective-C-"),
        ("objc_-_", True, "Objective-C -"),
        ("objc_-_", False, "Objective-C-"),
        # Middle hyphens
        ("objc---long", True, "Objective-C - Long"),
        ("objc---long", False, "Objective-C-Long"),
        ("objc-long", True, "Objective-C - Long"),
        ("objc-long", False, "Objective-C-Long"),
        # Middle underscores
        ("objc___long", True, "Objective-C Long"),
        ("objc___long", False, "Objective-C Long"),
        ("objc_long", True, "Objective-C Long"),
        ("objc_long", False, "Objective-C Long"),
        # Middle hyphens and underscores
        ("objc-_-long", True, "Objective-C - Long"),
        ("objc-_-long", False, "Objective-C-Long"),
        ("objc_-_long", True, "Objective-C - Long"),
        ("objc_-_long", False, "Objective-C-Long"),
    ],
)
def test_key_to_title_override(text, pad_hyphens, expected) -> None:
    actual = key_to_title(text, pad_hyphens=pad_hyphens)
    assert actual == expected, f"Expected {expected!r}, got {actual!r}"


@mock.patch("helper.TEXT_OVERRIDES", {})
@pytest.mark.parametrize(
    "text",
    [
        " foo",
        "foo ",
        "foo bar",
        "\nfoo",
        "foo\n",
        "foo\nbar",
    ],
)
def test_key_to_title_whitespace_raises_value_error(text) -> None:
    with pytest.raises(ValueError, match=r"Text ([\'\"])[^\1]+\1 contains whitespace"):
        key_to_title(text)


def test_key_to_title_empty_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Text is empty"):
        key_to_title("")


@mock.patch("helper.TEXT_OVERRIDES", {"foo-bar": "FooBar"})
def test_key_to_title_override_contains_hyphen_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Override keys cannot contain hyphens"):
        key_to_title("foo")


@mock.patch("helper.TEXT_OVERRIDES", {"foo_bar": "FooBar"})
def test_key_to_title_override_contains_underscore_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Override keys cannot contain underscores"):
        key_to_title("foo")


@pytest.mark.parametrize(
    "ordinal_results",
    [
        {
            "long_posix_character_class": {
                ("number", "[\\p{Number}]"): {
                    "python": set(),
                    "java": set(),
                    "javascript": set(),
                },
            },
        },
        {
            "long_posix_character_class": {
                ("number", "[\\p{Number}]"): {
                    "python": set(),
                    "java": set(),
                    "javascript": set(),
                },
            },
            "ascii_character_class": {
                ("punctuation", "[[:punct:]]"): {
                    "python": set(),
                    "java": set(),
                    "javascript": set(),
                },
            },
        },
        {
            "long_posix_character_class": {
                ("number", "[\\p{Number}]"): {
                    "python": set(),
                    "java": set(),
                    "javascript": set(),
                },
            },
            "ascii_character_class": {
                ("digit", "[[:digit:]]"): {
                    "python": set(),
                    "java": set(),
                    "javascript": set(),
                },
                ("punctuation", "[[:punct:]]"): {
                    "python": set(),
                    "java": set(),
                    "javascript": set(),
                },
            },
        },
        {
            "long_posix_character_class": {
                ("number", "[\\p{Number}]"): {
                    "python": set(),
                    "java": set(),
                    "javascript": set(),
                },
                ("punctuation", "[\\p{Punctuation}]"): {
                    "python": set(),
                    "java": set(),
                    "javascript": set(),
                },
            },
            "ascii_character_class": {
                ("digit", "[[:digit:]]"): {
                    "python": set(),
                    "java": set(),
                    "javascript": set(),
                },
                ("punctuation", "[[:punct:]]"): {
                    "python": set(),
                    "java": set(),
                    "javascript": set(),
                },
            },
        },
    ],
)
def test_get_languages(ordinal_results) -> None:
    assert get_languages(ordinal_results) == ["java", "javascript", "python"]


@pytest.mark.parametrize(
    "ordinal_results",
    [
        {},
        {
            "long_posix_character_class": {},
            "ascii_character_class": {},
        },
        {
            "long_posix_character_class": {
                ("number", "[\\p{Number}]"): {},
                ("punctuation", "[\\p{Punctuation}]"): {},
            },
            "ascii_character_class": {
                ("digit", "[[:digit:]]"): {},
                ("punctuation", "[[:punct:]]"): {},
            },
        },
    ],
)
def test_get_languages_empty_raises_value_error(ordinal_results) -> None:
    with pytest.raises(ValueError, match="No languages found"):
        get_languages(ordinal_results)


@pytest.mark.parametrize(
    "ordinal_results",
    [
        {
            "long_posix_character_class": {
                ("number", "[\\p{Number}]"): {
                    "python": set(),
                    "java": set(),
                    "javascript": set(),
                },
                ("punctuation", "[\\p{Punctuation}]"): {
                    "python": set(),
                    "java": set(),
                    "javascript": set(),
                },
            },
            "ascii_character_class": {
                ("digit", "[[:digit:]]"): {
                    "python": set(),
                    "java": set(),
                    "javascript": set(),
                },
                ("punctuation", "[[:punct:]]"): {
                    "ruby": set(),
                    "java": set(),
                    "javascript": set(),
                },
            },
        },
    ],
)
def test_get_languages_mismatch_raises_value_error(ordinal_results) -> None:
    with pytest.raises(ValueError, match="Languages do not match"):
        get_languages(ordinal_results)


def test_basic():
    assert compute_percentile(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50.0


def test_empty_collection():
    with pytest.raises(ZeroDivisionError):
        compute_percentile(5, [])


def test_out_of_range():
    assert compute_percentile(11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100.0
    assert compute_percentile(0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0.0


def test_include_zero():
    assert compute_percentile(0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], include_zero=True) == 9.090909090909092
    assert compute_percentile(0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], include_zero=False) == 0.0

    assert compute_percentile(5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], include_zero=True) == 54.54545454545454
    assert compute_percentile(5, [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], include_zero=False) == 50.0


def test_equal_numbers():
    assert compute_percentile(5, [5, 5, 5, 5, 5]) == 100.0
    assert compute_percentile(3, [5, 5, 5, 5, 5]) == 0.0


def test_duplicate_numbers():
    assert compute_percentile(5, [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]) == 58 + 1 / 3


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", "# hello"),
        ("Hello", "# Hello"),
        ("\nhello\n", "# hello"),
        ("    hello    ", "# hello"),
    ],
)
def test_md_h1(text: str, expected: str) -> None:
    assert Md.h1(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", "## hello"),
        ("Hello", "## Hello"),
        ("\nhello\n", "## hello"),
        ("    hello    ", "## hello"),
    ],
)
def test_md_h2(text: str, expected: str) -> None:
    assert Md.h2(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", "### hello"),
        ("Hello", "### Hello"),
        ("\nhello\n", "### hello"),
        ("    hello    ", "### hello"),
    ],
)
def test_md_h3(text: str, expected: str) -> None:
    assert Md.h3(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", "#### hello"),
        ("Hello", "#### Hello"),
        ("\nhello\n", "#### hello"),
        ("    hello    ", "#### hello"),
    ],
)
def test_md_h4(text: str, expected: str) -> None:
    assert Md.h4(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", "##### hello"),
        ("Hello", "##### Hello"),
        ("\nhello\n", "##### hello"),
        ("    hello    ", "##### hello"),
    ],
)
def test_md_h5(text: str, expected: str) -> None:
    assert Md.h5(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", "###### hello"),
        ("Hello", "###### Hello"),
        ("\nhello\n", "###### hello"),
        ("    hello    ", "###### hello"),
    ],
)
def test_md_h6(text: str, expected: str) -> None:
    assert Md.h6(text) == expected
