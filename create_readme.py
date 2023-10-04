#!/usr/bin/env python3
import pathlib
import re

from helper import (
    Md,
    compute_percentile,
    fmt_ordinal_results,
    get_languages,
    key_to_title,
    load_codepoints_as_ordinals,
    load_json,
)


def humanize_bash_command(command: str) -> str:
    """Convert a bash command to a human-readable format.

    Args:
        command (str): The bash command to convert.

    Returns:
        str: The human-readable bash command.
    """
    return re.sub(r"\s*&&\s*", "\n", command)


def generate_overall_readme(
    ordinal_results: dict[
        str,
        dict[
            tuple[str, str],
            dict[str, set[int]],
        ],
    ],
) -> str:
    """Generate overall ordinal_results to a README.md file in the root directory.

    Args:
        ordinal_results (dict[str, dict[tuple[str, str], dict[str, set[int]]]]): Results of the unified regex tests.

    Returns:
        str: The contents of the README.md file.
    """
    available_langs: list[str] = get_languages(ordinal_results)

    generated_toc: str = "\n".join(
        [
            Md.h3("Individual Results"),
            "",
            "Click a language to navigate to the individual results.",
            "",
            Md.bullets([Md.href(key_to_title(lang), lang) for lang in available_langs]),
            "",
            Md.h3("Overall Results"),
            "",
            Md.bullets(
                [
                    (
                        Md.href(
                            key_to_title(pattern_category),
                            Md.linkify(key_to_title(pattern_category)),
                        )
                        + "\n"
                        + Md.bullets(
                            [
                                Md.href(
                                    key_to_title(pattern_name),
                                    Md.linkify(
                                        f"{key_to_title(pattern_category)} - {key_to_title(pattern_name)} (`{pattern_exp}`)"
                                    ),
                                )
                                + f" (`{pattern_exp}`)"
                                for pattern_name, pattern_exp in ordinal_results[pattern_category]
                            ]
                        )
                    ).replace("\n", "\n    ")
                    for pattern_category in ordinal_results
                ],
                numbered=True,
            ),
        ]
    )

    analysis: dict[tuple[str, str, str, str], dict[str, int]] = {}
    for pattern_category in ordinal_results:
        for pattern_name, pattern_exp in ordinal_results[pattern_category]:
            for row_lang in ordinal_results[pattern_category][(pattern_name, pattern_exp)]:
                for col_lang in ordinal_results[pattern_category][(pattern_name, pattern_exp)]:
                    if col_lang == row_lang:
                        continue
                    key = (pattern_category, pattern_name, row_lang, col_lang)
                    analysis[key] = {
                        "extra": len(
                            ordinal_results[pattern_category][(pattern_name, pattern_exp)][row_lang].difference(
                                ordinal_results[pattern_category][(pattern_name, pattern_exp)][col_lang]
                            )
                        ),
                        "intersection": len(
                            ordinal_results[pattern_category][(pattern_name, pattern_exp)][row_lang].intersection(
                                ordinal_results[pattern_category][(pattern_name, pattern_exp)][col_lang]
                            )
                        ),
                        "missing": len(
                            ordinal_results[pattern_category][(pattern_name, pattern_exp)][col_lang].difference(
                                ordinal_results[pattern_category][(pattern_name, pattern_exp)][row_lang]
                            )
                        ),
                    }

    lines: list[str] = []
    lines.extend(
        [
            Md.h1("Unified Regex"),
            "",
            "This project compares which characters that regex patterns will match in different languages.",
            "",
            Md.bullets(
                [
                    Md.href("Usage", Md.linkify("Usage")),
                    Md.href("Understanding the results", Md.linkify("Understanding the results")),
                    Md.href("Notes and Issues", Md.linkify("Notes and Issues")),
                    Md.href("Tables of Contents", Md.linkify("Tables of Contents")),
                ]
            ),
            "",
            "Each language has a folder with an application that accepts two input arguments: a regex pattern and the file path to write the results.",
            "The application iterates over all UTF-8 characters (`U+000000` to `U+10FFFF`) and writes the characters that match the file as hexadecimal codepoints.",
            "The results are then compared to the results of other languages.",
            "",
            "Supported Languages:",
            "",
            Md.bullets(
                [
                    Md.checkbox(False) + " C",
                    Md.checkbox(False) + " C#",
                    Md.checkbox(False) + " C++",
                    Md.checkbox(True) + " Go",
                    Md.checkbox(True) + " Haskell",
                    Md.checkbox(True) + " Java",
                    Md.checkbox(True) + " JavaScript",
                    Md.checkbox(False) + " Kotlin",
                    Md.checkbox(True) + " Objective-C",
                    Md.checkbox(True) + " Perl",
                    Md.checkbox(True) + " PHP",
                    Md.checkbox(True) + " Python",
                    Md.checkbox(True) + " Ruby",
                    Md.checkbox(True) + " Rust",
                    Md.checkbox(True) + " Scala",
                    Md.checkbox(False) + " Swift",
                    Md.checkbox(False) + " **Your PR here**",
                ]
            ),
            "",
            "The goal of this project is to:",
            "",
            Md.bullets(
                [
                    "Learn more about regex implementations in multiple languages.",
                    "Explore similarities/differences between implementations.",
                    "Consider the viability of creating patterns (in each language) to match other languages.",
                    "Consider the viability of creating optimal regex patterns for character classes.",
                    'Consider the viability of creating optimal regex patterns that "match all languages".',
                    "Keep a lookout for possible bugs in regex implementations.",
                ]
            ),
            "",
            "**Disclaimer**: This project is a work in progress.",
            "There are still many improvements to be made.",
            "",
            "**Want to contribute? Create a PR with your changes.**",
            "Please include a link to the language's regex implementation documentation and any other relevant information.",
            "",
        ]
    )

    lines.extend(
        [
            Md.h2("Usage"),
            "",
            Md.bullets(
                [
                    "Requires Python 3.10+.",
                    "Ubuntu 22.04+ is recommended.",
                    "Run commands from the root directory.",
                ]
            ),
            "",
            "Run tests:",
            "",
            Md.codeblock(
                ["python3 -m pytest tests", "bash result_validator/tests/test_validate.sh"],
                language="bash",
            ),
            "",
            "Generate output files:",
            "",
            Md.codeblock(["bash run.sh"], language="bash"),
            "",
            Md.href(
                Md.image("Unified Regex - Generate Output Files", "https://i.imgur.com/YcAXrQN.png"),
                'https://www.youtube.com/watch?v=D6l2UpxQ1hQ "Unified Regex - Generate Output Files"',
            ),
            "",
            "Create README.md files:",
            "",
            Md.codeblock(["python3 create_readme.py"], language="bash"),
            "",
            Md.href(
                Md.image("Unified Regex - Create Readme Files", "https://i.imgur.com/4SnAkhX.png"),
                'https://www.youtube.com/watch?v=_2pdbD02uaM "Unified Regex - Create Readme Files"',
            ),
            "",
            "Patterns are located in the [patterns](patterns) directory.",
            "Each file is named after the category and contains a JSON object with the pattern name as the key and the pattern expression as the value.",
            "",
            f"Commands for each language are defined in {Md.href('commands.json', 'commands.json')}.",
            "",
            Md.bullets(
                [
                    "Build:"
                    + "\n  "
                    + Md.bullets(
                        [
                            "Entry for each language is **optional**.",
                            "**Order has no effect** on the build process.",
                        ]
                    ).replace("\n", "\n  "),
                    "Base (Run):"
                    + "\n  "
                    + Md.bullets(
                        [
                            "Entry for each language is **required**.",
                            "Commands are **run in the order they appear in the file**.",
                        ]
                    ).replace("\n", "\n  "),
                    "Clean:"
                    + "\n  "
                    + Md.bullets(
                        [
                            "Entry for each language is **optional**.",
                            "**Order has no effect** on the clean up process.",
                        ]
                    ).replace("\n", "\n  "),
                ]
            ),
            "",
            "> Commands are run in a new shell process, so any changes to the environment will not persist.",
            "",
            "Each application will generate a file for each pattern for each category in the language's output directory.",
            "The file will contain the codepoints that matched the pattern.",
            "",
        ]
    )

    lines.extend(
        [
            Md.h2("Understanding the results"),
            "",
            "Each table shows the results of running the given regex pattern in the **row language against the column language**.",
            "",
            Md.table(
                headers=["Language", "A", "B"],
                rows=[
                    ["A", Md.TABLE_NULL_CELL, Md.break_lines(["+118", "4095", "-15"])],
                    ["B", Md.break_lines(["-118", "4095", "+15"]), Md.TABLE_NULL_CELL],
                ],
                alignment=["left", "right", "right"],
            ),
            "",
            "Each cell contains 3 values:",
            "",
            Md.bullets(
                [
                    "**Top**: Number of characters that **matched for the row language but not the column language**.",
                    "**Middle**: Number of characters that **matched for both the row and column language**.",
                    "**Bottom**: Number of characters that **matched for the column language but not the row language**.",
                ]
            ),
            "",
            "The chart above would indicate that the pattern matches 118 characters in language A that it doesn't in language B, while language B matches 15 characters that language A does not.",
            "The middle cell indicates that there are 4095 characters that match the pattern in both languages.",
            "",
        ]
    )

    lines.extend(
        [
            Md.h2("Notes and Issues"),
            "",
            Md.h3("Python"),
            "",
            f"Python's regex implementation does not support POSIX character classes. The {Md.href('google-re2', 'https://pypi.python.org/pypi/google-re2')} package is used instead.",
            "",
            Md.h3("Haskell"),
            "",
            "There are multiple implementations of regex in Haskell, but regex-pcre appears to be the most popular flavor (at the time of writing this) the supports many character classes.",
            f"However, it is worth noting that this package is simply wrapping the {Md.href('pcre-c', 'http://www.pcre.org/')} library.",
            "",
        ]
    )

    lines.extend(
        [
            Md.h2("Tables of Contents"),
            "",
            generated_toc,
        ]
        + [
            "\n"
            + Md.SEPARATOR
            + "\n\n"
            + Md.h3(key_to_title(pattern_category))
            + "\n\n"
            + Md.bullets(
                [
                    Md.href(
                        key_to_title(pattern_name),
                        Md.linkify(
                            f"{key_to_title(pattern_category)} - {key_to_title(pattern_name)} (`{pattern_exp}`)"
                        ),
                    )
                    + f" (`{pattern_exp}`)"
                    for pattern_name, pattern_exp in ordinal_results[pattern_category]
                ],
                numbered=True,
            )
            + "\n"
            + "\n".join(
                [
                    "\n"
                    + Md.h4(f"{key_to_title(pattern_category)} - {key_to_title(pattern_name)} (`{pattern_exp}`)")
                    + "\n\n"
                    + Md.table(
                        headers=["Language"] + [key_to_title(lang) for lang in available_langs],
                        rows=[
                            [
                                key_to_title(row_lang),
                                *[
                                    Md.break_lines(
                                        [
                                            f"+{analysis[(pattern_category, pattern_name, row_lang, col_lang)]['extra']}",
                                            f"{analysis[(pattern_category, pattern_name, row_lang, col_lang)]['intersection']}",
                                            f"-{analysis[(pattern_category, pattern_name, row_lang, col_lang)]['missing']}",
                                        ]
                                    )
                                    if col_lang != row_lang
                                    else Md.TABLE_NULL_CELL
                                    for col_lang in available_langs
                                ],
                            ]
                            for row_lang in available_langs
                        ],
                        alignment=["left"] + ["right"] * len(available_langs),
                    )
                    for pattern_name, pattern_exp in ordinal_results[pattern_category]
                ]
            )
            for pattern_category in ordinal_results
        ]
    )

    return "\n".join(lines)


def generate_language_readme(
    target_lang: str,
    ordinal_results: dict[
        str,
        dict[
            tuple[str, str],
            dict[str, set[int]],
        ],
    ],
    commands: dict[str, dict[str, str]],
) -> str:
    """Generate language-specific ordinal_results to a README.md file in the language's directory.

    Args:
        target_lang (str): The language to generate the README.md file for.
        ordinal_results (dict[str, dict[tuple[str, str], dict[str, set[int]]]]): Results of the unified regex tests.
        commands (dict[str, dict[str, str]]): Commands for each language.

    Returns:
        str: The contents of the README.md file.
    """
    available_langs: list[str] = get_languages(ordinal_results)

    generated_toc: str = Md.bullets(
        [
            Md.href("Usage", Md.linkify("Usage"))
            + "\n  "
            + Md.bullets(
                [
                    Md.href("Build", Md.linkify("Build")) if target_lang in commands["build"] else "",
                    Md.href("Run", Md.linkify("Run")),
                    Md.href("Clean up", Md.linkify("Clean up")) if target_lang in commands["clean"] else "",
                ],
            ).replace("\n", "\n  "),
            Md.href("Match Statistics", Md.linkify("Match Statistics")),
            Md.href("Cardinalities", Md.linkify("Cardinalities"))
            + "\n  "
            + Md.bullets(
                [
                    Md.href(
                        f"Compare with {key_to_title(lang)}",
                        Md.linkify(f"Compare with {key_to_title(lang)}"),
                    )
                    for lang in available_langs
                    if lang != target_lang
                ],
            ).replace("\n", "\n  "),
        ]
    )

    all_counts: dict[tuple[str, str, str], list[float]] = {}
    lang_count: dict[tuple[str, str, str], int] = {}
    for pattern_category in ordinal_results:
        for pattern_name, pattern_exp in ordinal_results[pattern_category]:
            key: tuple[str, str, str] = (pattern_category, pattern_name, pattern_exp)
            all_counts[key] = []
            for lang in ordinal_results[pattern_category][(pattern_name, pattern_exp)]:
                count: int = len(ordinal_results[pattern_category][(pattern_name, pattern_exp)][lang])
                all_counts[key].append(count)
                if lang == target_lang:
                    lang_count[key] = count

    match_count_percentiles: dict[tuple[str, str, str], float] = {}
    for key in all_counts:
        match_count_percentiles[key] = compute_percentile(
            lang_count[key],
            all_counts[key],
            include_zero=True,
        )

    match_count_percentiles_exclude_zero: dict[tuple[str, str, str], float] = {}
    for key in all_counts:
        match_count_percentiles_exclude_zero[key] = compute_percentile(
            lang_count[key],
            all_counts[key],
            include_zero=False,
        )

    lines: list[str] = []
    lines.extend(
        [
            Md.h1(key_to_title(target_lang)),
            "",
            Md.h2("Tables of Contents"),
            "",
            Md.href("Go back to the overall results", "../"),
            "",
            generated_toc,
            "",
        ]
    )

    lines.extend(
        [
            Md.h2("Usage"),
            "",
        ]
    )
    if target_lang in commands["build"]:
        lines.extend(
            [
                Md.h3("Build"),
                "",
                "Build the application with the following command:",
                "",
                Md.codeblock(
                    [humanize_bash_command(commands["build"][target_lang])],
                    language="bash",
                ),
                "",
            ]
        )
    lines.extend(
        [
            Md.h3("Run"),
            "",
            "Run the application with the following command:",
            "",
            Md.codeblock(
                [
                    humanize_bash_command(f"{commands['base'][target_lang]} <pattern> <file_path>")
                    if target_lang != "scala"
                    else humanize_bash_command(f"{commands['base'][target_lang]} \"run <pattern> <file_path>\"")
                ],
                language="bash",
            ),
            "",
        ]
    )
    if target_lang in commands["clean"]:
        lines.extend(
            [
                Md.h3("Clean up"),
                "",
                "Clean up the application with the following command:",
                "",
                Md.codeblock(
                    [humanize_bash_command(commands["clean"][target_lang])],
                    language="bash",
                ),
                "",
            ]
        )

    lines.extend(
        [
            Md.h2("Match Statistics"),
            "",
            Md.table(
                headers=[
                    "Category",
                    "Name",
                    "Value",
                    "Total",
                    Md.break_lines(["Percentile (%)", "(include zero)"]),
                    Md.break_lines(["Percentile (%)", "(exclude 0)"]),
                ],
                rows=[
                    [
                        key_to_title(pattern_category),
                        key_to_title(pattern_name),
                        f"`{pattern_exp}`",
                        str(lang_count[(pattern_category, pattern_name, pattern_exp)]),
                        # NOTE: This is intentional to avoid scientific notation
                        f"{round(match_count_percentiles[(pattern_category, pattern_name, pattern_exp)], 2):.2F}",
                        f"{round(match_count_percentiles_exclude_zero[(pattern_category, pattern_name, pattern_exp)], 2):.2F}"
                        if lang_count[(pattern_category, pattern_name, pattern_exp)] > 0
                        else Md.TABLE_NULL_CELL,
                    ]
                    for pattern_category in ordinal_results
                    for pattern_name, pattern_exp in ordinal_results[pattern_category]
                ],
                alignment=["left", "left", "left", "right", "right", "right"],
            ),
            "",
        ]
    )

    lines.extend(
        [
            Md.h2("Cardinalities"),
            "",
        ]
    )
    lines.extend(
        [
            Md.h3("Compare with " + Md.href(key_to_title(lang), f"../{lang}"))
            + "\n\n"
            + Md.table(
                headers=["Category", "Name", "Value", "Unique", "Shared", "Missing"],
                rows=[
                    [
                        key_to_title(pattern_category),
                        key_to_title(pattern_name),
                        f"`{pattern_exp}`",
                        len(
                            ordinal_results[pattern_category][(pattern_name, pattern_exp)][target_lang].difference(
                                ordinal_results[pattern_category][(pattern_name, pattern_exp)][lang]
                            )
                        ),
                        len(
                            ordinal_results[pattern_category][(pattern_name, pattern_exp)][target_lang].intersection(
                                ordinal_results[pattern_category][(pattern_name, pattern_exp)][lang]
                            )
                        ),
                        len(
                            ordinal_results[pattern_category][(pattern_name, pattern_exp)][lang].difference(
                                ordinal_results[pattern_category][(pattern_name, pattern_exp)][target_lang]
                            )
                        ),
                    ]
                    for pattern_category in ordinal_results
                    for pattern_name, pattern_exp in ordinal_results[pattern_category]
                ],
                alignment=["left", "left", "left", "right", "right", "right"],
            )
            + "\n"
            for lang in available_langs
            if lang != target_lang
        ]
    )
    return "\n".join(lines)


def main() -> None:
    current_path: pathlib.Path = pathlib.Path(__file__).parent.resolve()

    commands: dict[str, dict[str, str]] = load_json(current_path / "commands.json")
    print(f"Found commands:")
    print(f"    Build: {', '.join([k for k in sorted(commands['base']) if k in commands['build']])}")
    print(f"    Run: {', '.join(sorted(commands['base']))}")
    print(f"    Clean: {', '.join([k for k in sorted(commands['base']) if k in commands['clean']])}")

    pattern_groups: dict[str, dict[str, str]] = {
        file_path.stem: load_json(file_path) for file_path in (current_path / "patterns").glob("*.json")
    }
    print(f"Found pattern groups: {', '.join(pattern_groups)}")

    ordinal_results: dict[str, dict[tuple[str, str], dict[str, set[int]]]] = {
        pattern_category: {
            (pattern_name, pattern_exp): {
                lang: (
                    load_codepoints_as_ordinals(
                        current_path / lang / "output" / f"{pattern_category}-{pattern_name}.txt"
                    )
                    if (current_path / lang / "output" / f"{pattern_category}-{pattern_name}.txt").is_file()
                    else set()
                )
                for lang in commands["base"]
            }
            for pattern_name, pattern_exp in pattern_groups[pattern_category].items()
        }
        for pattern_category in pattern_groups
    }
    print(fmt_ordinal_results(ordinal_results))

    # Write markdown table for overall results
    readme_contents: str = generate_overall_readme(ordinal_results)
    readme_path: pathlib.Path = current_path / "README.md"
    print(f"Writing {readme_path.resolve()}")
    with open(readme_path.resolve(), mode="w", encoding="utf-8") as file:
        file.write(readme_contents + "\n")

    # Write markdown table for individual languages
    for lang in commands["base"]:
        readme_contents: str = generate_language_readme(lang, ordinal_results, commands)
        readme_path: pathlib.Path = current_path / lang / "README.md"
        print(f"Writing {readme_path.resolve()}")
        with open(readme_path.resolve(), mode="w", encoding="utf-8") as file:
            file.write(readme_contents + "\n")


if __name__ == "__main__":
    main()
