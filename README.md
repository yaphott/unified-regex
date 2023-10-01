# Unified Regex

Common goals:

- Learn more about regex implementations in multiple languages.
- Explore similarities/differences between implementations.
- Consider viability of creating patterns (in each language) to match other languages.
- Consider viability of creating optimal regex patterns for character classes.
- Consider viability of creating optimal regex patterns that "match all languages".
- Keep a lookout for possible bugs in regex implementations.

Supported Languages:

- [ ] C
- [ ] C#
- [x] C++
- [x] Go
- [x] Haskell
- [x] Java
- [x] JavaScript
- [ ] Kotlin
- [x] Objective-C
- [x] Perl
- [x] PHP
- [x] Python
- [x] Ruby
- [x] Rust
- [x] Scala
- [ ] Swift
- [ ] **Your PR here**

**Disclaimer**: This is not a comprehensive test suite. It is meant to be a starting point for further exploration.

**Want to contribute? Create a PR with your changes.**
Please include a link to the language's regex implementation documentation and any other relevant information.

## Usage

- Requires Python 3.10+.
- Ubuntu 22.04+ is recommended.
- Run commands from the root directory.

Run tests:

```bash
python3 -m pytest tests
bash result_validator/tests/test_validate.sh
```

Generate output files:

```bash
bash run.sh
```

[![Unified Regex - Generate Output Files](https://i.imgur.com/YcAXrQN.png)](https://www.youtube.com/watch?v=D6l2UpxQ1hQ "Unified Regex - Generate Output Files")

Create README.md files:

```bash
python3 create_readme.py
```

[![Unified Regex - Create Readme Files](https://i.imgur.com/4SnAkhX.png)](https://www.youtube.com/watch?v=_2pdbD02uaM "Unified Regex - Create Readme Files")

Patterns are located in the [patterns](patterns) directory.
Each file is named after the category and contains a JSON object with the pattern name as the key and the pattern expression as the value.

Commands for each language are defined in [commands.json](commands.json).

- Build:
  - Entry for each language is **optional**.
  - **Order has no effect** on the build process.
- Base (Run):
  - Entry for each language is **required**.
  - Commands are **run in the order they appear in the file**.
- Clean:
  - Entry for each language is **optional**.
  - **Order has no effect** on the clean up process.

> Commands are run in a new shell process, so any changes to the environment will not persist.

Each application will generate a file for each pattern for each category in the language's output directory.
The file will contain the codepoints that matched the pattern.

## Understanding the results

Each table shows the results of running the given regex pattern in the **row language against the column language**.

| Language | A    | B    |
| :------- | ---: | ---: |
| A        | —    | +118<br>4095<br>-15 |
| B        | -118<br>4095<br>+15 | —    |

Each cell contains 3 values:

- **Top**: Number of characters that **matched for the row language but not the column language**.
- **Middle**: Number of characters that **matched for both the row and column language**.
- **Bottom**: Number of characters that **matched for the column language but not the row language**.

The chart above would indicate that the pattern matches 118 characters in language A that it doesn't in language B, while language B matches 15 characters that language A does not.
The middle cell indicates that there are 4095 characters that match the pattern in both languages.

## Notes and Issues

### Python

Python's regex implementation does not support POSIX character classes. The [google-re2](https://pypi.python.org/pypi/google-re2) package is used instead.

### Haskell

There are multiple implementations of regex in Haskell, but regex-pcre appears to be the most popular flavor (at the time of writing this) the supports many character classes.
However, it is worth noting that this package is simply wrapping the [pcre-c](http://www.pcre.org/) library.

### C++

The C++ regex implementation does not support POSIX character classes.

## Tables of Contents

### Individual Results

Click a language to navigate to the individual results.

- [C++](c++)
- [Go](go)
- [Haskell](haskell)
- [Java](java)
- [Javascript](javascript)
- [Obj-C](objc)
- [Perl](perl)
- [PHP](php)
- [Python](python)
- [Ruby](ruby)
- [Rust](rust)
- [Scala](scala)

### Overall Results

1. [Character Classes - ASCII](#character-classes---ascii)
    - [Uppercase Letter](#character-classes---ascii---uppercase-letter-upper) (`[[:upper:]]`)
    - [Lowercase Letter](#character-classes---ascii---lowercase-letter-lower) (`[[:lower:]]`)
    - [Letter And Digit](#character-classes---ascii---letter-and-digit-alnum) (`[[:alnum:]]`)
    - [Letter](#character-classes---ascii---letter-alpha) (`[[:alpha:]]`)
    - [ASCII Character](#character-classes---ascii---ascii-character-ascii) (`[[:ascii:]]`)
    - [Space And Tab](#character-classes---ascii---space-and-tab-blank) (`[[:blank:]]`)
    - [Control Character](#character-classes---ascii---control-character-cntrl) (`[[:cntrl:]]`)
    - [Digit](#character-classes---ascii---digit-digit) (`[[:digit:]]`)
    - [Visible Character](#character-classes---ascii---visible-character-graph) (`[[:graph:]]`)
    - [Printable](#character-classes---ascii---printable-print) (`[[:print:]]`)
    - [Punctuation](#character-classes---ascii---punctuation-punct) (`[[:punct:]]`)
    - [Whitespace](#character-classes---ascii---whitespace-space) (`[[:space:]]`)
    - [Word Character](#character-classes---ascii---word-character-word) (`[[:word:]]`)
    - [Hexadecimal Digit](#character-classes---ascii---hexadecimal-digit-xdigit) (`[[:xdigit:]]`)
2. [Character Classes - Common](#character-classes---common)
    - [Digit](#character-classes---common---digit-d) (`[\d]`)
    - [Whitespace](#character-classes---common---whitespace-s) (`[\s]`)
    - [Word Character](#character-classes---common---word-character-w) (`[\w]`)
3. [Character Classes - POSIX - Long](#character-classes---posix---long)
    - [Uppercase Letter](#character-classes---posix---long---uppercase-letter-puppercase_letter) (`[\p{Uppercase_Letter}]`)
    - [Lowercase Letter](#character-classes---posix---long---lowercase-letter-plowercase_letter) (`[\p{Lowercase_Letter}]`)
    - [Titlecase Letter](#character-classes---posix---long---titlecase-letter-ptitlecase_letter) (`[\p{Titlecase_Letter}]`)
    - [Cased Letter](#character-classes---posix---long---cased-letter-pcased_letter) (`[\p{Cased_Letter}]`)
    - [Modifier Letter](#character-classes---posix---long---modifier-letter-pmodifier_letter) (`[\p{Modifier_Letter}]`)
    - [Other Letter](#character-classes---posix---long---other-letter-pother_letter) (`[\p{Other_Letter}]`)
    - [Letter](#character-classes---posix---long---letter-pletter) (`[\p{Letter}]`)
    - [Nonspacing Mark](#character-classes---posix---long---nonspacing-mark-pnonspacing_mark) (`[\p{Nonspacing_Mark}]`)
    - [Spacing Mark](#character-classes---posix---long---spacing-mark-pspacing_mark) (`[\p{Spacing_Mark}]`)
    - [Enclosing Mark](#character-classes---posix---long---enclosing-mark-penclosing_mark) (`[\p{Enclosing_Mark}]`)
    - [Mark](#character-classes---posix---long---mark-pmark) (`[\p{Mark}]`)
    - [Decimal Number](#character-classes---posix---long---decimal-number-pdecimal_number) (`[\p{Decimal_Number}]`)
    - [Letter Number](#character-classes---posix---long---letter-number-pletter_number) (`[\p{Letter_Number}]`)
    - [Other Number](#character-classes---posix---long---other-number-pother_number) (`[\p{Other_Number}]`)
    - [Number](#character-classes---posix---long---number-pnumber) (`[\p{Number}]`)
    - [Connector Punctuation](#character-classes---posix---long---connector-punctuation-pconnector_punctuation) (`[\p{Connector_Punctuation}]`)
    - [Dash Punctuation](#character-classes---posix---long---dash-punctuation-pdash_punctuation) (`[\p{Dash_Punctuation}]`)
    - [Open Punctuation](#character-classes---posix---long---open-punctuation-popen_punctuation) (`[\p{Open_Punctuation}]`)
    - [Close Punctuation](#character-classes---posix---long---close-punctuation-pclose_punctuation) (`[\p{Close_Punctuation}]`)
    - [Initial Punctuation](#character-classes---posix---long---initial-punctuation-pinitial_punctuation) (`[\p{Initial_Punctuation}]`)
    - [Final Punctuation](#character-classes---posix---long---final-punctuation-pfinal_punctuation) (`[\p{Final_Punctuation}]`)
    - [Other Punctuation](#character-classes---posix---long---other-punctuation-pother_punctuation) (`[\p{Other_Punctuation}]`)
    - [Punctuation](#character-classes---posix---long---punctuation-ppunctuation) (`[\p{Punctuation}]`)
    - [Math Symbol](#character-classes---posix---long---math-symbol-pmath_symbol) (`[\p{Math_Symbol}]`)
    - [Currency Symbol](#character-classes---posix---long---currency-symbol-pcurrency_symbol) (`[\p{Currency_Symbol}]`)
    - [Modifier Symbol](#character-classes---posix---long---modifier-symbol-pmodifier_symbol) (`[\p{Modifier_Symbol}]`)
    - [Other Symbol](#character-classes---posix---long---other-symbol-pother_symbol) (`[\p{Other_Symbol}]`)
    - [Symbol](#character-classes---posix---long---symbol-psymbol) (`[\p{Symbol}]`)
    - [Space Separator](#character-classes---posix---long---space-separator-pspace_separator) (`[\p{Space_Separator}]`)
    - [Line Separator](#character-classes---posix---long---line-separator-pline_separator) (`[\p{Line_Separator}]`)
    - [Paragraph Separator](#character-classes---posix---long---paragraph-separator-pparagraph_separator) (`[\p{Paragraph_Separator}]`)
    - [Separator](#character-classes---posix---long---separator-pseparator) (`[\p{Separator}]`)
    - [Control](#character-classes---posix---long---control-pcontrol) (`[\p{Control}]`)
    - [Format](#character-classes---posix---long---format-pformat) (`[\p{Format}]`)
    - [Surrogate](#character-classes---posix---long---surrogate-psurrogate) (`[\p{Surrogate}]`)
    - [Private Use](#character-classes---posix---long---private-use-pprivate_use) (`[\p{Private_Use}]`)
    - [Unassigned](#character-classes---posix---long---unassigned-punassigned) (`[\p{Unassigned}]`)
    - [Other](#character-classes---posix---long---other-pother) (`[\p{Other}]`)
4. [Character Classes - POSIX - Short](#character-classes---posix---short)
    - [Uppercase Letter](#character-classes---posix---short---uppercase-letter-plu) (`[\p{Lu}]`)
    - [Lowercase Letter](#character-classes---posix---short---lowercase-letter-pll) (`[\p{Ll}]`)
    - [Titlecase Letter](#character-classes---posix---short---titlecase-letter-plt) (`[\p{Lt}]`)
    - [Cased Letter](#character-classes---posix---short---cased-letter-plc) (`[\p{LC}]`)
    - [Cased Letter Amp](#character-classes---posix---short---cased-letter-amp-pl) (`[\p{L&}]`)
    - [Modifier Letter](#character-classes---posix---short---modifier-letter-plm) (`[\p{Lm}]`)
    - [Other Letter](#character-classes---posix---short---other-letter-plo) (`[\p{Lo}]`)
    - [Letter](#character-classes---posix---short---letter-pl) (`[\p{L}]`)
    - [Nonspacing Mark](#character-classes---posix---short---nonspacing-mark-pmn) (`[\p{Mn}]`)
    - [Spacing Mark](#character-classes---posix---short---spacing-mark-pmc) (`[\p{Mc}]`)
    - [Enclosing Mark](#character-classes---posix---short---enclosing-mark-pme) (`[\p{Me}]`)
    - [Mark](#character-classes---posix---short---mark-pm) (`[\p{M}]`)
    - [Decimal Number](#character-classes---posix---short---decimal-number-pnd) (`[\p{Nd}]`)
    - [Letter Number](#character-classes---posix---short---letter-number-pnl) (`[\p{Nl}]`)
    - [Other Number](#character-classes---posix---short---other-number-pno) (`[\p{No}]`)
    - [Number](#character-classes---posix---short---number-pn) (`[\p{N}]`)
    - [Connector Punctuation](#character-classes---posix---short---connector-punctuation-ppc) (`[\p{Pc}]`)
    - [Dash Punctuation](#character-classes---posix---short---dash-punctuation-ppd) (`[\p{Pd}]`)
    - [Open Punctuation](#character-classes---posix---short---open-punctuation-pps) (`[\p{Ps}]`)
    - [Close Punctuation](#character-classes---posix---short---close-punctuation-ppe) (`[\p{Pe}]`)
    - [Initial Punctuation](#character-classes---posix---short---initial-punctuation-ppi) (`[\p{Pi}]`)
    - [Final Punctuation](#character-classes---posix---short---final-punctuation-ppf) (`[\p{Pf}]`)
    - [Other Punctuation](#character-classes---posix---short---other-punctuation-ppo) (`[\p{Po}]`)
    - [Punctuation](#character-classes---posix---short---punctuation-pp) (`[\p{P}]`)
    - [Math Symbol](#character-classes---posix---short---math-symbol-psm) (`[\p{Sm}]`)
    - [Currency Symbol](#character-classes---posix---short---currency-symbol-psc) (`[\p{Sc}]`)
    - [Modifier Symbol](#character-classes---posix---short---modifier-symbol-psk) (`[\p{Sk}]`)
    - [Other Symbol](#character-classes---posix---short---other-symbol-pso) (`[\p{So}]`)
    - [Symbol](#character-classes---posix---short---symbol-ps) (`[\p{S}]`)
    - [Space Separator](#character-classes---posix---short---space-separator-pzs) (`[\p{Zs}]`)
    - [Line Separator](#character-classes---posix---short---line-separator-pzl) (`[\p{Zl}]`)
    - [Paragraph Separator](#character-classes---posix---short---paragraph-separator-pzp) (`[\p{Zp}]`)
    - [Separator](#character-classes---posix---short---separator-pz) (`[\p{Z}]`)
    - [Control](#character-classes---posix---short---control-pcc) (`[\p{Cc}]`)
    - [Format](#character-classes---posix---short---format-pcf) (`[\p{Cf}]`)
    - [Surrogate](#character-classes---posix---short---surrogate-pcs) (`[\p{Cs}]`)
    - [Private Use](#character-classes---posix---short---private-use-pco) (`[\p{Co}]`)
    - [Unassigned](#character-classes---posix---short---unassigned-pcn) (`[\p{Cn}]`)
    - [Other](#character-classes---posix---short---other-pc) (`[\p{C}]`)

---

### Character Classes - ASCII

1. [Uppercase Letter](#character-classes---ascii---uppercase-letter-upper) (`[[:upper:]]`)
2. [Lowercase Letter](#character-classes---ascii---lowercase-letter-lower) (`[[:lower:]]`)
3. [Letter And Digit](#character-classes---ascii---letter-and-digit-alnum) (`[[:alnum:]]`)
4. [Letter](#character-classes---ascii---letter-alpha) (`[[:alpha:]]`)
5. [ASCII Character](#character-classes---ascii---ascii-character-ascii) (`[[:ascii:]]`)
6. [Space And Tab](#character-classes---ascii---space-and-tab-blank) (`[[:blank:]]`)
7. [Control Character](#character-classes---ascii---control-character-cntrl) (`[[:cntrl:]]`)
8. [Digit](#character-classes---ascii---digit-digit) (`[[:digit:]]`)
9. [Visible Character](#character-classes---ascii---visible-character-graph) (`[[:graph:]]`)
10. [Printable](#character-classes---ascii---printable-print) (`[[:print:]]`)
11. [Punctuation](#character-classes---ascii---punctuation-punct) (`[[:punct:]]`)
12. [Whitespace](#character-classes---ascii---whitespace-space) (`[[:space:]]`)
13. [Word Character](#character-classes---ascii---word-character-word) (`[[:word:]]`)
14. [Hexadecimal Digit](#character-classes---ascii---hexadecimal-digit-xdigit) (`[[:xdigit:]]`)

#### Character Classes - ASCII - Uppercase Letter (`[[:upper:]]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>26<br>-0 | +0<br>26<br>-0 | +26<br>0<br>-5 | +26<br>0<br>-0 | +0<br>26<br>-1925 | +0<br>26<br>-1855 | +0<br>26<br>-1805 | +0<br>26<br>-0 | +0<br>26<br>-1882 | +0<br>26<br>-0 | +26<br>0<br>-5 |
| Go         | +0<br>26<br>-0 | —     | +0<br>26<br>-0 | +26<br>0<br>-5 | +26<br>0<br>-0 | +0<br>26<br>-1925 | +0<br>26<br>-1855 | +0<br>26<br>-1805 | +0<br>26<br>-0 | +0<br>26<br>-1882 | +0<br>26<br>-0 | +26<br>0<br>-5 |
| Haskell    | +0<br>26<br>-0 | +0<br>26<br>-0 | —       | +26<br>0<br>-5 | +26<br>0<br>-0 | +0<br>26<br>-1925 | +0<br>26<br>-1855 | +0<br>26<br>-1805 | +0<br>26<br>-0 | +0<br>26<br>-1882 | +0<br>26<br>-0 | +26<br>0<br>-5 |
| Java       | +5<br>0<br>-26 | +5<br>0<br>-26 | +5<br>0<br>-26 | —     | +5<br>0<br>-0 | +5<br>0<br>-1951 | +5<br>0<br>-1881 | +5<br>0<br>-1831 | +5<br>0<br>-26 | +5<br>0<br>-1908 | +5<br>0<br>-26 | +0<br>5<br>-0 |
| Javascript | +0<br>0<br>-26 | +0<br>0<br>-26 | +0<br>0<br>-26 | +0<br>0<br>-5 | —          | +0<br>0<br>-1951 | +0<br>0<br>-1881 | +0<br>0<br>-1831 | +0<br>0<br>-26 | +0<br>0<br>-1908 | +0<br>0<br>-26 | +0<br>0<br>-5 |
| Obj-C      | +1925<br>26<br>-0 | +1925<br>26<br>-0 | +1925<br>26<br>-0 | +1951<br>0<br>-5 | +1951<br>0<br>-0 | —     | +70<br>1881<br>-0 | +120<br>1831<br>-0 | +1925<br>26<br>-0 | +43<br>1908<br>-0 | +1925<br>26<br>-0 | +1951<br>0<br>-5 |
| Perl       | +1855<br>26<br>-0 | +1855<br>26<br>-0 | +1855<br>26<br>-0 | +1881<br>0<br>-5 | +1881<br>0<br>-0 | +0<br>1881<br>-70 | —     | +120<br>1761<br>-70 | +1855<br>26<br>-0 | +3<br>1878<br>-30 | +1855<br>26<br>-0 | +1881<br>0<br>-5 |
| PHP        | +1805<br>26<br>-0 | +1805<br>26<br>-0 | +1805<br>26<br>-0 | +1831<br>0<br>-5 | +1831<br>0<br>-0 | +0<br>1831<br>-120 | +70<br>1761<br>-120 | —     | +1805<br>26<br>-0 | +43<br>1788<br>-120 | +1805<br>26<br>-0 | +1831<br>0<br>-5 |
| Python     | +0<br>26<br>-0 | +0<br>26<br>-0 | +0<br>26<br>-0 | +26<br>0<br>-5 | +26<br>0<br>-0 | +0<br>26<br>-1925 | +0<br>26<br>-1855 | +0<br>26<br>-1805 | —      | +0<br>26<br>-1882 | +0<br>26<br>-0 | +26<br>0<br>-5 |
| Ruby       | +1882<br>26<br>-0 | +1882<br>26<br>-0 | +1882<br>26<br>-0 | +1908<br>0<br>-5 | +1908<br>0<br>-0 | +0<br>1908<br>-43 | +30<br>1878<br>-3 | +120<br>1788<br>-43 | +1882<br>26<br>-0 | —     | +1882<br>26<br>-0 | +1908<br>0<br>-5 |
| Rust       | +0<br>26<br>-0 | +0<br>26<br>-0 | +0<br>26<br>-0 | +26<br>0<br>-5 | +26<br>0<br>-0 | +0<br>26<br>-1925 | +0<br>26<br>-1855 | +0<br>26<br>-1805 | +0<br>26<br>-0 | +0<br>26<br>-1882 | —     | +26<br>0<br>-5 |
| Scala      | +5<br>0<br>-26 | +5<br>0<br>-26 | +5<br>0<br>-26 | +0<br>5<br>-0 | +5<br>0<br>-0 | +5<br>0<br>-1951 | +5<br>0<br>-1881 | +5<br>0<br>-1831 | +5<br>0<br>-26 | +5<br>0<br>-1908 | +5<br>0<br>-26 | —     |

#### Character Classes - ASCII - Lowercase Letter (`[[:lower:]]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>26<br>-0 | +0<br>26<br>-0 | +21<br>5<br>-1 | +26<br>0<br>-0 | +0<br>26<br>-2445 | +0<br>26<br>-2283 | +0<br>26<br>-2201 | +0<br>26<br>-0 | +0<br>26<br>-2314 | +0<br>26<br>-0 | +21<br>5<br>-1 |
| Go         | +0<br>26<br>-0 | —     | +0<br>26<br>-0 | +21<br>5<br>-1 | +26<br>0<br>-0 | +0<br>26<br>-2445 | +0<br>26<br>-2283 | +0<br>26<br>-2201 | +0<br>26<br>-0 | +0<br>26<br>-2314 | +0<br>26<br>-0 | +21<br>5<br>-1 |
| Haskell    | +0<br>26<br>-0 | +0<br>26<br>-0 | —       | +21<br>5<br>-1 | +26<br>0<br>-0 | +0<br>26<br>-2445 | +0<br>26<br>-2283 | +0<br>26<br>-2201 | +0<br>26<br>-0 | +0<br>26<br>-2314 | +0<br>26<br>-0 | +21<br>5<br>-1 |
| Java       | +1<br>5<br>-21 | +1<br>5<br>-21 | +1<br>5<br>-21 | —     | +6<br>0<br>-0 | +1<br>5<br>-2466 | +1<br>5<br>-2304 | +1<br>5<br>-2222 | +1<br>5<br>-21 | +1<br>5<br>-2335 | +1<br>5<br>-21 | +0<br>6<br>-0 |
| Javascript | +0<br>0<br>-26 | +0<br>0<br>-26 | +0<br>0<br>-26 | +0<br>0<br>-6 | —          | +0<br>0<br>-2471 | +0<br>0<br>-2309 | +0<br>0<br>-2227 | +0<br>0<br>-26 | +0<br>0<br>-2340 | +0<br>0<br>-26 | +0<br>0<br>-6 |
| Obj-C      | +2445<br>26<br>-0 | +2445<br>26<br>-0 | +2445<br>26<br>-0 | +2466<br>5<br>-1 | +2471<br>0<br>-0 | —     | +162<br>2309<br>-0 | +244<br>2227<br>-0 | +2445<br>26<br>-0 | +131<br>2340<br>-0 | +2445<br>26<br>-0 | +2466<br>5<br>-1 |
| Perl       | +2283<br>26<br>-0 | +2283<br>26<br>-0 | +2283<br>26<br>-0 | +2304<br>5<br>-1 | +2309<br>0<br>-0 | +0<br>2309<br>-162 | —     | +187<br>2122<br>-105 | +2283<br>26<br>-0 | +4<br>2305<br>-35 | +2283<br>26<br>-0 | +2304<br>5<br>-1 |
| PHP        | +2201<br>26<br>-0 | +2201<br>26<br>-0 | +2201<br>26<br>-0 | +2222<br>5<br>-1 | +2227<br>0<br>-0 | +0<br>2227<br>-244 | +105<br>2122<br>-187 | —     | +2201<br>26<br>-0 | +76<br>2151<br>-189 | +2201<br>26<br>-0 | +2222<br>5<br>-1 |
| Python     | +0<br>26<br>-0 | +0<br>26<br>-0 | +0<br>26<br>-0 | +21<br>5<br>-1 | +26<br>0<br>-0 | +0<br>26<br>-2445 | +0<br>26<br>-2283 | +0<br>26<br>-2201 | —      | +0<br>26<br>-2314 | +0<br>26<br>-0 | +21<br>5<br>-1 |
| Ruby       | +2314<br>26<br>-0 | +2314<br>26<br>-0 | +2314<br>26<br>-0 | +2335<br>5<br>-1 | +2340<br>0<br>-0 | +0<br>2340<br>-131 | +35<br>2305<br>-4 | +189<br>2151<br>-76 | +2314<br>26<br>-0 | —     | +2314<br>26<br>-0 | +2335<br>5<br>-1 |
| Rust       | +0<br>26<br>-0 | +0<br>26<br>-0 | +0<br>26<br>-0 | +21<br>5<br>-1 | +26<br>0<br>-0 | +0<br>26<br>-2445 | +0<br>26<br>-2283 | +0<br>26<br>-2201 | +0<br>26<br>-0 | +0<br>26<br>-2314 | —     | +21<br>5<br>-1 |
| Scala      | +1<br>5<br>-21 | +1<br>5<br>-21 | +1<br>5<br>-21 | +0<br>6<br>-0 | +6<br>0<br>-0 | +1<br>5<br>-2466 | +1<br>5<br>-2304 | +1<br>5<br>-2222 | +1<br>5<br>-21 | +1<br>5<br>-2335 | +1<br>5<br>-21 | —     |

#### Character Classes - ASCII - Letter And Digit (`[[:alnum:]]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>62<br>-0 | +0<br>62<br>-0 | +57<br>5<br>-1 | +62<br>0<br>-0 | +0<br>62<br>-133994 | +0<br>62<br>-133398 | +0<br>62<br>-133485 | +0<br>62<br>-0 | +0<br>62<br>-127824 | +0<br>62<br>-0 | +57<br>5<br>-1 |
| Go         | +0<br>62<br>-0 | —       | +0<br>62<br>-0 | +57<br>5<br>-1 | +62<br>0<br>-0 | +0<br>62<br>-133994 | +0<br>62<br>-133398 | +0<br>62<br>-133485 | +0<br>62<br>-0 | +0<br>62<br>-127824 | +0<br>62<br>-0 | +57<br>5<br>-1 |
| Haskell    | +0<br>62<br>-0 | +0<br>62<br>-0 | —       | +57<br>5<br>-1 | +62<br>0<br>-0 | +0<br>62<br>-133994 | +0<br>62<br>-133398 | +0<br>62<br>-133485 | +0<br>62<br>-0 | +0<br>62<br>-127824 | +0<br>62<br>-0 | +57<br>5<br>-1 |
| Java       | +1<br>5<br>-57 | +1<br>5<br>-57 | +1<br>5<br>-57 | —       | +6<br>0<br>-0 | +1<br>5<br>-134051 | +1<br>5<br>-133455 | +1<br>5<br>-133542 | +1<br>5<br>-57 | +1<br>5<br>-127881 | +1<br>5<br>-57 | +0<br>6<br>-0 |
| Javascript | +0<br>0<br>-62 | +0<br>0<br>-62 | +0<br>0<br>-62 | +0<br>0<br>-6 | —          | +0<br>0<br>-134056 | +0<br>0<br>-133460 | +0<br>0<br>-133547 | +0<br>0<br>-62 | +0<br>0<br>-127886 | +0<br>0<br>-62 | +0<br>0<br>-6 |
| Obj-C      | +133994<br>62<br>-0 | +133994<br>62<br>-0 | +133994<br>62<br>-0 | +134051<br>5<br>-1 | +134056<br>0<br>-0 | —       | +596<br>133460<br>-0 | +1404<br>132652<br>-895 | +133994<br>62<br>-0 | +6170<br>127886<br>-0 | +133994<br>62<br>-0 | +134051<br>5<br>-1 |
| Perl       | +133398<br>62<br>-0 | +133398<br>62<br>-0 | +133398<br>62<br>-0 | +133455<br>5<br>-1 | +133460<br>0<br>-0 | +0<br>133460<br>-596 | —       | +1398<br>132062<br>-1485 | +133398<br>62<br>-0 | +5639<br>127821<br>-65 | +133398<br>62<br>-0 | +133455<br>5<br>-1 |
| PHP        | +133485<br>62<br>-0 | +133485<br>62<br>-0 | +133485<br>62<br>-0 | +133542<br>5<br>-1 | +133547<br>0<br>-0 | +895<br>132652<br>-1404 | +1485<br>132062<br>-1398 | —       | +133485<br>62<br>-0 | +7038<br>126509<br>-1377 | +133485<br>62<br>-0 | +133542<br>5<br>-1 |
| Python     | +0<br>62<br>-0 | +0<br>62<br>-0 | +0<br>62<br>-0 | +57<br>5<br>-1 | +62<br>0<br>-0 | +0<br>62<br>-133994 | +0<br>62<br>-133398 | +0<br>62<br>-133485 | —       | +0<br>62<br>-127824 | +0<br>62<br>-0 | +57<br>5<br>-1 |
| Ruby       | +127824<br>62<br>-0 | +127824<br>62<br>-0 | +127824<br>62<br>-0 | +127881<br>5<br>-1 | +127886<br>0<br>-0 | +0<br>127886<br>-6170 | +65<br>127821<br>-5639 | +1377<br>126509<br>-7038 | +127824<br>62<br>-0 | —       | +127824<br>62<br>-0 | +127881<br>5<br>-1 |
| Rust       | +0<br>62<br>-0 | +0<br>62<br>-0 | +0<br>62<br>-0 | +57<br>5<br>-1 | +62<br>0<br>-0 | +0<br>62<br>-133994 | +0<br>62<br>-133398 | +0<br>62<br>-133485 | +0<br>62<br>-0 | +0<br>62<br>-127824 | —       | +57<br>5<br>-1 |
| Scala      | +1<br>5<br>-57 | +1<br>5<br>-57 | +1<br>5<br>-57 | +0<br>6<br>-0 | +6<br>0<br>-0 | +1<br>5<br>-134051 | +1<br>5<br>-133455 | +1<br>5<br>-133542 | +1<br>5<br>-57 | +1<br>5<br>-127881 | +1<br>5<br>-57 | —       |

#### Character Classes - ASCII - Letter (`[[:alpha:]]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>52<br>-0 | +0<br>52<br>-0 | +48<br>4<br>-1 | +52<br>0<br>-0 | +0<br>52<br>-133344 | +0<br>52<br>-132758 | +0<br>52<br>-131704 | +0<br>52<br>-0 | +0<br>52<br>-127204 | +0<br>52<br>-0 | +48<br>4<br>-1 |
| Go         | +0<br>52<br>-0 | —       | +0<br>52<br>-0 | +48<br>4<br>-1 | +52<br>0<br>-0 | +0<br>52<br>-133344 | +0<br>52<br>-132758 | +0<br>52<br>-131704 | +0<br>52<br>-0 | +0<br>52<br>-127204 | +0<br>52<br>-0 | +48<br>4<br>-1 |
| Haskell    | +0<br>52<br>-0 | +0<br>52<br>-0 | —       | +48<br>4<br>-1 | +52<br>0<br>-0 | +0<br>52<br>-133344 | +0<br>52<br>-132758 | +0<br>52<br>-131704 | +0<br>52<br>-0 | +0<br>52<br>-127204 | +0<br>52<br>-0 | +48<br>4<br>-1 |
| Java       | +1<br>4<br>-48 | +1<br>4<br>-48 | +1<br>4<br>-48 | —       | +5<br>0<br>-0 | +1<br>4<br>-133392 | +1<br>4<br>-132806 | +1<br>4<br>-131752 | +1<br>4<br>-48 | +1<br>4<br>-127252 | +1<br>4<br>-48 | +0<br>5<br>-0 |
| Javascript | +0<br>0<br>-52 | +0<br>0<br>-52 | +0<br>0<br>-52 | +0<br>0<br>-5 | —          | +0<br>0<br>-133396 | +0<br>0<br>-132810 | +0<br>0<br>-131756 | +0<br>0<br>-52 | +0<br>0<br>-127256 | +0<br>0<br>-52 | +0<br>0<br>-5 |
| Obj-C      | +133344<br>52<br>-0 | +133344<br>52<br>-0 | +133344<br>52<br>-0 | +133392<br>4<br>-1 | +133396<br>0<br>-0 | —       | +586<br>132810<br>-0 | +1640<br>131756<br>-0 | +133344<br>52<br>-0 | +6140<br>127256<br>-0 | +133344<br>52<br>-0 | +133392<br>4<br>-1 |
| Perl       | +132758<br>52<br>-0 | +132758<br>52<br>-0 | +132758<br>52<br>-0 | +132806<br>4<br>-1 | +132810<br>0<br>-0 | +0<br>132810<br>-586 | —       | +1634<br>131176<br>-580 | +132758<br>52<br>-0 | +5619<br>127191<br>-65 | +132758<br>52<br>-0 | +132806<br>4<br>-1 |
| PHP        | +131704<br>52<br>-0 | +131704<br>52<br>-0 | +131704<br>52<br>-0 | +131752<br>4<br>-1 | +131756<br>0<br>-0 | +0<br>131756<br>-1640 | +580<br>131176<br>-1634 | —       | +131704<br>52<br>-0 | +6113<br>125643<br>-1613 | +131704<br>52<br>-0 | +131752<br>4<br>-1 |
| Python     | +0<br>52<br>-0 | +0<br>52<br>-0 | +0<br>52<br>-0 | +48<br>4<br>-1 | +52<br>0<br>-0 | +0<br>52<br>-133344 | +0<br>52<br>-132758 | +0<br>52<br>-131704 | —       | +0<br>52<br>-127204 | +0<br>52<br>-0 | +48<br>4<br>-1 |
| Ruby       | +127204<br>52<br>-0 | +127204<br>52<br>-0 | +127204<br>52<br>-0 | +127252<br>4<br>-1 | +127256<br>0<br>-0 | +0<br>127256<br>-6140 | +65<br>127191<br>-5619 | +1613<br>125643<br>-6113 | +127204<br>52<br>-0 | —       | +127204<br>52<br>-0 | +127252<br>4<br>-1 |
| Rust       | +0<br>52<br>-0 | +0<br>52<br>-0 | +0<br>52<br>-0 | +48<br>4<br>-1 | +52<br>0<br>-0 | +0<br>52<br>-133344 | +0<br>52<br>-132758 | +0<br>52<br>-131704 | +0<br>52<br>-0 | +0<br>52<br>-127204 | —       | +48<br>4<br>-1 |
| Scala      | +1<br>4<br>-48 | +1<br>4<br>-48 | +1<br>4<br>-48 | +0<br>5<br>-0 | +5<br>0<br>-0 | +1<br>4<br>-133392 | +1<br>4<br>-132806 | +1<br>4<br>-131752 | +1<br>4<br>-48 | +1<br>4<br>-127252 | +1<br>4<br>-48 | —       |

#### Character Classes - ASCII - ASCII Character (`[[:ascii:]]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>0<br>-128 | +0<br>0<br>-127 | +0<br>0<br>-5 | +0<br>0<br>-0 | +0<br>0<br>-128 | +0<br>0<br>-128 | +0<br>0<br>-128 | +0<br>0<br>-128 | +0<br>0<br>-128 | +0<br>0<br>-128 | +0<br>0<br>-5 |
| Go         | +128<br>0<br>-0 | —    | +1<br>127<br>-0 | +123<br>5<br>-0 | +128<br>0<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +123<br>5<br>-0 |
| Haskell    | +127<br>0<br>-0 | +0<br>127<br>-1 | —       | +122<br>5<br>-0 | +127<br>0<br>-0 | +0<br>127<br>-1 | +0<br>127<br>-1 | +0<br>127<br>-1 | +0<br>127<br>-1 | +0<br>127<br>-1 | +0<br>127<br>-1 | +122<br>5<br>-0 |
| Java       | +5<br>0<br>-0 | +0<br>5<br>-123 | +0<br>5<br>-122 | —    | +5<br>0<br>-0 | +0<br>5<br>-123 | +0<br>5<br>-123 | +0<br>5<br>-123 | +0<br>5<br>-123 | +0<br>5<br>-123 | +0<br>5<br>-123 | +0<br>5<br>-0 |
| Javascript | +0<br>0<br>-0 | +0<br>0<br>-128 | +0<br>0<br>-127 | +0<br>0<br>-5 | —          | +0<br>0<br>-128 | +0<br>0<br>-128 | +0<br>0<br>-128 | +0<br>0<br>-128 | +0<br>0<br>-128 | +0<br>0<br>-128 | +0<br>0<br>-5 |
| Obj-C      | +128<br>0<br>-0 | +0<br>128<br>-0 | +1<br>127<br>-0 | +123<br>5<br>-0 | +128<br>0<br>-0 | —     | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +123<br>5<br>-0 |
| Perl       | +128<br>0<br>-0 | +0<br>128<br>-0 | +1<br>127<br>-0 | +123<br>5<br>-0 | +128<br>0<br>-0 | +0<br>128<br>-0 | —    | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +123<br>5<br>-0 |
| PHP        | +128<br>0<br>-0 | +0<br>128<br>-0 | +1<br>127<br>-0 | +123<br>5<br>-0 | +128<br>0<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | —    | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +123<br>5<br>-0 |
| Python     | +128<br>0<br>-0 | +0<br>128<br>-0 | +1<br>127<br>-0 | +123<br>5<br>-0 | +128<br>0<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | —      | +0<br>128<br>-0 | +0<br>128<br>-0 | +123<br>5<br>-0 |
| Ruby       | +128<br>0<br>-0 | +0<br>128<br>-0 | +1<br>127<br>-0 | +123<br>5<br>-0 | +128<br>0<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | —    | +0<br>128<br>-0 | +123<br>5<br>-0 |
| Rust       | +128<br>0<br>-0 | +0<br>128<br>-0 | +1<br>127<br>-0 | +123<br>5<br>-0 | +128<br>0<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | +0<br>128<br>-0 | —    | +123<br>5<br>-0 |
| Scala      | +5<br>0<br>-0 | +0<br>5<br>-123 | +0<br>5<br>-122 | +0<br>5<br>-0 | +5<br>0<br>-0 | +0<br>5<br>-123 | +0<br>5<br>-123 | +0<br>5<br>-123 | +0<br>5<br>-123 | +0<br>5<br>-123 | +0<br>5<br>-123 | —     |

#### Character Classes - ASCII - Space And Tab (`[[:blank:]]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>2<br>-0 | +0<br>2<br>-0 | +2<br>0<br>-6 | +2<br>0<br>-0 | +0<br>2<br>-16 | +0<br>2<br>-15 | +0<br>2<br>-17 | +0<br>2<br>-0 | +0<br>2<br>-16 | +0<br>2<br>-0 | +2<br>0<br>-6 |
| Go         | +0<br>2<br>-0 | —   | +0<br>2<br>-0 | +2<br>0<br>-6 | +2<br>0<br>-0 | +0<br>2<br>-16 | +0<br>2<br>-15 | +0<br>2<br>-17 | +0<br>2<br>-0 | +0<br>2<br>-16 | +0<br>2<br>-0 | +2<br>0<br>-6 |
| Haskell    | +0<br>2<br>-0 | +0<br>2<br>-0 | —       | +2<br>0<br>-6 | +2<br>0<br>-0 | +0<br>2<br>-16 | +0<br>2<br>-15 | +0<br>2<br>-17 | +0<br>2<br>-0 | +0<br>2<br>-16 | +0<br>2<br>-0 | +2<br>0<br>-6 |
| Java       | +6<br>0<br>-2 | +6<br>0<br>-2 | +6<br>0<br>-2 | —    | +6<br>0<br>-0 | +6<br>0<br>-18 | +6<br>0<br>-17 | +6<br>0<br>-19 | +6<br>0<br>-2 | +6<br>0<br>-18 | +6<br>0<br>-2 | +0<br>6<br>-0 |
| Javascript | +0<br>0<br>-2 | +0<br>0<br>-2 | +0<br>0<br>-2 | +0<br>0<br>-6 | —          | +0<br>0<br>-18 | +0<br>0<br>-17 | +0<br>0<br>-19 | +0<br>0<br>-2 | +0<br>0<br>-18 | +0<br>0<br>-2 | +0<br>0<br>-6 |
| Obj-C      | +16<br>2<br>-0 | +16<br>2<br>-0 | +16<br>2<br>-0 | +18<br>0<br>-6 | +18<br>0<br>-0 | —     | +1<br>17<br>-0 | +0<br>18<br>-1 | +16<br>2<br>-0 | +0<br>18<br>-0 | +16<br>2<br>-0 | +18<br>0<br>-6 |
| Perl       | +15<br>2<br>-0 | +15<br>2<br>-0 | +15<br>2<br>-0 | +17<br>0<br>-6 | +17<br>0<br>-0 | +0<br>17<br>-1 | —    | +0<br>17<br>-2 | +15<br>2<br>-0 | +0<br>17<br>-1 | +15<br>2<br>-0 | +17<br>0<br>-6 |
| PHP        | +17<br>2<br>-0 | +17<br>2<br>-0 | +17<br>2<br>-0 | +19<br>0<br>-6 | +19<br>0<br>-0 | +1<br>18<br>-0 | +2<br>17<br>-0 | —   | +17<br>2<br>-0 | +1<br>18<br>-0 | +17<br>2<br>-0 | +19<br>0<br>-6 |
| Python     | +0<br>2<br>-0 | +0<br>2<br>-0 | +0<br>2<br>-0 | +2<br>0<br>-6 | +2<br>0<br>-0 | +0<br>2<br>-16 | +0<br>2<br>-15 | +0<br>2<br>-17 | —      | +0<br>2<br>-16 | +0<br>2<br>-0 | +2<br>0<br>-6 |
| Ruby       | +16<br>2<br>-0 | +16<br>2<br>-0 | +16<br>2<br>-0 | +18<br>0<br>-6 | +18<br>0<br>-0 | +0<br>18<br>-0 | +1<br>17<br>-0 | +0<br>18<br>-1 | +16<br>2<br>-0 | —    | +16<br>2<br>-0 | +18<br>0<br>-6 |
| Rust       | +0<br>2<br>-0 | +0<br>2<br>-0 | +0<br>2<br>-0 | +2<br>0<br>-6 | +2<br>0<br>-0 | +0<br>2<br>-16 | +0<br>2<br>-15 | +0<br>2<br>-17 | +0<br>2<br>-0 | +0<br>2<br>-16 | —    | +2<br>0<br>-6 |
| Scala      | +6<br>0<br>-2 | +6<br>0<br>-2 | +6<br>0<br>-2 | +0<br>6<br>-0 | +6<br>0<br>-0 | +6<br>0<br>-18 | +6<br>0<br>-17 | +6<br>0<br>-19 | +6<br>0<br>-2 | +6<br>0<br>-18 | +6<br>0<br>-2 | —     |

#### Character Classes - ASCII - Control Character (`[[:cntrl:]]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>33<br>-0 | +1<br>32<br>-0 | +33<br>0<br>-6 | +33<br>0<br>-0 | +0<br>33<br>-32 | +0<br>33<br>-0 | +0<br>33<br>-32 | +0<br>33<br>-0 | +0<br>33<br>-32 | +0<br>33<br>-0 | +33<br>0<br>-6 |
| Go         | +0<br>33<br>-0 | —   | +1<br>32<br>-0 | +33<br>0<br>-6 | +33<br>0<br>-0 | +0<br>33<br>-32 | +0<br>33<br>-0 | +0<br>33<br>-32 | +0<br>33<br>-0 | +0<br>33<br>-32 | +0<br>33<br>-0 | +33<br>0<br>-6 |
| Haskell    | +0<br>32<br>-1 | +0<br>32<br>-1 | —       | +32<br>0<br>-6 | +32<br>0<br>-0 | +0<br>32<br>-33 | +0<br>32<br>-1 | +0<br>32<br>-33 | +0<br>32<br>-1 | +0<br>32<br>-33 | +0<br>32<br>-1 | +32<br>0<br>-6 |
| Java       | +6<br>0<br>-33 | +6<br>0<br>-33 | +6<br>0<br>-32 | —    | +6<br>0<br>-0 | +6<br>0<br>-65 | +6<br>0<br>-33 | +6<br>0<br>-65 | +6<br>0<br>-33 | +6<br>0<br>-65 | +6<br>0<br>-33 | +0<br>6<br>-0 |
| Javascript | +0<br>0<br>-33 | +0<br>0<br>-33 | +0<br>0<br>-32 | +0<br>0<br>-6 | —          | +0<br>0<br>-65 | +0<br>0<br>-33 | +0<br>0<br>-65 | +0<br>0<br>-33 | +0<br>0<br>-65 | +0<br>0<br>-33 | +0<br>0<br>-6 |
| Obj-C      | +32<br>33<br>-0 | +32<br>33<br>-0 | +33<br>32<br>-0 | +65<br>0<br>-6 | +65<br>0<br>-0 | —     | +32<br>33<br>-0 | +0<br>65<br>-0 | +32<br>33<br>-0 | +0<br>65<br>-0 | +32<br>33<br>-0 | +65<br>0<br>-6 |
| Perl       | +0<br>33<br>-0 | +0<br>33<br>-0 | +1<br>32<br>-0 | +33<br>0<br>-6 | +33<br>0<br>-0 | +0<br>33<br>-32 | —    | +0<br>33<br>-32 | +0<br>33<br>-0 | +0<br>33<br>-32 | +0<br>33<br>-0 | +33<br>0<br>-6 |
| PHP        | +32<br>33<br>-0 | +32<br>33<br>-0 | +33<br>32<br>-0 | +65<br>0<br>-6 | +65<br>0<br>-0 | +0<br>65<br>-0 | +32<br>33<br>-0 | —   | +32<br>33<br>-0 | +0<br>65<br>-0 | +32<br>33<br>-0 | +65<br>0<br>-6 |
| Python     | +0<br>33<br>-0 | +0<br>33<br>-0 | +1<br>32<br>-0 | +33<br>0<br>-6 | +33<br>0<br>-0 | +0<br>33<br>-32 | +0<br>33<br>-0 | +0<br>33<br>-32 | —      | +0<br>33<br>-32 | +0<br>33<br>-0 | +33<br>0<br>-6 |
| Ruby       | +32<br>33<br>-0 | +32<br>33<br>-0 | +33<br>32<br>-0 | +65<br>0<br>-6 | +65<br>0<br>-0 | +0<br>65<br>-0 | +32<br>33<br>-0 | +0<br>65<br>-0 | +32<br>33<br>-0 | —    | +32<br>33<br>-0 | +65<br>0<br>-6 |
| Rust       | +0<br>33<br>-0 | +0<br>33<br>-0 | +1<br>32<br>-0 | +33<br>0<br>-6 | +33<br>0<br>-0 | +0<br>33<br>-32 | +0<br>33<br>-0 | +0<br>33<br>-32 | +0<br>33<br>-0 | +0<br>33<br>-32 | —    | +33<br>0<br>-6 |
| Scala      | +6<br>0<br>-33 | +6<br>0<br>-33 | +6<br>0<br>-32 | +0<br>6<br>-0 | +6<br>0<br>-0 | +6<br>0<br>-65 | +6<br>0<br>-33 | +6<br>0<br>-65 | +6<br>0<br>-33 | +6<br>0<br>-65 | +6<br>0<br>-33 | —     |

#### Character Classes - ASCII - Digit (`[[:digit:]]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>10<br>-0 | +0<br>10<br>-0 | +10<br>0<br>-5 | +10<br>0<br>-0 | +0<br>10<br>-650 | +0<br>10<br>-640 | +0<br>10<br>-650 | +0<br>10<br>-0 | +0<br>10<br>-620 | +0<br>10<br>-0 | +10<br>0<br>-5 |
| Go         | +0<br>10<br>-0 | —    | +0<br>10<br>-0 | +10<br>0<br>-5 | +10<br>0<br>-0 | +0<br>10<br>-650 | +0<br>10<br>-640 | +0<br>10<br>-650 | +0<br>10<br>-0 | +0<br>10<br>-620 | +0<br>10<br>-0 | +10<br>0<br>-5 |
| Haskell    | +0<br>10<br>-0 | +0<br>10<br>-0 | —       | +10<br>0<br>-5 | +10<br>0<br>-0 | +0<br>10<br>-650 | +0<br>10<br>-640 | +0<br>10<br>-650 | +0<br>10<br>-0 | +0<br>10<br>-620 | +0<br>10<br>-0 | +10<br>0<br>-5 |
| Java       | +5<br>0<br>-10 | +5<br>0<br>-10 | +5<br>0<br>-10 | —    | +5<br>0<br>-0 | +5<br>0<br>-660 | +5<br>0<br>-650 | +5<br>0<br>-660 | +5<br>0<br>-10 | +5<br>0<br>-630 | +5<br>0<br>-10 | +0<br>5<br>-0 |
| Javascript | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-5 | —          | +0<br>0<br>-660 | +0<br>0<br>-650 | +0<br>0<br>-660 | +0<br>0<br>-10 | +0<br>0<br>-630 | +0<br>0<br>-10 | +0<br>0<br>-5 |
| Obj-C      | +650<br>10<br>-0 | +650<br>10<br>-0 | +650<br>10<br>-0 | +660<br>0<br>-5 | +660<br>0<br>-0 | —     | +10<br>650<br>-0 | +0<br>660<br>-0 | +650<br>10<br>-0 | +30<br>630<br>-0 | +650<br>10<br>-0 | +660<br>0<br>-5 |
| Perl       | +640<br>10<br>-0 | +640<br>10<br>-0 | +640<br>10<br>-0 | +650<br>0<br>-5 | +650<br>0<br>-0 | +0<br>650<br>-10 | —    | +0<br>650<br>-10 | +640<br>10<br>-0 | +20<br>630<br>-0 | +640<br>10<br>-0 | +650<br>0<br>-5 |
| PHP        | +650<br>10<br>-0 | +650<br>10<br>-0 | +650<br>10<br>-0 | +660<br>0<br>-5 | +660<br>0<br>-0 | +0<br>660<br>-0 | +10<br>650<br>-0 | —    | +650<br>10<br>-0 | +30<br>630<br>-0 | +650<br>10<br>-0 | +660<br>0<br>-5 |
| Python     | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +10<br>0<br>-5 | +10<br>0<br>-0 | +0<br>10<br>-650 | +0<br>10<br>-640 | +0<br>10<br>-650 | —      | +0<br>10<br>-620 | +0<br>10<br>-0 | +10<br>0<br>-5 |
| Ruby       | +620<br>10<br>-0 | +620<br>10<br>-0 | +620<br>10<br>-0 | +630<br>0<br>-5 | +630<br>0<br>-0 | +0<br>630<br>-30 | +0<br>630<br>-20 | +0<br>630<br>-30 | +620<br>10<br>-0 | —    | +620<br>10<br>-0 | +630<br>0<br>-5 |
| Rust       | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +10<br>0<br>-5 | +10<br>0<br>-0 | +0<br>10<br>-650 | +0<br>10<br>-640 | +0<br>10<br>-650 | +0<br>10<br>-0 | +0<br>10<br>-620 | —    | +10<br>0<br>-5 |
| Scala      | +5<br>0<br>-10 | +5<br>0<br>-10 | +5<br>0<br>-10 | +0<br>5<br>-0 | +5<br>0<br>-0 | +5<br>0<br>-660 | +5<br>0<br>-650 | +5<br>0<br>-660 | +5<br>0<br>-10 | +5<br>0<br>-630 | +5<br>0<br>-10 | —     |

#### Character Classes - ASCII - Visible Character (`[[:graph:]]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>94<br>-0 | +0<br>94<br>-0 | +88<br>6<br>-0 | +94<br>0<br>-0 | +0<br>94<br>-282052 | +0<br>94<br>-281119 | +0<br>94<br>-144578 | +0<br>94<br>-0 | +0<br>94<br>-275284 | +0<br>94<br>-0 | +88<br>6<br>-0 |
| Go         | +0<br>94<br>-0 | —       | +0<br>94<br>-0 | +88<br>6<br>-0 | +94<br>0<br>-0 | +0<br>94<br>-282052 | +0<br>94<br>-281119 | +0<br>94<br>-144578 | +0<br>94<br>-0 | +0<br>94<br>-275284 | +0<br>94<br>-0 | +88<br>6<br>-0 |
| Haskell    | +0<br>94<br>-0 | +0<br>94<br>-0 | —       | +88<br>6<br>-0 | +94<br>0<br>-0 | +0<br>94<br>-282052 | +0<br>94<br>-281119 | +0<br>94<br>-144578 | +0<br>94<br>-0 | +0<br>94<br>-275284 | +0<br>94<br>-0 | +88<br>6<br>-0 |
| Java       | +0<br>6<br>-88 | +0<br>6<br>-88 | +0<br>6<br>-88 | —       | +6<br>0<br>-0 | +0<br>6<br>-282140 | +0<br>6<br>-281207 | +0<br>6<br>-144666 | +0<br>6<br>-88 | +0<br>6<br>-275372 | +0<br>6<br>-88 | +0<br>6<br>-0 |
| Javascript | +0<br>0<br>-94 | +0<br>0<br>-94 | +0<br>0<br>-94 | +0<br>0<br>-6 | —          | +0<br>0<br>-282146 | +0<br>0<br>-281213 | +0<br>0<br>-144672 | +0<br>0<br>-94 | +0<br>0<br>-275378 | +0<br>0<br>-94 | +0<br>0<br>-6 |
| Obj-C      | +282052<br>94<br>-0 | +282052<br>94<br>-0 | +282052<br>94<br>-0 | +282140<br>6<br>-0 | +282146<br>0<br>-0 | —       | +933<br>281213<br>-0 | +137474<br>144672<br>-0 | +282052<br>94<br>-0 | +6768<br>275378<br>-0 | +282052<br>94<br>-0 | +282140<br>6<br>-0 |
| Perl       | +281119<br>94<br>-0 | +281119<br>94<br>-0 | +281119<br>94<br>-0 | +281207<br>6<br>-0 | +281213<br>0<br>-0 | +0<br>281213<br>-933 | —       | +137474<br>143739<br>-933 | +281119<br>94<br>-0 | +5930<br>275283<br>-95 | +281119<br>94<br>-0 | +281207<br>6<br>-0 |
| PHP        | +144578<br>94<br>-0 | +144578<br>94<br>-0 | +144578<br>94<br>-0 | +144666<br>6<br>-0 | +144672<br>0<br>-0 | +0<br>144672<br>-137474 | +933<br>143739<br>-137474 | —       | +144578<br>94<br>-0 | +6768<br>137904<br>-137474 | +144578<br>94<br>-0 | +144666<br>6<br>-0 |
| Python     | +0<br>94<br>-0 | +0<br>94<br>-0 | +0<br>94<br>-0 | +88<br>6<br>-0 | +94<br>0<br>-0 | +0<br>94<br>-282052 | +0<br>94<br>-281119 | +0<br>94<br>-144578 | —       | +0<br>94<br>-275284 | +0<br>94<br>-0 | +88<br>6<br>-0 |
| Ruby       | +275284<br>94<br>-0 | +275284<br>94<br>-0 | +275284<br>94<br>-0 | +275372<br>6<br>-0 | +275378<br>0<br>-0 | +0<br>275378<br>-6768 | +95<br>275283<br>-5930 | +137474<br>137904<br>-6768 | +275284<br>94<br>-0 | —       | +275284<br>94<br>-0 | +275372<br>6<br>-0 |
| Rust       | +0<br>94<br>-0 | +0<br>94<br>-0 | +0<br>94<br>-0 | +88<br>6<br>-0 | +94<br>0<br>-0 | +0<br>94<br>-282052 | +0<br>94<br>-281119 | +0<br>94<br>-144578 | +0<br>94<br>-0 | +0<br>94<br>-275284 | —       | +88<br>6<br>-0 |
| Scala      | +0<br>6<br>-88 | +0<br>6<br>-88 | +0<br>6<br>-88 | +0<br>6<br>-0 | +6<br>0<br>-0 | +0<br>6<br>-282140 | +0<br>6<br>-281207 | +0<br>6<br>-144666 | +0<br>6<br>-88 | +0<br>6<br>-275372 | +0<br>6<br>-88 | —       |

#### Character Classes - ASCII - Printable (`[[:print:]]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>95<br>-0 | +0<br>95<br>-0 | +89<br>6<br>-0 | +95<br>0<br>-0 | +0<br>95<br>-282068 | +0<br>95<br>-281134 | +0<br>95<br>-144595 | +0<br>95<br>-0 | +0<br>95<br>-275300 | +0<br>95<br>-0 | +89<br>6<br>-0 |
| Go         | +0<br>95<br>-0 | —       | +0<br>95<br>-0 | +89<br>6<br>-0 | +95<br>0<br>-0 | +0<br>95<br>-282068 | +0<br>95<br>-281134 | +0<br>95<br>-144595 | +0<br>95<br>-0 | +0<br>95<br>-275300 | +0<br>95<br>-0 | +89<br>6<br>-0 |
| Haskell    | +0<br>95<br>-0 | +0<br>95<br>-0 | —       | +89<br>6<br>-0 | +95<br>0<br>-0 | +0<br>95<br>-282068 | +0<br>95<br>-281134 | +0<br>95<br>-144595 | +0<br>95<br>-0 | +0<br>95<br>-275300 | +0<br>95<br>-0 | +89<br>6<br>-0 |
| Java       | +0<br>6<br>-89 | +0<br>6<br>-89 | +0<br>6<br>-89 | —       | +6<br>0<br>-0 | +0<br>6<br>-282157 | +0<br>6<br>-281223 | +0<br>6<br>-144684 | +0<br>6<br>-89 | +0<br>6<br>-275389 | +0<br>6<br>-89 | +0<br>6<br>-0 |
| Javascript | +0<br>0<br>-95 | +0<br>0<br>-95 | +0<br>0<br>-95 | +0<br>0<br>-6 | —          | +0<br>0<br>-282163 | +0<br>0<br>-281229 | +0<br>0<br>-144690 | +0<br>0<br>-95 | +0<br>0<br>-275395 | +0<br>0<br>-95 | +0<br>0<br>-6 |
| Obj-C      | +282068<br>95<br>-0 | +282068<br>95<br>-0 | +282068<br>95<br>-0 | +282157<br>6<br>-0 | +282163<br>0<br>-0 | —       | +934<br>281229<br>-0 | +137473<br>144690<br>-0 | +282068<br>95<br>-0 | +6768<br>275395<br>-0 | +282068<br>95<br>-0 | +282157<br>6<br>-0 |
| Perl       | +281134<br>95<br>-0 | +281134<br>95<br>-0 | +281134<br>95<br>-0 | +281223<br>6<br>-0 | +281229<br>0<br>-0 | +0<br>281229<br>-934 | —       | +137473<br>143756<br>-934 | +281134<br>95<br>-0 | +5930<br>275299<br>-96 | +281134<br>95<br>-0 | +281223<br>6<br>-0 |
| PHP        | +144595<br>95<br>-0 | +144595<br>95<br>-0 | +144595<br>95<br>-0 | +144684<br>6<br>-0 | +144690<br>0<br>-0 | +0<br>144690<br>-137473 | +934<br>143756<br>-137473 | —       | +144595<br>95<br>-0 | +6768<br>137922<br>-137473 | +144595<br>95<br>-0 | +144684<br>6<br>-0 |
| Python     | +0<br>95<br>-0 | +0<br>95<br>-0 | +0<br>95<br>-0 | +89<br>6<br>-0 | +95<br>0<br>-0 | +0<br>95<br>-282068 | +0<br>95<br>-281134 | +0<br>95<br>-144595 | —       | +0<br>95<br>-275300 | +0<br>95<br>-0 | +89<br>6<br>-0 |
| Ruby       | +275300<br>95<br>-0 | +275300<br>95<br>-0 | +275300<br>95<br>-0 | +275389<br>6<br>-0 | +275395<br>0<br>-0 | +0<br>275395<br>-6768 | +96<br>275299<br>-5930 | +137473<br>137922<br>-6768 | +275300<br>95<br>-0 | —       | +275300<br>95<br>-0 | +275389<br>6<br>-0 |
| Rust       | +0<br>95<br>-0 | +0<br>95<br>-0 | +0<br>95<br>-0 | +89<br>6<br>-0 | +95<br>0<br>-0 | +0<br>95<br>-282068 | +0<br>95<br>-281134 | +0<br>95<br>-144595 | +0<br>95<br>-0 | +0<br>95<br>-275300 | —       | +89<br>6<br>-0 |
| Scala      | +0<br>6<br>-89 | +0<br>6<br>-89 | +0<br>6<br>-89 | +0<br>6<br>-0 | +6<br>0<br>-0 | +0<br>6<br>-282157 | +0<br>6<br>-281223 | +0<br>6<br>-144684 | +0<br>6<br>-89 | +0<br>6<br>-275389 | +0<br>6<br>-89 | —       |

#### Character Classes - ASCII - Punctuation (`[[:punct:]]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>32<br>-0 | +0<br>32<br>-0 | +31<br>1<br>-5 | +32<br>0<br>-0 | +9<br>23<br>-796 | +0<br>32<br>-768 | +0<br>32<br>-796 | +0<br>32<br>-0 | +0<br>32<br>-769 | +0<br>32<br>-0 | +31<br>1<br>-5 |
| Go         | +0<br>32<br>-0 | —    | +0<br>32<br>-0 | +31<br>1<br>-5 | +32<br>0<br>-0 | +9<br>23<br>-796 | +0<br>32<br>-768 | +0<br>32<br>-796 | +0<br>32<br>-0 | +0<br>32<br>-769 | +0<br>32<br>-0 | +31<br>1<br>-5 |
| Haskell    | +0<br>32<br>-0 | +0<br>32<br>-0 | —       | +31<br>1<br>-5 | +32<br>0<br>-0 | +9<br>23<br>-796 | +0<br>32<br>-768 | +0<br>32<br>-796 | +0<br>32<br>-0 | +0<br>32<br>-769 | +0<br>32<br>-0 | +31<br>1<br>-5 |
| Java       | +5<br>1<br>-31 | +5<br>1<br>-31 | +5<br>1<br>-31 | —    | +6<br>0<br>-0 | +5<br>1<br>-818 | +5<br>1<br>-799 | +5<br>1<br>-827 | +5<br>1<br>-31 | +5<br>1<br>-800 | +5<br>1<br>-31 | +0<br>6<br>-0 |
| Javascript | +0<br>0<br>-32 | +0<br>0<br>-32 | +0<br>0<br>-32 | +0<br>0<br>-6 | —          | +0<br>0<br>-819 | +0<br>0<br>-800 | +0<br>0<br>-828 | +0<br>0<br>-32 | +0<br>0<br>-801 | +0<br>0<br>-32 | +0<br>0<br>-6 |
| Obj-C      | +796<br>23<br>-9 | +796<br>23<br>-9 | +796<br>23<br>-9 | +818<br>1<br>-5 | +819<br>0<br>-0 | —     | +28<br>791<br>-9 | +0<br>819<br>-9 | +796<br>23<br>-9 | +27<br>792<br>-9 | +796<br>23<br>-9 | +818<br>1<br>-5 |
| Perl       | +768<br>32<br>-0 | +768<br>32<br>-0 | +768<br>32<br>-0 | +799<br>1<br>-5 | +800<br>0<br>-0 | +9<br>791<br>-28 | —    | +0<br>800<br>-28 | +768<br>32<br>-0 | +6<br>794<br>-7 | +768<br>32<br>-0 | +799<br>1<br>-5 |
| PHP        | +796<br>32<br>-0 | +796<br>32<br>-0 | +796<br>32<br>-0 | +827<br>1<br>-5 | +828<br>0<br>-0 | +9<br>819<br>-0 | +28<br>800<br>-0 | —    | +796<br>32<br>-0 | +27<br>801<br>-0 | +796<br>32<br>-0 | +827<br>1<br>-5 |
| Python     | +0<br>32<br>-0 | +0<br>32<br>-0 | +0<br>32<br>-0 | +31<br>1<br>-5 | +32<br>0<br>-0 | +9<br>23<br>-796 | +0<br>32<br>-768 | +0<br>32<br>-796 | —      | +0<br>32<br>-769 | +0<br>32<br>-0 | +31<br>1<br>-5 |
| Ruby       | +769<br>32<br>-0 | +769<br>32<br>-0 | +769<br>32<br>-0 | +800<br>1<br>-5 | +801<br>0<br>-0 | +9<br>792<br>-27 | +7<br>794<br>-6 | +0<br>801<br>-27 | +769<br>32<br>-0 | —    | +769<br>32<br>-0 | +800<br>1<br>-5 |
| Rust       | +0<br>32<br>-0 | +0<br>32<br>-0 | +0<br>32<br>-0 | +31<br>1<br>-5 | +32<br>0<br>-0 | +9<br>23<br>-796 | +0<br>32<br>-768 | +0<br>32<br>-796 | +0<br>32<br>-0 | +0<br>32<br>-769 | —    | +31<br>1<br>-5 |
| Scala      | +5<br>1<br>-31 | +5<br>1<br>-31 | +5<br>1<br>-31 | +0<br>6<br>-0 | +6<br>0<br>-0 | +5<br>1<br>-818 | +5<br>1<br>-799 | +5<br>1<br>-827 | +5<br>1<br>-31 | +5<br>1<br>-800 | +5<br>1<br>-31 | —     |

#### Character Classes - ASCII - Whitespace (`[[:space:]]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>6<br>-0 | +0<br>6<br>-0 | +6<br>0<br>-6 | +6<br>0<br>-0 | +0<br>6<br>-19 | +0<br>6<br>-17 | +0<br>6<br>-20 | +0<br>6<br>-0 | +0<br>6<br>-19 | +0<br>6<br>-0 | +6<br>0<br>-6 |
| Go         | +0<br>6<br>-0 | —   | +0<br>6<br>-0 | +6<br>0<br>-6 | +6<br>0<br>-0 | +0<br>6<br>-19 | +0<br>6<br>-17 | +0<br>6<br>-20 | +0<br>6<br>-0 | +0<br>6<br>-19 | +0<br>6<br>-0 | +6<br>0<br>-6 |
| Haskell    | +0<br>6<br>-0 | +0<br>6<br>-0 | —       | +6<br>0<br>-6 | +6<br>0<br>-0 | +0<br>6<br>-19 | +0<br>6<br>-17 | +0<br>6<br>-20 | +0<br>6<br>-0 | +0<br>6<br>-19 | +0<br>6<br>-0 | +6<br>0<br>-6 |
| Java       | +6<br>0<br>-6 | +6<br>0<br>-6 | +6<br>0<br>-6 | —    | +6<br>0<br>-0 | +6<br>0<br>-25 | +6<br>0<br>-23 | +6<br>0<br>-26 | +6<br>0<br>-6 | +6<br>0<br>-25 | +6<br>0<br>-6 | +0<br>6<br>-0 |
| Javascript | +0<br>0<br>-6 | +0<br>0<br>-6 | +0<br>0<br>-6 | +0<br>0<br>-6 | —          | +0<br>0<br>-25 | +0<br>0<br>-23 | +0<br>0<br>-26 | +0<br>0<br>-6 | +0<br>0<br>-25 | +0<br>0<br>-6 | +0<br>0<br>-6 |
| Obj-C      | +19<br>6<br>-0 | +19<br>6<br>-0 | +19<br>6<br>-0 | +25<br>0<br>-6 | +25<br>0<br>-0 | —     | +2<br>23<br>-0 | +0<br>25<br>-1 | +19<br>6<br>-0 | +0<br>25<br>-0 | +19<br>6<br>-0 | +25<br>0<br>-6 |
| Perl       | +17<br>6<br>-0 | +17<br>6<br>-0 | +17<br>6<br>-0 | +23<br>0<br>-6 | +23<br>0<br>-0 | +0<br>23<br>-2 | —    | +0<br>23<br>-3 | +17<br>6<br>-0 | +0<br>23<br>-2 | +17<br>6<br>-0 | +23<br>0<br>-6 |
| PHP        | +20<br>6<br>-0 | +20<br>6<br>-0 | +20<br>6<br>-0 | +26<br>0<br>-6 | +26<br>0<br>-0 | +1<br>25<br>-0 | +3<br>23<br>-0 | —   | +20<br>6<br>-0 | +1<br>25<br>-0 | +20<br>6<br>-0 | +26<br>0<br>-6 |
| Python     | +0<br>6<br>-0 | +0<br>6<br>-0 | +0<br>6<br>-0 | +6<br>0<br>-6 | +6<br>0<br>-0 | +0<br>6<br>-19 | +0<br>6<br>-17 | +0<br>6<br>-20 | —      | +0<br>6<br>-19 | +0<br>6<br>-0 | +6<br>0<br>-6 |
| Ruby       | +19<br>6<br>-0 | +19<br>6<br>-0 | +19<br>6<br>-0 | +25<br>0<br>-6 | +25<br>0<br>-0 | +0<br>25<br>-0 | +2<br>23<br>-0 | +0<br>25<br>-1 | +19<br>6<br>-0 | —    | +19<br>6<br>-0 | +25<br>0<br>-6 |
| Rust       | +0<br>6<br>-0 | +0<br>6<br>-0 | +0<br>6<br>-0 | +6<br>0<br>-6 | +6<br>0<br>-0 | +0<br>6<br>-19 | +0<br>6<br>-17 | +0<br>6<br>-20 | +0<br>6<br>-0 | +0<br>6<br>-19 | —    | +6<br>0<br>-6 |
| Scala      | +6<br>0<br>-6 | +6<br>0<br>-6 | +6<br>0<br>-6 | +0<br>6<br>-0 | +6<br>0<br>-0 | +6<br>0<br>-25 | +6<br>0<br>-23 | +6<br>0<br>-26 | +6<br>0<br>-6 | +6<br>0<br>-25 | +6<br>0<br>-6 | —     |

#### Character Classes - ASCII - Word Character (`[[:word:]]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-63 | +0<br>0<br>-63 | +0<br>0<br>-5 | +0<br>0<br>-0 | +0<br>0<br>-135202 | +0<br>0<br>-134499 | +0<br>0<br>-133548 | +0<br>0<br>-63 | +0<br>0<br>-128917 | +0<br>0<br>-63 | +0<br>0<br>-5 |
| Go         | +63<br>0<br>-0 | —       | +0<br>63<br>-0 | +59<br>4<br>-1 | +63<br>0<br>-0 | +0<br>63<br>-135139 | +0<br>63<br>-134436 | +0<br>63<br>-133485 | +0<br>63<br>-0 | +0<br>63<br>-128854 | +0<br>63<br>-0 | +59<br>4<br>-1 |
| Haskell    | +63<br>0<br>-0 | +0<br>63<br>-0 | —       | +59<br>4<br>-1 | +63<br>0<br>-0 | +0<br>63<br>-135139 | +0<br>63<br>-134436 | +0<br>63<br>-133485 | +0<br>63<br>-0 | +0<br>63<br>-128854 | +0<br>63<br>-0 | +59<br>4<br>-1 |
| Java       | +5<br>0<br>-0 | +1<br>4<br>-59 | +1<br>4<br>-59 | —       | +5<br>0<br>-0 | +1<br>4<br>-135198 | +1<br>4<br>-134495 | +1<br>4<br>-133544 | +1<br>4<br>-59 | +1<br>4<br>-128913 | +1<br>4<br>-59 | +0<br>5<br>-0 |
| Javascript | +0<br>0<br>-0 | +0<br>0<br>-63 | +0<br>0<br>-63 | +0<br>0<br>-5 | —          | +0<br>0<br>-135202 | +0<br>0<br>-134499 | +0<br>0<br>-133548 | +0<br>0<br>-63 | +0<br>0<br>-128917 | +0<br>0<br>-63 | +0<br>0<br>-5 |
| Obj-C      | +135202<br>0<br>-0 | +135139<br>63<br>-0 | +135139<br>63<br>-0 | +135198<br>4<br>-1 | +135202<br>0<br>-0 | —       | +703<br>134499<br>-0 | +2549<br>132653<br>-895 | +135139<br>63<br>-0 | +6285<br>128917<br>-0 | +135139<br>63<br>-0 | +135198<br>4<br>-1 |
| Perl       | +134499<br>0<br>-0 | +134436<br>63<br>-0 | +134436<br>63<br>-0 | +134495<br>4<br>-1 | +134499<br>0<br>-0 | +0<br>134499<br>-703 | —       | +2436<br>132063<br>-1485 | +134436<br>63<br>-0 | +5647<br>128852<br>-65 | +134436<br>63<br>-0 | +134495<br>4<br>-1 |
| PHP        | +133548<br>0<br>-0 | +133485<br>63<br>-0 | +133485<br>63<br>-0 | +133544<br>4<br>-1 | +133548<br>0<br>-0 | +895<br>132653<br>-2549 | +1485<br>132063<br>-2436 | —       | +133485<br>63<br>-0 | +7038<br>126510<br>-2407 | +133485<br>63<br>-0 | +133544<br>4<br>-1 |
| Python     | +63<br>0<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +59<br>4<br>-1 | +63<br>0<br>-0 | +0<br>63<br>-135139 | +0<br>63<br>-134436 | +0<br>63<br>-133485 | —       | +0<br>63<br>-128854 | +0<br>63<br>-0 | +59<br>4<br>-1 |
| Ruby       | +128917<br>0<br>-0 | +128854<br>63<br>-0 | +128854<br>63<br>-0 | +128913<br>4<br>-1 | +128917<br>0<br>-0 | +0<br>128917<br>-6285 | +65<br>128852<br>-5647 | +2407<br>126510<br>-7038 | +128854<br>63<br>-0 | —       | +128854<br>63<br>-0 | +128913<br>4<br>-1 |
| Rust       | +63<br>0<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +59<br>4<br>-1 | +63<br>0<br>-0 | +0<br>63<br>-135139 | +0<br>63<br>-134436 | +0<br>63<br>-133485 | +0<br>63<br>-0 | +0<br>63<br>-128854 | —       | +59<br>4<br>-1 |
| Scala      | +5<br>0<br>-0 | +1<br>4<br>-59 | +1<br>4<br>-59 | +0<br>5<br>-0 | +5<br>0<br>-0 | +1<br>4<br>-135198 | +1<br>4<br>-134495 | +1<br>4<br>-133544 | +1<br>4<br>-59 | +1<br>4<br>-128913 | +1<br>4<br>-59 | —       |

#### Character Classes - ASCII - Hexadecimal Digit (`[[:xdigit:]]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>22<br>-0 | +0<br>22<br>-0 | +21<br>1<br>-5 | +22<br>0<br>-0 | +0<br>22<br>-662 | +0<br>22<br>-22 | +0<br>22<br>-0 | +0<br>22<br>-0 | +0<br>22<br>-0 | +0<br>22<br>-0 | +21<br>1<br>-5 |
| Go         | +0<br>22<br>-0 | —    | +0<br>22<br>-0 | +21<br>1<br>-5 | +22<br>0<br>-0 | +0<br>22<br>-662 | +0<br>22<br>-22 | +0<br>22<br>-0 | +0<br>22<br>-0 | +0<br>22<br>-0 | +0<br>22<br>-0 | +21<br>1<br>-5 |
| Haskell    | +0<br>22<br>-0 | +0<br>22<br>-0 | —       | +21<br>1<br>-5 | +22<br>0<br>-0 | +0<br>22<br>-662 | +0<br>22<br>-22 | +0<br>22<br>-0 | +0<br>22<br>-0 | +0<br>22<br>-0 | +0<br>22<br>-0 | +21<br>1<br>-5 |
| Java       | +5<br>1<br>-21 | +5<br>1<br>-21 | +5<br>1<br>-21 | —    | +6<br>0<br>-0 | +5<br>1<br>-683 | +5<br>1<br>-43 | +5<br>1<br>-21 | +5<br>1<br>-21 | +5<br>1<br>-21 | +5<br>1<br>-21 | +0<br>6<br>-0 |
| Javascript | +0<br>0<br>-22 | +0<br>0<br>-22 | +0<br>0<br>-22 | +0<br>0<br>-6 | —          | +0<br>0<br>-684 | +0<br>0<br>-44 | +0<br>0<br>-22 | +0<br>0<br>-22 | +0<br>0<br>-22 | +0<br>0<br>-22 | +0<br>0<br>-6 |
| Obj-C      | +662<br>22<br>-0 | +662<br>22<br>-0 | +662<br>22<br>-0 | +683<br>1<br>-5 | +684<br>0<br>-0 | —     | +640<br>44<br>-0 | +662<br>22<br>-0 | +662<br>22<br>-0 | +662<br>22<br>-0 | +662<br>22<br>-0 | +683<br>1<br>-5 |
| Perl       | +22<br>22<br>-0 | +22<br>22<br>-0 | +22<br>22<br>-0 | +43<br>1<br>-5 | +44<br>0<br>-0 | +0<br>44<br>-640 | —    | +22<br>22<br>-0 | +22<br>22<br>-0 | +22<br>22<br>-0 | +22<br>22<br>-0 | +43<br>1<br>-5 |
| PHP        | +0<br>22<br>-0 | +0<br>22<br>-0 | +0<br>22<br>-0 | +21<br>1<br>-5 | +22<br>0<br>-0 | +0<br>22<br>-662 | +0<br>22<br>-22 | —    | +0<br>22<br>-0 | +0<br>22<br>-0 | +0<br>22<br>-0 | +21<br>1<br>-5 |
| Python     | +0<br>22<br>-0 | +0<br>22<br>-0 | +0<br>22<br>-0 | +21<br>1<br>-5 | +22<br>0<br>-0 | +0<br>22<br>-662 | +0<br>22<br>-22 | +0<br>22<br>-0 | —      | +0<br>22<br>-0 | +0<br>22<br>-0 | +21<br>1<br>-5 |
| Ruby       | +0<br>22<br>-0 | +0<br>22<br>-0 | +0<br>22<br>-0 | +21<br>1<br>-5 | +22<br>0<br>-0 | +0<br>22<br>-662 | +0<br>22<br>-22 | +0<br>22<br>-0 | +0<br>22<br>-0 | —    | +0<br>22<br>-0 | +21<br>1<br>-5 |
| Rust       | +0<br>22<br>-0 | +0<br>22<br>-0 | +0<br>22<br>-0 | +21<br>1<br>-5 | +22<br>0<br>-0 | +0<br>22<br>-662 | +0<br>22<br>-22 | +0<br>22<br>-0 | +0<br>22<br>-0 | +0<br>22<br>-0 | —    | +21<br>1<br>-5 |
| Scala      | +5<br>1<br>-21 | +5<br>1<br>-21 | +5<br>1<br>-21 | +0<br>6<br>-0 | +6<br>0<br>-0 | +5<br>1<br>-683 | +5<br>1<br>-43 | +5<br>1<br>-21 | +5<br>1<br>-21 | +5<br>1<br>-21 | +5<br>1<br>-21 | —     |

---

### Character Classes - Common

1. [Digit](#character-classes---common---digit-d) (`[\d]`)
2. [Whitespace](#character-classes---common---whitespace-s) (`[\s]`)
3. [Word Character](#character-classes---common---word-character-w) (`[\w]`)

#### Character Classes - Common - Digit (`[\d]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-650 | +0<br>10<br>-640 | +0<br>10<br>-650 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-670 | +0<br>10<br>-0 |
| Go         | +0<br>10<br>-0 | —    | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-650 | +0<br>10<br>-640 | +0<br>10<br>-650 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-670 | +0<br>10<br>-0 |
| Haskell    | +0<br>10<br>-0 | +0<br>10<br>-0 | —       | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-650 | +0<br>10<br>-640 | +0<br>10<br>-650 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-670 | +0<br>10<br>-0 |
| Java       | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —    | +0<br>10<br>-0 | +0<br>10<br>-650 | +0<br>10<br>-640 | +0<br>10<br>-650 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-670 | +0<br>10<br>-0 |
| Javascript | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —          | +0<br>10<br>-650 | +0<br>10<br>-640 | +0<br>10<br>-650 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-670 | +0<br>10<br>-0 |
| Obj-C      | +650<br>10<br>-0 | +650<br>10<br>-0 | +650<br>10<br>-0 | +650<br>10<br>-0 | +650<br>10<br>-0 | —     | +10<br>650<br>-0 | +0<br>660<br>-0 | +650<br>10<br>-0 | +650<br>10<br>-0 | +0<br>660<br>-20 | +650<br>10<br>-0 |
| Perl       | +640<br>10<br>-0 | +640<br>10<br>-0 | +640<br>10<br>-0 | +640<br>10<br>-0 | +640<br>10<br>-0 | +0<br>650<br>-10 | —    | +0<br>650<br>-10 | +640<br>10<br>-0 | +640<br>10<br>-0 | +0<br>650<br>-30 | +640<br>10<br>-0 |
| PHP        | +650<br>10<br>-0 | +650<br>10<br>-0 | +650<br>10<br>-0 | +650<br>10<br>-0 | +650<br>10<br>-0 | +0<br>660<br>-0 | +10<br>650<br>-0 | —    | +650<br>10<br>-0 | +650<br>10<br>-0 | +0<br>660<br>-20 | +650<br>10<br>-0 |
| Python     | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-650 | +0<br>10<br>-640 | +0<br>10<br>-650 | —      | +0<br>10<br>-0 | +0<br>10<br>-670 | +0<br>10<br>-0 |
| Ruby       | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-650 | +0<br>10<br>-640 | +0<br>10<br>-650 | +0<br>10<br>-0 | —    | +0<br>10<br>-670 | +0<br>10<br>-0 |
| Rust       | +670<br>10<br>-0 | +670<br>10<br>-0 | +670<br>10<br>-0 | +670<br>10<br>-0 | +670<br>10<br>-0 | +20<br>660<br>-0 | +30<br>650<br>-0 | +20<br>660<br>-0 | +670<br>10<br>-0 | +670<br>10<br>-0 | —    | +670<br>10<br>-0 |
| Scala      | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-650 | +0<br>10<br>-640 | +0<br>10<br>-650 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-670 | —     |

#### Character Classes - Common - Whitespace (`[\s]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +1<br>5<br>-0 | +0<br>6<br>-0 | +0<br>6<br>-0 | +0<br>6<br>-19 | +0<br>6<br>-19 | +0<br>6<br>-17 | +0<br>6<br>-20 | +1<br>5<br>-0 | +0<br>6<br>-0 | +0<br>6<br>-19 | +0<br>6<br>-0 |
| Go         | +0<br>5<br>-1 | —   | +0<br>5<br>-1 | +0<br>5<br>-1 | +0<br>5<br>-20 | +0<br>5<br>-20 | +0<br>5<br>-18 | +0<br>5<br>-21 | +0<br>5<br>-0 | +0<br>5<br>-1 | +0<br>5<br>-20 | +0<br>5<br>-1 |
| Haskell    | +0<br>6<br>-0 | +1<br>5<br>-0 | —       | +0<br>6<br>-0 | +0<br>6<br>-19 | +0<br>6<br>-19 | +0<br>6<br>-17 | +0<br>6<br>-20 | +1<br>5<br>-0 | +0<br>6<br>-0 | +0<br>6<br>-19 | +0<br>6<br>-0 |
| Java       | +0<br>6<br>-0 | +1<br>5<br>-0 | +0<br>6<br>-0 | —    | +0<br>6<br>-19 | +0<br>6<br>-19 | +0<br>6<br>-17 | +0<br>6<br>-20 | +1<br>5<br>-0 | +0<br>6<br>-0 | +0<br>6<br>-19 | +0<br>6<br>-0 |
| Javascript | +19<br>6<br>-0 | +20<br>5<br>-0 | +19<br>6<br>-0 | +19<br>6<br>-0 | —          | +1<br>24<br>-1 | +2<br>23<br>-0 | +1<br>24<br>-2 | +20<br>5<br>-0 | +19<br>6<br>-0 | +1<br>24<br>-1 | +19<br>6<br>-0 |
| Obj-C      | +19<br>6<br>-0 | +20<br>5<br>-0 | +19<br>6<br>-0 | +19<br>6<br>-0 | +1<br>24<br>-1 | —     | +2<br>23<br>-0 | +0<br>25<br>-1 | +20<br>5<br>-0 | +19<br>6<br>-0 | +0<br>25<br>-0 | +19<br>6<br>-0 |
| Perl       | +17<br>6<br>-0 | +18<br>5<br>-0 | +17<br>6<br>-0 | +17<br>6<br>-0 | +0<br>23<br>-2 | +0<br>23<br>-2 | —    | +0<br>23<br>-3 | +18<br>5<br>-0 | +17<br>6<br>-0 | +0<br>23<br>-2 | +17<br>6<br>-0 |
| PHP        | +20<br>6<br>-0 | +21<br>5<br>-0 | +20<br>6<br>-0 | +20<br>6<br>-0 | +2<br>24<br>-1 | +1<br>25<br>-0 | +3<br>23<br>-0 | —   | +21<br>5<br>-0 | +20<br>6<br>-0 | +1<br>25<br>-0 | +20<br>6<br>-0 |
| Python     | +0<br>5<br>-1 | +0<br>5<br>-0 | +0<br>5<br>-1 | +0<br>5<br>-1 | +0<br>5<br>-20 | +0<br>5<br>-20 | +0<br>5<br>-18 | +0<br>5<br>-21 | —      | +0<br>5<br>-1 | +0<br>5<br>-20 | +0<br>5<br>-1 |
| Ruby       | +0<br>6<br>-0 | +1<br>5<br>-0 | +0<br>6<br>-0 | +0<br>6<br>-0 | +0<br>6<br>-19 | +0<br>6<br>-19 | +0<br>6<br>-17 | +0<br>6<br>-20 | +1<br>5<br>-0 | —    | +0<br>6<br>-19 | +0<br>6<br>-0 |
| Rust       | +19<br>6<br>-0 | +20<br>5<br>-0 | +19<br>6<br>-0 | +19<br>6<br>-0 | +1<br>24<br>-1 | +0<br>25<br>-0 | +2<br>23<br>-0 | +0<br>25<br>-1 | +20<br>5<br>-0 | +19<br>6<br>-0 | —    | +19<br>6<br>-0 |
| Scala      | +0<br>6<br>-0 | +1<br>5<br>-0 | +0<br>6<br>-0 | +0<br>6<br>-0 | +0<br>6<br>-19 | +0<br>6<br>-19 | +0<br>6<br>-17 | +0<br>6<br>-20 | +1<br>5<br>-0 | +0<br>6<br>-0 | +0<br>6<br>-19 | —     |

#### Character Classes - Common - Word Character (`[\w]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-135139 | +0<br>63<br>-134436 | +0<br>63<br>-133485 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-139549 | +0<br>63<br>-0 |
| Go         | +0<br>63<br>-0 | —       | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-135139 | +0<br>63<br>-134436 | +0<br>63<br>-133485 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-139549 | +0<br>63<br>-0 |
| Haskell    | +0<br>63<br>-0 | +0<br>63<br>-0 | —       | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-135139 | +0<br>63<br>-134436 | +0<br>63<br>-133485 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-139549 | +0<br>63<br>-0 |
| Java       | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | —       | +0<br>63<br>-0 | +0<br>63<br>-135139 | +0<br>63<br>-134436 | +0<br>63<br>-133485 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-139549 | +0<br>63<br>-0 |
| Javascript | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | —          | +0<br>63<br>-135139 | +0<br>63<br>-134436 | +0<br>63<br>-133485 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-139549 | +0<br>63<br>-0 |
| Obj-C      | +135139<br>63<br>-0 | +135139<br>63<br>-0 | +135139<br>63<br>-0 | +135139<br>63<br>-0 | +135139<br>63<br>-0 | —       | +703<br>134499<br>-0 | +2549<br>132653<br>-895 | +135139<br>63<br>-0 | +135139<br>63<br>-0 | +0<br>135202<br>-4410 | +135139<br>63<br>-0 |
| Perl       | +134436<br>63<br>-0 | +134436<br>63<br>-0 | +134436<br>63<br>-0 | +134436<br>63<br>-0 | +134436<br>63<br>-0 | +0<br>134499<br>-703 | —       | +2436<br>132063<br>-1485 | +134436<br>63<br>-0 | +134436<br>63<br>-0 | +0<br>134499<br>-5113 | +134436<br>63<br>-0 |
| PHP        | +133485<br>63<br>-0 | +133485<br>63<br>-0 | +133485<br>63<br>-0 | +133485<br>63<br>-0 | +133485<br>63<br>-0 | +895<br>132653<br>-2549 | +1485<br>132063<br>-2436 | —       | +133485<br>63<br>-0 | +133485<br>63<br>-0 | +895<br>132653<br>-6959 | +133485<br>63<br>-0 |
| Python     | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-135139 | +0<br>63<br>-134436 | +0<br>63<br>-133485 | —       | +0<br>63<br>-0 | +0<br>63<br>-139549 | +0<br>63<br>-0 |
| Ruby       | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-135139 | +0<br>63<br>-134436 | +0<br>63<br>-133485 | +0<br>63<br>-0 | —       | +0<br>63<br>-139549 | +0<br>63<br>-0 |
| Rust       | +139549<br>63<br>-0 | +139549<br>63<br>-0 | +139549<br>63<br>-0 | +139549<br>63<br>-0 | +139549<br>63<br>-0 | +4410<br>135202<br>-0 | +5113<br>134499<br>-0 | +6959<br>132653<br>-895 | +139549<br>63<br>-0 | +139549<br>63<br>-0 | —       | +139549<br>63<br>-0 |
| Scala      | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-135139 | +0<br>63<br>-134436 | +0<br>63<br>-133485 | +0<br>63<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-139549 | —       |

---

### Character Classes - POSIX - Long

1. [Uppercase Letter](#character-classes---posix---long---uppercase-letter-puppercase_letter) (`[\p{Uppercase_Letter}]`)
2. [Lowercase Letter](#character-classes---posix---long---lowercase-letter-plowercase_letter) (`[\p{Lowercase_Letter}]`)
3. [Titlecase Letter](#character-classes---posix---long---titlecase-letter-ptitlecase_letter) (`[\p{Titlecase_Letter}]`)
4. [Cased Letter](#character-classes---posix---long---cased-letter-pcased_letter) (`[\p{Cased_Letter}]`)
5. [Modifier Letter](#character-classes---posix---long---modifier-letter-pmodifier_letter) (`[\p{Modifier_Letter}]`)
6. [Other Letter](#character-classes---posix---long---other-letter-pother_letter) (`[\p{Other_Letter}]`)
7. [Letter](#character-classes---posix---long---letter-pletter) (`[\p{Letter}]`)
8. [Nonspacing Mark](#character-classes---posix---long---nonspacing-mark-pnonspacing_mark) (`[\p{Nonspacing_Mark}]`)
9. [Spacing Mark](#character-classes---posix---long---spacing-mark-pspacing_mark) (`[\p{Spacing_Mark}]`)
10. [Enclosing Mark](#character-classes---posix---long---enclosing-mark-penclosing_mark) (`[\p{Enclosing_Mark}]`)
11. [Mark](#character-classes---posix---long---mark-pmark) (`[\p{Mark}]`)
12. [Decimal Number](#character-classes---posix---long---decimal-number-pdecimal_number) (`[\p{Decimal_Number}]`)
13. [Letter Number](#character-classes---posix---long---letter-number-pletter_number) (`[\p{Letter_Number}]`)
14. [Other Number](#character-classes---posix---long---other-number-pother_number) (`[\p{Other_Number}]`)
15. [Number](#character-classes---posix---long---number-pnumber) (`[\p{Number}]`)
16. [Connector Punctuation](#character-classes---posix---long---connector-punctuation-pconnector_punctuation) (`[\p{Connector_Punctuation}]`)
17. [Dash Punctuation](#character-classes---posix---long---dash-punctuation-pdash_punctuation) (`[\p{Dash_Punctuation}]`)
18. [Open Punctuation](#character-classes---posix---long---open-punctuation-popen_punctuation) (`[\p{Open_Punctuation}]`)
19. [Close Punctuation](#character-classes---posix---long---close-punctuation-pclose_punctuation) (`[\p{Close_Punctuation}]`)
20. [Initial Punctuation](#character-classes---posix---long---initial-punctuation-pinitial_punctuation) (`[\p{Initial_Punctuation}]`)
21. [Final Punctuation](#character-classes---posix---long---final-punctuation-pfinal_punctuation) (`[\p{Final_Punctuation}]`)
22. [Other Punctuation](#character-classes---posix---long---other-punctuation-pother_punctuation) (`[\p{Other_Punctuation}]`)
23. [Punctuation](#character-classes---posix---long---punctuation-ppunctuation) (`[\p{Punctuation}]`)
24. [Math Symbol](#character-classes---posix---long---math-symbol-pmath_symbol) (`[\p{Math_Symbol}]`)
25. [Currency Symbol](#character-classes---posix---long---currency-symbol-pcurrency_symbol) (`[\p{Currency_Symbol}]`)
26. [Modifier Symbol](#character-classes---posix---long---modifier-symbol-pmodifier_symbol) (`[\p{Modifier_Symbol}]`)
27. [Other Symbol](#character-classes---posix---long---other-symbol-pother_symbol) (`[\p{Other_Symbol}]`)
28. [Symbol](#character-classes---posix---long---symbol-psymbol) (`[\p{Symbol}]`)
29. [Space Separator](#character-classes---posix---long---space-separator-pspace_separator) (`[\p{Space_Separator}]`)
30. [Line Separator](#character-classes---posix---long---line-separator-pline_separator) (`[\p{Line_Separator}]`)
31. [Paragraph Separator](#character-classes---posix---long---paragraph-separator-pparagraph_separator) (`[\p{Paragraph_Separator}]`)
32. [Separator](#character-classes---posix---long---separator-pseparator) (`[\p{Separator}]`)
33. [Control](#character-classes---posix---long---control-pcontrol) (`[\p{Control}]`)
34. [Format](#character-classes---posix---long---format-pformat) (`[\p{Format}]`)
35. [Surrogate](#character-classes---posix---long---surrogate-psurrogate) (`[\p{Surrogate}]`)
36. [Private Use](#character-classes---posix---long---private-use-pprivate_use) (`[\p{Private_Use}]`)
37. [Unassigned](#character-classes---posix---long---unassigned-punassigned) (`[\p{Unassigned}]`)
38. [Other](#character-classes---posix---long---other-pother) (`[\p{Other}]`)

#### Character Classes - POSIX - Long - Uppercase Letter (`[\p{Uppercase_Letter}]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1831 | +0<br>0<br>-1831 | +0<br>0<br>-1791 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1788 | +0<br>0<br>-1831 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1831 | +0<br>0<br>-1831 | +0<br>0<br>-1791 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1788 | +0<br>0<br>-1831 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-1831 | +0<br>0<br>-1831 | +0<br>0<br>-1791 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1788 | +0<br>0<br>-1831 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —     | +0<br>0<br>-1831 | +0<br>0<br>-1831 | +0<br>0<br>-1791 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1788 | +0<br>0<br>-1831 | +0<br>0<br>-0 |
| Javascript | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +1831<br>0<br>-0 | —          | +0<br>1831<br>-0 | +40<br>1791<br>-0 | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +43<br>1788<br>-0 | +0<br>1831<br>-0 | +1831<br>0<br>-0 |
| Obj-C      | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +0<br>1831<br>-0 | —     | +40<br>1791<br>-0 | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +43<br>1788<br>-0 | +0<br>1831<br>-0 | +1831<br>0<br>-0 |
| Perl       | +1791<br>0<br>-0 | +1791<br>0<br>-0 | +1791<br>0<br>-0 | +1791<br>0<br>-0 | +0<br>1791<br>-40 | +0<br>1791<br>-40 | —     | +1791<br>0<br>-0 | +1791<br>0<br>-0 | +3<br>1788<br>-0 | +0<br>1791<br>-40 | +1791<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1831 | +0<br>0<br>-1831 | +0<br>0<br>-1791 | —     | +0<br>0<br>-0 | +0<br>0<br>-1788 | +0<br>0<br>-1831 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1831 | +0<br>0<br>-1831 | +0<br>0<br>-1791 | +0<br>0<br>-0 | —      | +0<br>0<br>-1788 | +0<br>0<br>-1831 | +0<br>0<br>-0 |
| Ruby       | +1788<br>0<br>-0 | +1788<br>0<br>-0 | +1788<br>0<br>-0 | +1788<br>0<br>-0 | +0<br>1788<br>-43 | +0<br>1788<br>-43 | +0<br>1788<br>-3 | +1788<br>0<br>-0 | +1788<br>0<br>-0 | —     | +0<br>1788<br>-43 | +1788<br>0<br>-0 |
| Rust       | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +0<br>1831<br>-0 | +0<br>1831<br>-0 | +40<br>1791<br>-0 | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +43<br>1788<br>-0 | —     | +1831<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1831 | +0<br>0<br>-1831 | +0<br>0<br>-1791 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1788 | +0<br>0<br>-1831 | —     |

#### Character Classes - POSIX - Long - Lowercase Letter (`[\p{Lowercase_Letter}]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2233 | +0<br>0<br>-2227 | +0<br>0<br>-2155 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2151 | +0<br>0<br>-2233 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2233 | +0<br>0<br>-2227 | +0<br>0<br>-2155 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2151 | +0<br>0<br>-2233 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-2233 | +0<br>0<br>-2227 | +0<br>0<br>-2155 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2151 | +0<br>0<br>-2233 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —     | +0<br>0<br>-2233 | +0<br>0<br>-2227 | +0<br>0<br>-2155 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2151 | +0<br>0<br>-2233 | +0<br>0<br>-0 |
| Javascript | +2233<br>0<br>-0 | +2233<br>0<br>-0 | +2233<br>0<br>-0 | +2233<br>0<br>-0 | —          | +6<br>2227<br>-0 | +78<br>2155<br>-0 | +2233<br>0<br>-0 | +2233<br>0<br>-0 | +82<br>2151<br>-0 | +0<br>2233<br>-0 | +2233<br>0<br>-0 |
| Obj-C      | +2227<br>0<br>-0 | +2227<br>0<br>-0 | +2227<br>0<br>-0 | +2227<br>0<br>-0 | +0<br>2227<br>-6 | —     | +72<br>2155<br>-0 | +2227<br>0<br>-0 | +2227<br>0<br>-0 | +76<br>2151<br>-0 | +0<br>2227<br>-6 | +2227<br>0<br>-0 |
| Perl       | +2155<br>0<br>-0 | +2155<br>0<br>-0 | +2155<br>0<br>-0 | +2155<br>0<br>-0 | +0<br>2155<br>-78 | +0<br>2155<br>-72 | —     | +2155<br>0<br>-0 | +2155<br>0<br>-0 | +4<br>2151<br>-0 | +0<br>2155<br>-78 | +2155<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2233 | +0<br>0<br>-2227 | +0<br>0<br>-2155 | —     | +0<br>0<br>-0 | +0<br>0<br>-2151 | +0<br>0<br>-2233 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2233 | +0<br>0<br>-2227 | +0<br>0<br>-2155 | +0<br>0<br>-0 | —      | +0<br>0<br>-2151 | +0<br>0<br>-2233 | +0<br>0<br>-0 |
| Ruby       | +2151<br>0<br>-0 | +2151<br>0<br>-0 | +2151<br>0<br>-0 | +2151<br>0<br>-0 | +0<br>2151<br>-82 | +0<br>2151<br>-76 | +0<br>2151<br>-4 | +2151<br>0<br>-0 | +2151<br>0<br>-0 | —     | +0<br>2151<br>-82 | +2151<br>0<br>-0 |
| Rust       | +2233<br>0<br>-0 | +2233<br>0<br>-0 | +2233<br>0<br>-0 | +2233<br>0<br>-0 | +0<br>2233<br>-0 | +6<br>2227<br>-0 | +78<br>2155<br>-0 | +2233<br>0<br>-0 | +2233<br>0<br>-0 | +82<br>2151<br>-0 | —     | +2233<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2233 | +0<br>0<br>-2227 | +0<br>0<br>-2155 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2151 | +0<br>0<br>-2233 | —     |

#### Character Classes - POSIX - Long - Titlecase Letter (`[\p{Titlecase_Letter}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-0 |
| Javascript | +31<br>0<br>-0 | +31<br>0<br>-0 | +31<br>0<br>-0 | +31<br>0<br>-0 | —          | +0<br>31<br>-0 | +0<br>31<br>-0 | +31<br>0<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +31<br>0<br>-0 |
| Obj-C      | +31<br>0<br>-0 | +31<br>0<br>-0 | +31<br>0<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | —     | +0<br>31<br>-0 | +31<br>0<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +31<br>0<br>-0 |
| Perl       | +31<br>0<br>-0 | +31<br>0<br>-0 | +31<br>0<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | —    | +31<br>0<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +31<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | —   | +0<br>0<br>-0 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-0 | —      | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-0 |
| Ruby       | +31<br>0<br>-0 | +31<br>0<br>-0 | +31<br>0<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +31<br>0<br>-0 | +31<br>0<br>-0 | —    | +0<br>31<br>-0 | +31<br>0<br>-0 |
| Rust       | +31<br>0<br>-0 | +31<br>0<br>-0 | +31<br>0<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +31<br>0<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | —    | +31<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-31 | +0<br>0<br>-31 | —     |

#### Character Classes - POSIX - Long - Cased Letter (`[\p{Cased_Letter}]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-4095 | +0<br>0<br>-4089 | +0<br>0<br>-3977 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3970 | +0<br>0<br>-4095 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-4095 | +0<br>0<br>-4089 | +0<br>0<br>-3977 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3970 | +0<br>0<br>-4095 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-4095 | +0<br>0<br>-4089 | +0<br>0<br>-3977 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3970 | +0<br>0<br>-4095 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —     | +0<br>0<br>-4095 | +0<br>0<br>-4089 | +0<br>0<br>-3977 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3970 | +0<br>0<br>-4095 | +0<br>0<br>-0 |
| Javascript | +4095<br>0<br>-0 | +4095<br>0<br>-0 | +4095<br>0<br>-0 | +4095<br>0<br>-0 | —          | +6<br>4089<br>-0 | +118<br>3977<br>-0 | +4095<br>0<br>-0 | +4095<br>0<br>-0 | +125<br>3970<br>-0 | +0<br>4095<br>-0 | +4095<br>0<br>-0 |
| Obj-C      | +4089<br>0<br>-0 | +4089<br>0<br>-0 | +4089<br>0<br>-0 | +4089<br>0<br>-0 | +0<br>4089<br>-6 | —     | +112<br>3977<br>-0 | +4089<br>0<br>-0 | +4089<br>0<br>-0 | +119<br>3970<br>-0 | +0<br>4089<br>-6 | +4089<br>0<br>-0 |
| Perl       | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +0<br>3977<br>-118 | +0<br>3977<br>-112 | —     | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +7<br>3970<br>-0 | +0<br>3977<br>-118 | +3977<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-4095 | +0<br>0<br>-4089 | +0<br>0<br>-3977 | —     | +0<br>0<br>-0 | +0<br>0<br>-3970 | +0<br>0<br>-4095 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-4095 | +0<br>0<br>-4089 | +0<br>0<br>-3977 | +0<br>0<br>-0 | —      | +0<br>0<br>-3970 | +0<br>0<br>-4095 | +0<br>0<br>-0 |
| Ruby       | +3970<br>0<br>-0 | +3970<br>0<br>-0 | +3970<br>0<br>-0 | +3970<br>0<br>-0 | +0<br>3970<br>-125 | +0<br>3970<br>-119 | +0<br>3970<br>-7 | +3970<br>0<br>-0 | +3970<br>0<br>-0 | —     | +0<br>3970<br>-125 | +3970<br>0<br>-0 |
| Rust       | +4095<br>0<br>-0 | +4095<br>0<br>-0 | +4095<br>0<br>-0 | +4095<br>0<br>-0 | +0<br>4095<br>-0 | +6<br>4089<br>-0 | +118<br>3977<br>-0 | +4095<br>0<br>-0 | +4095<br>0<br>-0 | +125<br>3970<br>-0 | —     | +4095<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-4095 | +0<br>0<br>-4089 | +0<br>0<br>-3977 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3970 | +0<br>0<br>-4095 | —     |

#### Character Classes - POSIX - Long - Modifier Letter (`[\p{Modifier_Letter}]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-397 | +0<br>0<br>-334 | +0<br>0<br>-260 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-259 | +0<br>0<br>-397 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-397 | +0<br>0<br>-334 | +0<br>0<br>-260 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-259 | +0<br>0<br>-397 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-397 | +0<br>0<br>-334 | +0<br>0<br>-260 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-259 | +0<br>0<br>-397 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-397 | +0<br>0<br>-334 | +0<br>0<br>-260 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-259 | +0<br>0<br>-397 | +0<br>0<br>-0 |
| Javascript | +397<br>0<br>-0 | +397<br>0<br>-0 | +397<br>0<br>-0 | +397<br>0<br>-0 | —          | +63<br>334<br>-0 | +137<br>260<br>-0 | +397<br>0<br>-0 | +397<br>0<br>-0 | +138<br>259<br>-0 | +0<br>397<br>-0 | +397<br>0<br>-0 |
| Obj-C      | +334<br>0<br>-0 | +334<br>0<br>-0 | +334<br>0<br>-0 | +334<br>0<br>-0 | +0<br>334<br>-63 | —     | +74<br>260<br>-0 | +334<br>0<br>-0 | +334<br>0<br>-0 | +75<br>259<br>-0 | +0<br>334<br>-63 | +334<br>0<br>-0 |
| Perl       | +260<br>0<br>-0 | +260<br>0<br>-0 | +260<br>0<br>-0 | +260<br>0<br>-0 | +0<br>260<br>-137 | +0<br>260<br>-74 | —    | +260<br>0<br>-0 | +260<br>0<br>-0 | +1<br>259<br>-0 | +0<br>260<br>-137 | +260<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-397 | +0<br>0<br>-334 | +0<br>0<br>-260 | —    | +0<br>0<br>-0 | +0<br>0<br>-259 | +0<br>0<br>-397 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-397 | +0<br>0<br>-334 | +0<br>0<br>-260 | +0<br>0<br>-0 | —      | +0<br>0<br>-259 | +0<br>0<br>-397 | +0<br>0<br>-0 |
| Ruby       | +259<br>0<br>-0 | +259<br>0<br>-0 | +259<br>0<br>-0 | +259<br>0<br>-0 | +0<br>259<br>-138 | +0<br>259<br>-75 | +0<br>259<br>-1 | +259<br>0<br>-0 | +259<br>0<br>-0 | —    | +0<br>259<br>-138 | +259<br>0<br>-0 |
| Rust       | +397<br>0<br>-0 | +397<br>0<br>-0 | +397<br>0<br>-0 | +397<br>0<br>-0 | +0<br>397<br>-0 | +63<br>334<br>-0 | +137<br>260<br>-0 | +397<br>0<br>-0 | +397<br>0<br>-0 | +138<br>259<br>-0 | —    | +397<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-397 | +0<br>0<br>-334 | +0<br>0<br>-260 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-259 | +0<br>0<br>-397 | —     |

#### Character Classes - POSIX - Long - Other Letter (`[\p{Other_Letter}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-131612 | +0<br>0<br>-127333 | +0<br>0<br>-127004 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-121414 | +0<br>0<br>-131612 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-131612 | +0<br>0<br>-127333 | +0<br>0<br>-127004 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-121414 | +0<br>0<br>-131612 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-131612 | +0<br>0<br>-127333 | +0<br>0<br>-127004 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-121414 | +0<br>0<br>-131612 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-131612 | +0<br>0<br>-127333 | +0<br>0<br>-127004 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-121414 | +0<br>0<br>-131612 | +0<br>0<br>-0 |
| Javascript | +131612<br>0<br>-0 | +131612<br>0<br>-0 | +131612<br>0<br>-0 | +131612<br>0<br>-0 | —          | +4279<br>127333<br>-0 | +4608<br>127004<br>-0 | +131612<br>0<br>-0 | +131612<br>0<br>-0 | +10198<br>121414<br>-0 | +0<br>131612<br>-0 | +131612<br>0<br>-0 |
| Obj-C      | +127333<br>0<br>-0 | +127333<br>0<br>-0 | +127333<br>0<br>-0 | +127333<br>0<br>-0 | +0<br>127333<br>-4279 | —       | +329<br>127004<br>-0 | +127333<br>0<br>-0 | +127333<br>0<br>-0 | +5919<br>121414<br>-0 | +0<br>127333<br>-4279 | +127333<br>0<br>-0 |
| Perl       | +127004<br>0<br>-0 | +127004<br>0<br>-0 | +127004<br>0<br>-0 | +127004<br>0<br>-0 | +0<br>127004<br>-4608 | +0<br>127004<br>-329 | —       | +127004<br>0<br>-0 | +127004<br>0<br>-0 | +5590<br>121414<br>-0 | +0<br>127004<br>-4608 | +127004<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-131612 | +0<br>0<br>-127333 | +0<br>0<br>-127004 | —       | +0<br>0<br>-0 | +0<br>0<br>-121414 | +0<br>0<br>-131612 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-131612 | +0<br>0<br>-127333 | +0<br>0<br>-127004 | +0<br>0<br>-0 | —       | +0<br>0<br>-121414 | +0<br>0<br>-131612 | +0<br>0<br>-0 |
| Ruby       | +121414<br>0<br>-0 | +121414<br>0<br>-0 | +121414<br>0<br>-0 | +121414<br>0<br>-0 | +0<br>121414<br>-10198 | +0<br>121414<br>-5919 | +0<br>121414<br>-5590 | +121414<br>0<br>-0 | +121414<br>0<br>-0 | —       | +0<br>121414<br>-10198 | +121414<br>0<br>-0 |
| Rust       | +131612<br>0<br>-0 | +131612<br>0<br>-0 | +131612<br>0<br>-0 | +131612<br>0<br>-0 | +0<br>131612<br>-0 | +4279<br>127333<br>-0 | +4608<br>127004<br>-0 | +131612<br>0<br>-0 | +131612<br>0<br>-0 | +10198<br>121414<br>-0 | —       | +131612<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-131612 | +0<br>0<br>-127333 | +0<br>0<br>-127004 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-121414 | +0<br>0<br>-131612 | —       |

#### Character Classes - POSIX - Long - Letter (`[\p{Letter}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-136104 | +0<br>0<br>-131756 | +0<br>0<br>-131241 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-125643 | +0<br>0<br>-136104 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-136104 | +0<br>0<br>-131756 | +0<br>0<br>-131241 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-125643 | +0<br>0<br>-136104 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-136104 | +0<br>0<br>-131756 | +0<br>0<br>-131241 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-125643 | +0<br>0<br>-136104 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-136104 | +0<br>0<br>-131756 | +0<br>0<br>-131241 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-125643 | +0<br>0<br>-136104 | +0<br>0<br>-0 |
| Javascript | +136104<br>0<br>-0 | +136104<br>0<br>-0 | +136104<br>0<br>-0 | +136104<br>0<br>-0 | —          | +4348<br>131756<br>-0 | +4863<br>131241<br>-0 | +136104<br>0<br>-0 | +136104<br>0<br>-0 | +10461<br>125643<br>-0 | +0<br>136104<br>-0 | +136104<br>0<br>-0 |
| Obj-C      | +131756<br>0<br>-0 | +131756<br>0<br>-0 | +131756<br>0<br>-0 | +131756<br>0<br>-0 | +0<br>131756<br>-4348 | —       | +515<br>131241<br>-0 | +131756<br>0<br>-0 | +131756<br>0<br>-0 | +6113<br>125643<br>-0 | +0<br>131756<br>-4348 | +131756<br>0<br>-0 |
| Perl       | +131241<br>0<br>-0 | +131241<br>0<br>-0 | +131241<br>0<br>-0 | +131241<br>0<br>-0 | +0<br>131241<br>-4863 | +0<br>131241<br>-515 | —       | +131241<br>0<br>-0 | +131241<br>0<br>-0 | +5598<br>125643<br>-0 | +0<br>131241<br>-4863 | +131241<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-136104 | +0<br>0<br>-131756 | +0<br>0<br>-131241 | —       | +0<br>0<br>-0 | +0<br>0<br>-125643 | +0<br>0<br>-136104 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-136104 | +0<br>0<br>-131756 | +0<br>0<br>-131241 | +0<br>0<br>-0 | —       | +0<br>0<br>-125643 | +0<br>0<br>-136104 | +0<br>0<br>-0 |
| Ruby       | +125643<br>0<br>-0 | +125643<br>0<br>-0 | +125643<br>0<br>-0 | +125643<br>0<br>-0 | +0<br>125643<br>-10461 | +0<br>125643<br>-6113 | +0<br>125643<br>-5598 | +125643<br>0<br>-0 | +125643<br>0<br>-0 | —       | +0<br>125643<br>-10461 | +125643<br>0<br>-0 |
| Rust       | +136104<br>0<br>-0 | +136104<br>0<br>-0 | +136104<br>0<br>-0 | +136104<br>0<br>-0 | +0<br>136104<br>-0 | +4348<br>131756<br>-0 | +4863<br>131241<br>-0 | +136104<br>0<br>-0 | +136104<br>0<br>-0 | +10461<br>125643<br>-0 | —       | +136104<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-136104 | +0<br>0<br>-131756 | +0<br>0<br>-131241 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-125643 | +0<br>0<br>-136104 | —       |

#### Character Classes - POSIX - Long - Nonspacing Mark (`[\p{Nonspacing_Mark}]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1985 | +0<br>0<br>-1950 | +0<br>0<br>-1839 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1826 | +0<br>0<br>-1985 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1985 | +0<br>0<br>-1950 | +0<br>0<br>-1839 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1826 | +0<br>0<br>-1985 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-1985 | +0<br>0<br>-1950 | +0<br>0<br>-1839 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1826 | +0<br>0<br>-1985 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —     | +0<br>0<br>-1985 | +0<br>0<br>-1950 | +0<br>0<br>-1839 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1826 | +0<br>0<br>-1985 | +0<br>0<br>-0 |
| Javascript | +1985<br>0<br>-0 | +1985<br>0<br>-0 | +1985<br>0<br>-0 | +1985<br>0<br>-0 | —          | +35<br>1950<br>-0 | +147<br>1838<br>-1 | +1985<br>0<br>-0 | +1985<br>0<br>-0 | +160<br>1825<br>-1 | +0<br>1985<br>-0 | +1985<br>0<br>-0 |
| Obj-C      | +1950<br>0<br>-0 | +1950<br>0<br>-0 | +1950<br>0<br>-0 | +1950<br>0<br>-0 | +0<br>1950<br>-35 | —     | +112<br>1838<br>-1 | +1950<br>0<br>-0 | +1950<br>0<br>-0 | +125<br>1825<br>-1 | +0<br>1950<br>-35 | +1950<br>0<br>-0 |
| Perl       | +1839<br>0<br>-0 | +1839<br>0<br>-0 | +1839<br>0<br>-0 | +1839<br>0<br>-0 | +1<br>1838<br>-147 | +1<br>1838<br>-112 | —     | +1839<br>0<br>-0 | +1839<br>0<br>-0 | +13<br>1826<br>-0 | +1<br>1838<br>-147 | +1839<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1985 | +0<br>0<br>-1950 | +0<br>0<br>-1839 | —     | +0<br>0<br>-0 | +0<br>0<br>-1826 | +0<br>0<br>-1985 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1985 | +0<br>0<br>-1950 | +0<br>0<br>-1839 | +0<br>0<br>-0 | —      | +0<br>0<br>-1826 | +0<br>0<br>-1985 | +0<br>0<br>-0 |
| Ruby       | +1826<br>0<br>-0 | +1826<br>0<br>-0 | +1826<br>0<br>-0 | +1826<br>0<br>-0 | +1<br>1825<br>-160 | +1<br>1825<br>-125 | +0<br>1826<br>-13 | +1826<br>0<br>-0 | +1826<br>0<br>-0 | —     | +1<br>1825<br>-160 | +1826<br>0<br>-0 |
| Rust       | +1985<br>0<br>-0 | +1985<br>0<br>-0 | +1985<br>0<br>-0 | +1985<br>0<br>-0 | +0<br>1985<br>-0 | +35<br>1950<br>-0 | +147<br>1838<br>-1 | +1985<br>0<br>-0 | +1985<br>0<br>-0 | +160<br>1825<br>-1 | —     | +1985<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1985 | +0<br>0<br>-1950 | +0<br>0<br>-1839 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1826 | +0<br>0<br>-1985 | —     |

#### Character Classes - POSIX - Long - Spacing Mark (`[\p{Spacing_Mark}]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-452 | +0<br>0<br>-445 | +0<br>0<br>-443 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-429 | +0<br>0<br>-452 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-452 | +0<br>0<br>-445 | +0<br>0<br>-443 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-429 | +0<br>0<br>-452 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-452 | +0<br>0<br>-445 | +0<br>0<br>-443 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-429 | +0<br>0<br>-452 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-452 | +0<br>0<br>-445 | +0<br>0<br>-443 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-429 | +0<br>0<br>-452 | +0<br>0<br>-0 |
| Javascript | +452<br>0<br>-0 | +452<br>0<br>-0 | +452<br>0<br>-0 | +452<br>0<br>-0 | —          | +7<br>445<br>-0 | +9<br>443<br>-0 | +452<br>0<br>-0 | +452<br>0<br>-0 | +23<br>429<br>-0 | +0<br>452<br>-0 | +452<br>0<br>-0 |
| Obj-C      | +445<br>0<br>-0 | +445<br>0<br>-0 | +445<br>0<br>-0 | +445<br>0<br>-0 | +0<br>445<br>-7 | —     | +2<br>443<br>-0 | +445<br>0<br>-0 | +445<br>0<br>-0 | +16<br>429<br>-0 | +0<br>445<br>-7 | +445<br>0<br>-0 |
| Perl       | +443<br>0<br>-0 | +443<br>0<br>-0 | +443<br>0<br>-0 | +443<br>0<br>-0 | +0<br>443<br>-9 | +0<br>443<br>-2 | —    | +443<br>0<br>-0 | +443<br>0<br>-0 | +14<br>429<br>-0 | +0<br>443<br>-9 | +443<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-452 | +0<br>0<br>-445 | +0<br>0<br>-443 | —    | +0<br>0<br>-0 | +0<br>0<br>-429 | +0<br>0<br>-452 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-452 | +0<br>0<br>-445 | +0<br>0<br>-443 | +0<br>0<br>-0 | —      | +0<br>0<br>-429 | +0<br>0<br>-452 | +0<br>0<br>-0 |
| Ruby       | +429<br>0<br>-0 | +429<br>0<br>-0 | +429<br>0<br>-0 | +429<br>0<br>-0 | +0<br>429<br>-23 | +0<br>429<br>-16 | +0<br>429<br>-14 | +429<br>0<br>-0 | +429<br>0<br>-0 | —    | +0<br>429<br>-23 | +429<br>0<br>-0 |
| Rust       | +452<br>0<br>-0 | +452<br>0<br>-0 | +452<br>0<br>-0 | +452<br>0<br>-0 | +0<br>452<br>-0 | +7<br>445<br>-0 | +9<br>443<br>-0 | +452<br>0<br>-0 | +452<br>0<br>-0 | +23<br>429<br>-0 | —    | +452<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-452 | +0<br>0<br>-445 | +0<br>0<br>-443 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-429 | +0<br>0<br>-452 | —     |

#### Character Classes - POSIX - Long - Enclosing Mark (`[\p{Enclosing_Mark}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-0 |
| Javascript | +13<br>0<br>-0 | +13<br>0<br>-0 | +13<br>0<br>-0 | +13<br>0<br>-0 | —          | +0<br>13<br>-0 | +0<br>13<br>-0 | +13<br>0<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +13<br>0<br>-0 |
| Obj-C      | +13<br>0<br>-0 | +13<br>0<br>-0 | +13<br>0<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | —     | +0<br>13<br>-0 | +13<br>0<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +13<br>0<br>-0 |
| Perl       | +13<br>0<br>-0 | +13<br>0<br>-0 | +13<br>0<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | —    | +13<br>0<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +13<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | —   | +0<br>0<br>-0 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-0 | —      | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-0 |
| Ruby       | +13<br>0<br>-0 | +13<br>0<br>-0 | +13<br>0<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +13<br>0<br>-0 | +13<br>0<br>-0 | —    | +0<br>13<br>-0 | +13<br>0<br>-0 |
| Rust       | +13<br>0<br>-0 | +13<br>0<br>-0 | +13<br>0<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +13<br>0<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | —    | +13<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-13 | +0<br>0<br>-13 | —     |

#### Character Classes - POSIX - Long - Mark (`[\p{Mark}]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2450 | +0<br>0<br>-2408 | +0<br>0<br>-2295 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2268 | +0<br>0<br>-2450 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2450 | +0<br>0<br>-2408 | +0<br>0<br>-2295 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2268 | +0<br>0<br>-2450 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-2450 | +0<br>0<br>-2408 | +0<br>0<br>-2295 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2268 | +0<br>0<br>-2450 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —     | +0<br>0<br>-2450 | +0<br>0<br>-2408 | +0<br>0<br>-2295 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2268 | +0<br>0<br>-2450 | +0<br>0<br>-0 |
| Javascript | +2450<br>0<br>-0 | +2450<br>0<br>-0 | +2450<br>0<br>-0 | +2450<br>0<br>-0 | —          | +42<br>2408<br>-0 | +155<br>2295<br>-0 | +2450<br>0<br>-0 | +2450<br>0<br>-0 | +182<br>2268<br>-0 | +0<br>2450<br>-0 | +2450<br>0<br>-0 |
| Obj-C      | +2408<br>0<br>-0 | +2408<br>0<br>-0 | +2408<br>0<br>-0 | +2408<br>0<br>-0 | +0<br>2408<br>-42 | —     | +113<br>2295<br>-0 | +2408<br>0<br>-0 | +2408<br>0<br>-0 | +140<br>2268<br>-0 | +0<br>2408<br>-42 | +2408<br>0<br>-0 |
| Perl       | +2295<br>0<br>-0 | +2295<br>0<br>-0 | +2295<br>0<br>-0 | +2295<br>0<br>-0 | +0<br>2295<br>-155 | +0<br>2295<br>-113 | —     | +2295<br>0<br>-0 | +2295<br>0<br>-0 | +27<br>2268<br>-0 | +0<br>2295<br>-155 | +2295<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2450 | +0<br>0<br>-2408 | +0<br>0<br>-2295 | —     | +0<br>0<br>-0 | +0<br>0<br>-2268 | +0<br>0<br>-2450 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2450 | +0<br>0<br>-2408 | +0<br>0<br>-2295 | +0<br>0<br>-0 | —      | +0<br>0<br>-2268 | +0<br>0<br>-2450 | +0<br>0<br>-0 |
| Ruby       | +2268<br>0<br>-0 | +2268<br>0<br>-0 | +2268<br>0<br>-0 | +2268<br>0<br>-0 | +0<br>2268<br>-182 | +0<br>2268<br>-140 | +0<br>2268<br>-27 | +2268<br>0<br>-0 | +2268<br>0<br>-0 | —     | +0<br>2268<br>-182 | +2268<br>0<br>-0 |
| Rust       | +2450<br>0<br>-0 | +2450<br>0<br>-0 | +2450<br>0<br>-0 | +2450<br>0<br>-0 | +0<br>2450<br>-0 | +42<br>2408<br>-0 | +155<br>2295<br>-0 | +2450<br>0<br>-0 | +2450<br>0<br>-0 | +182<br>2268<br>-0 | —     | +2450<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2450 | +0<br>0<br>-2408 | +0<br>0<br>-2295 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2268 | +0<br>0<br>-2450 | —     |

#### Character Classes - POSIX - Long - Decimal Number (`[\p{Decimal_Number}]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-680 | +0<br>0<br>-660 | +0<br>0<br>-650 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-630 | +0<br>0<br>-680 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-680 | +0<br>0<br>-660 | +0<br>0<br>-650 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-630 | +0<br>0<br>-680 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-680 | +0<br>0<br>-660 | +0<br>0<br>-650 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-630 | +0<br>0<br>-680 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-680 | +0<br>0<br>-660 | +0<br>0<br>-650 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-630 | +0<br>0<br>-680 | +0<br>0<br>-0 |
| Javascript | +680<br>0<br>-0 | +680<br>0<br>-0 | +680<br>0<br>-0 | +680<br>0<br>-0 | —          | +20<br>660<br>-0 | +30<br>650<br>-0 | +680<br>0<br>-0 | +680<br>0<br>-0 | +50<br>630<br>-0 | +0<br>680<br>-0 | +680<br>0<br>-0 |
| Obj-C      | +660<br>0<br>-0 | +660<br>0<br>-0 | +660<br>0<br>-0 | +660<br>0<br>-0 | +0<br>660<br>-20 | —     | +10<br>650<br>-0 | +660<br>0<br>-0 | +660<br>0<br>-0 | +30<br>630<br>-0 | +0<br>660<br>-20 | +660<br>0<br>-0 |
| Perl       | +650<br>0<br>-0 | +650<br>0<br>-0 | +650<br>0<br>-0 | +650<br>0<br>-0 | +0<br>650<br>-30 | +0<br>650<br>-10 | —    | +650<br>0<br>-0 | +650<br>0<br>-0 | +20<br>630<br>-0 | +0<br>650<br>-30 | +650<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-680 | +0<br>0<br>-660 | +0<br>0<br>-650 | —    | +0<br>0<br>-0 | +0<br>0<br>-630 | +0<br>0<br>-680 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-680 | +0<br>0<br>-660 | +0<br>0<br>-650 | +0<br>0<br>-0 | —      | +0<br>0<br>-630 | +0<br>0<br>-680 | +0<br>0<br>-0 |
| Ruby       | +630<br>0<br>-0 | +630<br>0<br>-0 | +630<br>0<br>-0 | +630<br>0<br>-0 | +0<br>630<br>-50 | +0<br>630<br>-30 | +0<br>630<br>-20 | +630<br>0<br>-0 | +630<br>0<br>-0 | —    | +0<br>630<br>-50 | +630<br>0<br>-0 |
| Rust       | +680<br>0<br>-0 | +680<br>0<br>-0 | +680<br>0<br>-0 | +680<br>0<br>-0 | +0<br>680<br>-0 | +20<br>660<br>-0 | +30<br>650<br>-0 | +680<br>0<br>-0 | +680<br>0<br>-0 | +50<br>630<br>-0 | —    | +680<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-680 | +0<br>0<br>-660 | +0<br>0<br>-650 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-630 | +0<br>0<br>-680 | —     |

#### Character Classes - POSIX - Long - Letter Number (`[\p{Letter_Number}]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-0 |
| Javascript | +236<br>0<br>-0 | +236<br>0<br>-0 | +236<br>0<br>-0 | +236<br>0<br>-0 | —          | +0<br>236<br>-0 | +0<br>236<br>-0 | +236<br>0<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +236<br>0<br>-0 |
| Obj-C      | +236<br>0<br>-0 | +236<br>0<br>-0 | +236<br>0<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | —     | +0<br>236<br>-0 | +236<br>0<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +236<br>0<br>-0 |
| Perl       | +236<br>0<br>-0 | +236<br>0<br>-0 | +236<br>0<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | —    | +236<br>0<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +236<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | —    | +0<br>0<br>-0 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-0 | —      | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-0 |
| Ruby       | +236<br>0<br>-0 | +236<br>0<br>-0 | +236<br>0<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +236<br>0<br>-0 | +236<br>0<br>-0 | —    | +0<br>236<br>-0 | +236<br>0<br>-0 |
| Rust       | +236<br>0<br>-0 | +236<br>0<br>-0 | +236<br>0<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +236<br>0<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | —    | +236<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-236 | +0<br>0<br>-236 | —     |

#### Character Classes - POSIX - Long - Other Number (`[\p{Other_Number}]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-915 | +0<br>0<br>-895 | +0<br>0<br>-895 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-888 | +0<br>0<br>-915 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-915 | +0<br>0<br>-895 | +0<br>0<br>-895 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-888 | +0<br>0<br>-915 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-915 | +0<br>0<br>-895 | +0<br>0<br>-895 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-888 | +0<br>0<br>-915 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-915 | +0<br>0<br>-895 | +0<br>0<br>-895 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-888 | +0<br>0<br>-915 | +0<br>0<br>-0 |
| Javascript | +915<br>0<br>-0 | +915<br>0<br>-0 | +915<br>0<br>-0 | +915<br>0<br>-0 | —          | +20<br>895<br>-0 | +20<br>895<br>-0 | +915<br>0<br>-0 | +915<br>0<br>-0 | +27<br>888<br>-0 | +0<br>915<br>-0 | +915<br>0<br>-0 |
| Obj-C      | +895<br>0<br>-0 | +895<br>0<br>-0 | +895<br>0<br>-0 | +895<br>0<br>-0 | +0<br>895<br>-20 | —     | +0<br>895<br>-0 | +895<br>0<br>-0 | +895<br>0<br>-0 | +7<br>888<br>-0 | +0<br>895<br>-20 | +895<br>0<br>-0 |
| Perl       | +895<br>0<br>-0 | +895<br>0<br>-0 | +895<br>0<br>-0 | +895<br>0<br>-0 | +0<br>895<br>-20 | +0<br>895<br>-0 | —    | +895<br>0<br>-0 | +895<br>0<br>-0 | +7<br>888<br>-0 | +0<br>895<br>-20 | +895<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-915 | +0<br>0<br>-895 | +0<br>0<br>-895 | —    | +0<br>0<br>-0 | +0<br>0<br>-888 | +0<br>0<br>-915 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-915 | +0<br>0<br>-895 | +0<br>0<br>-895 | +0<br>0<br>-0 | —      | +0<br>0<br>-888 | +0<br>0<br>-915 | +0<br>0<br>-0 |
| Ruby       | +888<br>0<br>-0 | +888<br>0<br>-0 | +888<br>0<br>-0 | +888<br>0<br>-0 | +0<br>888<br>-27 | +0<br>888<br>-7 | +0<br>888<br>-7 | +888<br>0<br>-0 | +888<br>0<br>-0 | —    | +0<br>888<br>-27 | +888<br>0<br>-0 |
| Rust       | +915<br>0<br>-0 | +915<br>0<br>-0 | +915<br>0<br>-0 | +915<br>0<br>-0 | +0<br>915<br>-0 | +20<br>895<br>-0 | +20<br>895<br>-0 | +915<br>0<br>-0 | +915<br>0<br>-0 | +27<br>888<br>-0 | —    | +915<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-915 | +0<br>0<br>-895 | +0<br>0<br>-895 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-888 | +0<br>0<br>-915 | —     |

#### Character Classes - POSIX - Long - Number (`[\p{Number}]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1831 | +0<br>0<br>-1791 | +0<br>0<br>-1781 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1754 | +0<br>0<br>-1831 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1831 | +0<br>0<br>-1791 | +0<br>0<br>-1781 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1754 | +0<br>0<br>-1831 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-1831 | +0<br>0<br>-1791 | +0<br>0<br>-1781 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1754 | +0<br>0<br>-1831 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —     | +0<br>0<br>-1831 | +0<br>0<br>-1791 | +0<br>0<br>-1781 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1754 | +0<br>0<br>-1831 | +0<br>0<br>-0 |
| Javascript | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +1831<br>0<br>-0 | —          | +40<br>1791<br>-0 | +50<br>1781<br>-0 | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +77<br>1754<br>-0 | +0<br>1831<br>-0 | +1831<br>0<br>-0 |
| Obj-C      | +1791<br>0<br>-0 | +1791<br>0<br>-0 | +1791<br>0<br>-0 | +1791<br>0<br>-0 | +0<br>1791<br>-40 | —     | +10<br>1781<br>-0 | +1791<br>0<br>-0 | +1791<br>0<br>-0 | +37<br>1754<br>-0 | +0<br>1791<br>-40 | +1791<br>0<br>-0 |
| Perl       | +1781<br>0<br>-0 | +1781<br>0<br>-0 | +1781<br>0<br>-0 | +1781<br>0<br>-0 | +0<br>1781<br>-50 | +0<br>1781<br>-10 | —     | +1781<br>0<br>-0 | +1781<br>0<br>-0 | +27<br>1754<br>-0 | +0<br>1781<br>-50 | +1781<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1831 | +0<br>0<br>-1791 | +0<br>0<br>-1781 | —     | +0<br>0<br>-0 | +0<br>0<br>-1754 | +0<br>0<br>-1831 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1831 | +0<br>0<br>-1791 | +0<br>0<br>-1781 | +0<br>0<br>-0 | —      | +0<br>0<br>-1754 | +0<br>0<br>-1831 | +0<br>0<br>-0 |
| Ruby       | +1754<br>0<br>-0 | +1754<br>0<br>-0 | +1754<br>0<br>-0 | +1754<br>0<br>-0 | +0<br>1754<br>-77 | +0<br>1754<br>-37 | +0<br>1754<br>-27 | +1754<br>0<br>-0 | +1754<br>0<br>-0 | —     | +0<br>1754<br>-77 | +1754<br>0<br>-0 |
| Rust       | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +0<br>1831<br>-0 | +40<br>1791<br>-0 | +50<br>1781<br>-0 | +1831<br>0<br>-0 | +1831<br>0<br>-0 | +77<br>1754<br>-0 | —     | +1831<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1831 | +0<br>0<br>-1791 | +0<br>0<br>-1781 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1754 | +0<br>0<br>-1831 | —     |

#### Character Classes - POSIX - Long - Connector Punctuation (`[\p{Connector_Punctuation}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 |
| Javascript | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | —          | +0<br>10<br>-0 | +0<br>10<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +10<br>0<br>-0 |
| Obj-C      | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | —     | +0<br>10<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +10<br>0<br>-0 |
| Perl       | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —    | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +10<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | —   | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 | —      | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 |
| Ruby       | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | —    | +0<br>10<br>-0 | +10<br>0<br>-0 |
| Rust       | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | —    | +10<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | —     |

#### Character Classes - POSIX - Long - Dash Punctuation (`[\p{Dash_Punctuation}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-26 | +0<br>0<br>-26 | +0<br>0<br>-25 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-24 | +0<br>0<br>-26 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-26 | +0<br>0<br>-26 | +0<br>0<br>-25 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-24 | +0<br>0<br>-26 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-26 | +0<br>0<br>-26 | +0<br>0<br>-25 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-24 | +0<br>0<br>-26 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-26 | +0<br>0<br>-26 | +0<br>0<br>-25 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-24 | +0<br>0<br>-26 | +0<br>0<br>-0 |
| Javascript | +26<br>0<br>-0 | +26<br>0<br>-0 | +26<br>0<br>-0 | +26<br>0<br>-0 | —          | +0<br>26<br>-0 | +1<br>25<br>-0 | +26<br>0<br>-0 | +26<br>0<br>-0 | +2<br>24<br>-0 | +0<br>26<br>-0 | +26<br>0<br>-0 |
| Obj-C      | +26<br>0<br>-0 | +26<br>0<br>-0 | +26<br>0<br>-0 | +26<br>0<br>-0 | +0<br>26<br>-0 | —     | +1<br>25<br>-0 | +26<br>0<br>-0 | +26<br>0<br>-0 | +2<br>24<br>-0 | +0<br>26<br>-0 | +26<br>0<br>-0 |
| Perl       | +25<br>0<br>-0 | +25<br>0<br>-0 | +25<br>0<br>-0 | +25<br>0<br>-0 | +0<br>25<br>-1 | +0<br>25<br>-1 | —    | +25<br>0<br>-0 | +25<br>0<br>-0 | +1<br>24<br>-0 | +0<br>25<br>-1 | +25<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-26 | +0<br>0<br>-26 | +0<br>0<br>-25 | —   | +0<br>0<br>-0 | +0<br>0<br>-24 | +0<br>0<br>-26 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-26 | +0<br>0<br>-26 | +0<br>0<br>-25 | +0<br>0<br>-0 | —      | +0<br>0<br>-24 | +0<br>0<br>-26 | +0<br>0<br>-0 |
| Ruby       | +24<br>0<br>-0 | +24<br>0<br>-0 | +24<br>0<br>-0 | +24<br>0<br>-0 | +0<br>24<br>-2 | +0<br>24<br>-2 | +0<br>24<br>-1 | +24<br>0<br>-0 | +24<br>0<br>-0 | —    | +0<br>24<br>-2 | +24<br>0<br>-0 |
| Rust       | +26<br>0<br>-0 | +26<br>0<br>-0 | +26<br>0<br>-0 | +26<br>0<br>-0 | +0<br>26<br>-0 | +0<br>26<br>-0 | +1<br>25<br>-0 | +26<br>0<br>-0 | +26<br>0<br>-0 | +2<br>24<br>-0 | —    | +26<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-26 | +0<br>0<br>-26 | +0<br>0<br>-25 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-24 | +0<br>0<br>-26 | —     |

#### Character Classes - POSIX - Long - Open Punctuation (`[\p{Open_Punctuation}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-79 | +0<br>0<br>-79 | +0<br>0<br>-75 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-75 | +0<br>0<br>-79 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-79 | +0<br>0<br>-79 | +0<br>0<br>-75 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-75 | +0<br>0<br>-79 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-79 | +0<br>0<br>-79 | +0<br>0<br>-75 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-75 | +0<br>0<br>-79 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-79 | +0<br>0<br>-79 | +0<br>0<br>-75 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-75 | +0<br>0<br>-79 | +0<br>0<br>-0 |
| Javascript | +79<br>0<br>-0 | +79<br>0<br>-0 | +79<br>0<br>-0 | +79<br>0<br>-0 | —          | +0<br>79<br>-0 | +4<br>75<br>-0 | +79<br>0<br>-0 | +79<br>0<br>-0 | +4<br>75<br>-0 | +0<br>79<br>-0 | +79<br>0<br>-0 |
| Obj-C      | +79<br>0<br>-0 | +79<br>0<br>-0 | +79<br>0<br>-0 | +79<br>0<br>-0 | +0<br>79<br>-0 | —     | +4<br>75<br>-0 | +79<br>0<br>-0 | +79<br>0<br>-0 | +4<br>75<br>-0 | +0<br>79<br>-0 | +79<br>0<br>-0 |
| Perl       | +75<br>0<br>-0 | +75<br>0<br>-0 | +75<br>0<br>-0 | +75<br>0<br>-0 | +0<br>75<br>-4 | +0<br>75<br>-4 | —    | +75<br>0<br>-0 | +75<br>0<br>-0 | +0<br>75<br>-0 | +0<br>75<br>-4 | +75<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-79 | +0<br>0<br>-79 | +0<br>0<br>-75 | —   | +0<br>0<br>-0 | +0<br>0<br>-75 | +0<br>0<br>-79 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-79 | +0<br>0<br>-79 | +0<br>0<br>-75 | +0<br>0<br>-0 | —      | +0<br>0<br>-75 | +0<br>0<br>-79 | +0<br>0<br>-0 |
| Ruby       | +75<br>0<br>-0 | +75<br>0<br>-0 | +75<br>0<br>-0 | +75<br>0<br>-0 | +0<br>75<br>-4 | +0<br>75<br>-4 | +0<br>75<br>-0 | +75<br>0<br>-0 | +75<br>0<br>-0 | —    | +0<br>75<br>-4 | +75<br>0<br>-0 |
| Rust       | +79<br>0<br>-0 | +79<br>0<br>-0 | +79<br>0<br>-0 | +79<br>0<br>-0 | +0<br>79<br>-0 | +0<br>79<br>-0 | +4<br>75<br>-0 | +79<br>0<br>-0 | +79<br>0<br>-0 | +4<br>75<br>-0 | —    | +79<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-79 | +0<br>0<br>-79 | +0<br>0<br>-75 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-75 | +0<br>0<br>-79 | —     |

#### Character Classes - POSIX - Long - Close Punctuation (`[\p{Close_Punctuation}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-77 | +0<br>0<br>-77 | +0<br>0<br>-73 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-73 | +0<br>0<br>-77 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-77 | +0<br>0<br>-77 | +0<br>0<br>-73 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-73 | +0<br>0<br>-77 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-77 | +0<br>0<br>-77 | +0<br>0<br>-73 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-73 | +0<br>0<br>-77 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-77 | +0<br>0<br>-77 | +0<br>0<br>-73 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-73 | +0<br>0<br>-77 | +0<br>0<br>-0 |
| Javascript | +77<br>0<br>-0 | +77<br>0<br>-0 | +77<br>0<br>-0 | +77<br>0<br>-0 | —          | +0<br>77<br>-0 | +4<br>73<br>-0 | +77<br>0<br>-0 | +77<br>0<br>-0 | +4<br>73<br>-0 | +0<br>77<br>-0 | +77<br>0<br>-0 |
| Obj-C      | +77<br>0<br>-0 | +77<br>0<br>-0 | +77<br>0<br>-0 | +77<br>0<br>-0 | +0<br>77<br>-0 | —     | +4<br>73<br>-0 | +77<br>0<br>-0 | +77<br>0<br>-0 | +4<br>73<br>-0 | +0<br>77<br>-0 | +77<br>0<br>-0 |
| Perl       | +73<br>0<br>-0 | +73<br>0<br>-0 | +73<br>0<br>-0 | +73<br>0<br>-0 | +0<br>73<br>-4 | +0<br>73<br>-4 | —    | +73<br>0<br>-0 | +73<br>0<br>-0 | +0<br>73<br>-0 | +0<br>73<br>-4 | +73<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-77 | +0<br>0<br>-77 | +0<br>0<br>-73 | —   | +0<br>0<br>-0 | +0<br>0<br>-73 | +0<br>0<br>-77 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-77 | +0<br>0<br>-77 | +0<br>0<br>-73 | +0<br>0<br>-0 | —      | +0<br>0<br>-73 | +0<br>0<br>-77 | +0<br>0<br>-0 |
| Ruby       | +73<br>0<br>-0 | +73<br>0<br>-0 | +73<br>0<br>-0 | +73<br>0<br>-0 | +0<br>73<br>-4 | +0<br>73<br>-4 | +0<br>73<br>-0 | +73<br>0<br>-0 | +73<br>0<br>-0 | —    | +0<br>73<br>-4 | +73<br>0<br>-0 |
| Rust       | +77<br>0<br>-0 | +77<br>0<br>-0 | +77<br>0<br>-0 | +77<br>0<br>-0 | +0<br>77<br>-0 | +0<br>77<br>-0 | +4<br>73<br>-0 | +77<br>0<br>-0 | +77<br>0<br>-0 | +4<br>73<br>-0 | —    | +77<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-77 | +0<br>0<br>-77 | +0<br>0<br>-73 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-73 | +0<br>0<br>-77 | —     |

#### Character Classes - POSIX - Long - Initial Punctuation (`[\p{Initial_Punctuation}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-0 |
| Javascript | +12<br>0<br>-0 | +12<br>0<br>-0 | +12<br>0<br>-0 | +12<br>0<br>-0 | —          | +0<br>12<br>-0 | +0<br>12<br>-0 | +12<br>0<br>-0 | +12<br>0<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +12<br>0<br>-0 |
| Obj-C      | +12<br>0<br>-0 | +12<br>0<br>-0 | +12<br>0<br>-0 | +12<br>0<br>-0 | +0<br>12<br>-0 | —     | +0<br>12<br>-0 | +12<br>0<br>-0 | +12<br>0<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +12<br>0<br>-0 |
| Perl       | +12<br>0<br>-0 | +12<br>0<br>-0 | +12<br>0<br>-0 | +12<br>0<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | —    | +12<br>0<br>-0 | +12<br>0<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +12<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-12 | —   | +0<br>0<br>-0 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-0 | —      | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-0 |
| Ruby       | +12<br>0<br>-0 | +12<br>0<br>-0 | +12<br>0<br>-0 | +12<br>0<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +12<br>0<br>-0 | +12<br>0<br>-0 | —    | +0<br>12<br>-0 | +12<br>0<br>-0 |
| Rust       | +12<br>0<br>-0 | +12<br>0<br>-0 | +12<br>0<br>-0 | +12<br>0<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +12<br>0<br>-0 | +12<br>0<br>-0 | +0<br>12<br>-0 | —    | +12<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-12 | +0<br>0<br>-12 | —     |

#### Character Classes - POSIX - Long - Final Punctuation (`[\p{Final_Punctuation}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 |
| Javascript | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | —          | +0<br>10<br>-0 | +0<br>10<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +10<br>0<br>-0 |
| Obj-C      | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | —     | +0<br>10<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +10<br>0<br>-0 |
| Perl       | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —    | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +10<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | —   | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 | —      | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 |
| Ruby       | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | —    | +0<br>10<br>-0 | +10<br>0<br>-0 |
| Rust       | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +10<br>0<br>-0 | +10<br>0<br>-0 | +0<br>10<br>-0 | —    | +10<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-10 | +0<br>0<br>-10 | —     |

#### Character Classes - POSIX - Long - Other Punctuation (`[\p{Other_Punctuation}]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-628 | +0<br>0<br>-605 | +0<br>0<br>-593 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-588 | +0<br>0<br>-628 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-628 | +0<br>0<br>-605 | +0<br>0<br>-593 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-588 | +0<br>0<br>-628 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-628 | +0<br>0<br>-605 | +0<br>0<br>-593 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-588 | +0<br>0<br>-628 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-628 | +0<br>0<br>-605 | +0<br>0<br>-593 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-588 | +0<br>0<br>-628 | +0<br>0<br>-0 |
| Javascript | +628<br>0<br>-0 | +628<br>0<br>-0 | +628<br>0<br>-0 | +628<br>0<br>-0 | —          | +23<br>605<br>-0 | +35<br>593<br>-0 | +628<br>0<br>-0 | +628<br>0<br>-0 | +40<br>588<br>-0 | +0<br>628<br>-0 | +628<br>0<br>-0 |
| Obj-C      | +605<br>0<br>-0 | +605<br>0<br>-0 | +605<br>0<br>-0 | +605<br>0<br>-0 | +0<br>605<br>-23 | —     | +12<br>593<br>-0 | +605<br>0<br>-0 | +605<br>0<br>-0 | +17<br>588<br>-0 | +0<br>605<br>-23 | +605<br>0<br>-0 |
| Perl       | +593<br>0<br>-0 | +593<br>0<br>-0 | +593<br>0<br>-0 | +593<br>0<br>-0 | +0<br>593<br>-35 | +0<br>593<br>-12 | —    | +593<br>0<br>-0 | +593<br>0<br>-0 | +5<br>588<br>-0 | +0<br>593<br>-35 | +593<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-628 | +0<br>0<br>-605 | +0<br>0<br>-593 | —    | +0<br>0<br>-0 | +0<br>0<br>-588 | +0<br>0<br>-628 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-628 | +0<br>0<br>-605 | +0<br>0<br>-593 | +0<br>0<br>-0 | —      | +0<br>0<br>-588 | +0<br>0<br>-628 | +0<br>0<br>-0 |
| Ruby       | +588<br>0<br>-0 | +588<br>0<br>-0 | +588<br>0<br>-0 | +588<br>0<br>-0 | +0<br>588<br>-40 | +0<br>588<br>-17 | +0<br>588<br>-5 | +588<br>0<br>-0 | +588<br>0<br>-0 | —    | +0<br>588<br>-40 | +588<br>0<br>-0 |
| Rust       | +628<br>0<br>-0 | +628<br>0<br>-0 | +628<br>0<br>-0 | +628<br>0<br>-0 | +0<br>628<br>-0 | +23<br>605<br>-0 | +35<br>593<br>-0 | +628<br>0<br>-0 | +628<br>0<br>-0 | +40<br>588<br>-0 | —    | +628<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-628 | +0<br>0<br>-605 | +0<br>0<br>-593 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-588 | +0<br>0<br>-628 | —     |

#### Character Classes - POSIX - Long - Punctuation (`[\p{Punctuation}]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-842 | +0<br>0<br>-819 | +0<br>0<br>-798 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-792 | +0<br>0<br>-842 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-842 | +0<br>0<br>-819 | +0<br>0<br>-798 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-792 | +0<br>0<br>-842 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-842 | +0<br>0<br>-819 | +0<br>0<br>-798 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-792 | +0<br>0<br>-842 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-842 | +0<br>0<br>-819 | +0<br>0<br>-798 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-792 | +0<br>0<br>-842 | +0<br>0<br>-0 |
| Javascript | +842<br>0<br>-0 | +842<br>0<br>-0 | +842<br>0<br>-0 | +842<br>0<br>-0 | —          | +23<br>819<br>-0 | +44<br>798<br>-0 | +842<br>0<br>-0 | +842<br>0<br>-0 | +50<br>792<br>-0 | +0<br>842<br>-0 | +842<br>0<br>-0 |
| Obj-C      | +819<br>0<br>-0 | +819<br>0<br>-0 | +819<br>0<br>-0 | +819<br>0<br>-0 | +0<br>819<br>-23 | —     | +21<br>798<br>-0 | +819<br>0<br>-0 | +819<br>0<br>-0 | +27<br>792<br>-0 | +0<br>819<br>-23 | +819<br>0<br>-0 |
| Perl       | +798<br>0<br>-0 | +798<br>0<br>-0 | +798<br>0<br>-0 | +798<br>0<br>-0 | +0<br>798<br>-44 | +0<br>798<br>-21 | —    | +798<br>0<br>-0 | +798<br>0<br>-0 | +6<br>792<br>-0 | +0<br>798<br>-44 | +798<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-842 | +0<br>0<br>-819 | +0<br>0<br>-798 | —    | +0<br>0<br>-0 | +0<br>0<br>-792 | +0<br>0<br>-842 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-842 | +0<br>0<br>-819 | +0<br>0<br>-798 | +0<br>0<br>-0 | —      | +0<br>0<br>-792 | +0<br>0<br>-842 | +0<br>0<br>-0 |
| Ruby       | +792<br>0<br>-0 | +792<br>0<br>-0 | +792<br>0<br>-0 | +792<br>0<br>-0 | +0<br>792<br>-50 | +0<br>792<br>-27 | +0<br>792<br>-6 | +792<br>0<br>-0 | +792<br>0<br>-0 | —    | +0<br>792<br>-50 | +792<br>0<br>-0 |
| Rust       | +842<br>0<br>-0 | +842<br>0<br>-0 | +842<br>0<br>-0 | +842<br>0<br>-0 | +0<br>842<br>-0 | +23<br>819<br>-0 | +44<br>798<br>-0 | +842<br>0<br>-0 | +842<br>0<br>-0 | +50<br>792<br>-0 | —    | +842<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-842 | +0<br>0<br>-819 | +0<br>0<br>-798 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-792 | +0<br>0<br>-842 | —     |

#### Character Classes - POSIX - Long - Math Symbol (`[\p{Math_Symbol}]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-0 |
| Javascript | +948<br>0<br>-0 | +948<br>0<br>-0 | +948<br>0<br>-0 | +948<br>0<br>-0 | —          | +0<br>948<br>-0 | +0<br>948<br>-0 | +948<br>0<br>-0 | +948<br>0<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +948<br>0<br>-0 |
| Obj-C      | +948<br>0<br>-0 | +948<br>0<br>-0 | +948<br>0<br>-0 | +948<br>0<br>-0 | +0<br>948<br>-0 | —     | +0<br>948<br>-0 | +948<br>0<br>-0 | +948<br>0<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +948<br>0<br>-0 |
| Perl       | +948<br>0<br>-0 | +948<br>0<br>-0 | +948<br>0<br>-0 | +948<br>0<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | —    | +948<br>0<br>-0 | +948<br>0<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +948<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-948 | —    | +0<br>0<br>-0 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-0 | —      | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-0 |
| Ruby       | +948<br>0<br>-0 | +948<br>0<br>-0 | +948<br>0<br>-0 | +948<br>0<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +948<br>0<br>-0 | +948<br>0<br>-0 | —    | +0<br>948<br>-0 | +948<br>0<br>-0 |
| Rust       | +948<br>0<br>-0 | +948<br>0<br>-0 | +948<br>0<br>-0 | +948<br>0<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +948<br>0<br>-0 | +948<br>0<br>-0 | +0<br>948<br>-0 | —    | +948<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-948 | +0<br>0<br>-948 | —     |

#### Character Classes - POSIX - Long - Currency Symbol (`[\p{Currency_Symbol}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-63 | +0<br>0<br>-63 | +0<br>0<br>-62 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-62 | +0<br>0<br>-63 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-63 | +0<br>0<br>-63 | +0<br>0<br>-62 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-62 | +0<br>0<br>-63 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-63 | +0<br>0<br>-63 | +0<br>0<br>-62 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-62 | +0<br>0<br>-63 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-63 | +0<br>0<br>-63 | +0<br>0<br>-62 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-62 | +0<br>0<br>-63 | +0<br>0<br>-0 |
| Javascript | +63<br>0<br>-0 | +63<br>0<br>-0 | +63<br>0<br>-0 | +63<br>0<br>-0 | —          | +0<br>63<br>-0 | +1<br>62<br>-0 | +63<br>0<br>-0 | +63<br>0<br>-0 | +1<br>62<br>-0 | +0<br>63<br>-0 | +63<br>0<br>-0 |
| Obj-C      | +63<br>0<br>-0 | +63<br>0<br>-0 | +63<br>0<br>-0 | +63<br>0<br>-0 | +0<br>63<br>-0 | —     | +1<br>62<br>-0 | +63<br>0<br>-0 | +63<br>0<br>-0 | +1<br>62<br>-0 | +0<br>63<br>-0 | +63<br>0<br>-0 |
| Perl       | +62<br>0<br>-0 | +62<br>0<br>-0 | +62<br>0<br>-0 | +62<br>0<br>-0 | +0<br>62<br>-1 | +0<br>62<br>-1 | —    | +62<br>0<br>-0 | +62<br>0<br>-0 | +0<br>62<br>-0 | +0<br>62<br>-1 | +62<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-63 | +0<br>0<br>-63 | +0<br>0<br>-62 | —   | +0<br>0<br>-0 | +0<br>0<br>-62 | +0<br>0<br>-63 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-63 | +0<br>0<br>-63 | +0<br>0<br>-62 | +0<br>0<br>-0 | —      | +0<br>0<br>-62 | +0<br>0<br>-63 | +0<br>0<br>-0 |
| Ruby       | +62<br>0<br>-0 | +62<br>0<br>-0 | +62<br>0<br>-0 | +62<br>0<br>-0 | +0<br>62<br>-1 | +0<br>62<br>-1 | +0<br>62<br>-0 | +62<br>0<br>-0 | +62<br>0<br>-0 | —    | +0<br>62<br>-1 | +62<br>0<br>-0 |
| Rust       | +63<br>0<br>-0 | +63<br>0<br>-0 | +63<br>0<br>-0 | +63<br>0<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +1<br>62<br>-0 | +63<br>0<br>-0 | +63<br>0<br>-0 | +1<br>62<br>-0 | —    | +63<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-63 | +0<br>0<br>-63 | +0<br>0<br>-62 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-62 | +0<br>0<br>-63 | —     |

#### Character Classes - POSIX - Long - Modifier Symbol (`[\p{Modifier_Symbol}]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-125 | +0<br>0<br>-125 | +0<br>0<br>-123 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-121 | +0<br>0<br>-125 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-125 | +0<br>0<br>-125 | +0<br>0<br>-123 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-121 | +0<br>0<br>-125 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-125 | +0<br>0<br>-125 | +0<br>0<br>-123 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-121 | +0<br>0<br>-125 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-125 | +0<br>0<br>-125 | +0<br>0<br>-123 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-121 | +0<br>0<br>-125 | +0<br>0<br>-0 |
| Javascript | +125<br>0<br>-0 | +125<br>0<br>-0 | +125<br>0<br>-0 | +125<br>0<br>-0 | —          | +0<br>125<br>-0 | +2<br>123<br>-0 | +125<br>0<br>-0 | +125<br>0<br>-0 | +4<br>121<br>-0 | +0<br>125<br>-0 | +125<br>0<br>-0 |
| Obj-C      | +125<br>0<br>-0 | +125<br>0<br>-0 | +125<br>0<br>-0 | +125<br>0<br>-0 | +0<br>125<br>-0 | —     | +2<br>123<br>-0 | +125<br>0<br>-0 | +125<br>0<br>-0 | +4<br>121<br>-0 | +0<br>125<br>-0 | +125<br>0<br>-0 |
| Perl       | +123<br>0<br>-0 | +123<br>0<br>-0 | +123<br>0<br>-0 | +123<br>0<br>-0 | +0<br>123<br>-2 | +0<br>123<br>-2 | —    | +123<br>0<br>-0 | +123<br>0<br>-0 | +2<br>121<br>-0 | +0<br>123<br>-2 | +123<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-125 | +0<br>0<br>-125 | +0<br>0<br>-123 | —    | +0<br>0<br>-0 | +0<br>0<br>-121 | +0<br>0<br>-125 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-125 | +0<br>0<br>-125 | +0<br>0<br>-123 | +0<br>0<br>-0 | —      | +0<br>0<br>-121 | +0<br>0<br>-125 | +0<br>0<br>-0 |
| Ruby       | +121<br>0<br>-0 | +121<br>0<br>-0 | +121<br>0<br>-0 | +121<br>0<br>-0 | +0<br>121<br>-4 | +0<br>121<br>-4 | +0<br>121<br>-2 | +121<br>0<br>-0 | +121<br>0<br>-0 | —    | +0<br>121<br>-4 | +121<br>0<br>-0 |
| Rust       | +125<br>0<br>-0 | +125<br>0<br>-0 | +125<br>0<br>-0 | +125<br>0<br>-0 | +0<br>125<br>-0 | +0<br>125<br>-0 | +2<br>123<br>-0 | +125<br>0<br>-0 | +125<br>0<br>-0 | +4<br>121<br>-0 | —    | +125<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-125 | +0<br>0<br>-125 | +0<br>0<br>-123 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-121 | +0<br>0<br>-125 | —     |

#### Character Classes - POSIX - Long - Other Symbol (`[\p{Other_Symbol}]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-6634 | +0<br>0<br>-6605 | +0<br>0<br>-6431 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-6161 | +0<br>0<br>-6634 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-6634 | +0<br>0<br>-6605 | +0<br>0<br>-6431 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-6161 | +0<br>0<br>-6634 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-6634 | +0<br>0<br>-6605 | +0<br>0<br>-6431 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-6161 | +0<br>0<br>-6634 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —     | +0<br>0<br>-6634 | +0<br>0<br>-6605 | +0<br>0<br>-6431 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-6161 | +0<br>0<br>-6634 | +0<br>0<br>-0 |
| Javascript | +6634<br>0<br>-0 | +6634<br>0<br>-0 | +6634<br>0<br>-0 | +6634<br>0<br>-0 | —          | +29<br>6605<br>-0 | +203<br>6431<br>-0 | +6634<br>0<br>-0 | +6634<br>0<br>-0 | +473<br>6161<br>-0 | +0<br>6634<br>-0 | +6634<br>0<br>-0 |
| Obj-C      | +6605<br>0<br>-0 | +6605<br>0<br>-0 | +6605<br>0<br>-0 | +6605<br>0<br>-0 | +0<br>6605<br>-29 | —     | +174<br>6431<br>-0 | +6605<br>0<br>-0 | +6605<br>0<br>-0 | +444<br>6161<br>-0 | +0<br>6605<br>-29 | +6605<br>0<br>-0 |
| Perl       | +6431<br>0<br>-0 | +6431<br>0<br>-0 | +6431<br>0<br>-0 | +6431<br>0<br>-0 | +0<br>6431<br>-203 | +0<br>6431<br>-174 | —     | +6431<br>0<br>-0 | +6431<br>0<br>-0 | +270<br>6161<br>-0 | +0<br>6431<br>-203 | +6431<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-6634 | +0<br>0<br>-6605 | +0<br>0<br>-6431 | —     | +0<br>0<br>-0 | +0<br>0<br>-6161 | +0<br>0<br>-6634 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-6634 | +0<br>0<br>-6605 | +0<br>0<br>-6431 | +0<br>0<br>-0 | —      | +0<br>0<br>-6161 | +0<br>0<br>-6634 | +0<br>0<br>-0 |
| Ruby       | +6161<br>0<br>-0 | +6161<br>0<br>-0 | +6161<br>0<br>-0 | +6161<br>0<br>-0 | +0<br>6161<br>-473 | +0<br>6161<br>-444 | +0<br>6161<br>-270 | +6161<br>0<br>-0 | +6161<br>0<br>-0 | —     | +0<br>6161<br>-473 | +6161<br>0<br>-0 |
| Rust       | +6634<br>0<br>-0 | +6634<br>0<br>-0 | +6634<br>0<br>-0 | +6634<br>0<br>-0 | +0<br>6634<br>-0 | +29<br>6605<br>-0 | +203<br>6431<br>-0 | +6634<br>0<br>-0 | +6634<br>0<br>-0 | +473<br>6161<br>-0 | —     | +6634<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-6634 | +0<br>0<br>-6605 | +0<br>0<br>-6431 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-6161 | +0<br>0<br>-6634 | —     |

#### Character Classes - POSIX - Long - Symbol (`[\p{Symbol}]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-7770 | +0<br>0<br>-7741 | +0<br>0<br>-7564 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-7292 | +0<br>0<br>-7770 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-7770 | +0<br>0<br>-7741 | +0<br>0<br>-7564 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-7292 | +0<br>0<br>-7770 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-7770 | +0<br>0<br>-7741 | +0<br>0<br>-7564 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-7292 | +0<br>0<br>-7770 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —     | +0<br>0<br>-7770 | +0<br>0<br>-7741 | +0<br>0<br>-7564 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-7292 | +0<br>0<br>-7770 | +0<br>0<br>-0 |
| Javascript | +7770<br>0<br>-0 | +7770<br>0<br>-0 | +7770<br>0<br>-0 | +7770<br>0<br>-0 | —          | +29<br>7741<br>-0 | +206<br>7564<br>-0 | +7770<br>0<br>-0 | +7770<br>0<br>-0 | +478<br>7292<br>-0 | +0<br>7770<br>-0 | +7770<br>0<br>-0 |
| Obj-C      | +7741<br>0<br>-0 | +7741<br>0<br>-0 | +7741<br>0<br>-0 | +7741<br>0<br>-0 | +0<br>7741<br>-29 | —     | +177<br>7564<br>-0 | +7741<br>0<br>-0 | +7741<br>0<br>-0 | +449<br>7292<br>-0 | +0<br>7741<br>-29 | +7741<br>0<br>-0 |
| Perl       | +7564<br>0<br>-0 | +7564<br>0<br>-0 | +7564<br>0<br>-0 | +7564<br>0<br>-0 | +0<br>7564<br>-206 | +0<br>7564<br>-177 | —     | +7564<br>0<br>-0 | +7564<br>0<br>-0 | +272<br>7292<br>-0 | +0<br>7564<br>-206 | +7564<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-7770 | +0<br>0<br>-7741 | +0<br>0<br>-7564 | —     | +0<br>0<br>-0 | +0<br>0<br>-7292 | +0<br>0<br>-7770 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-7770 | +0<br>0<br>-7741 | +0<br>0<br>-7564 | +0<br>0<br>-0 | —      | +0<br>0<br>-7292 | +0<br>0<br>-7770 | +0<br>0<br>-0 |
| Ruby       | +7292<br>0<br>-0 | +7292<br>0<br>-0 | +7292<br>0<br>-0 | +7292<br>0<br>-0 | +0<br>7292<br>-478 | +0<br>7292<br>-449 | +0<br>7292<br>-272 | +7292<br>0<br>-0 | +7292<br>0<br>-0 | —     | +0<br>7292<br>-478 | +7292<br>0<br>-0 |
| Rust       | +7770<br>0<br>-0 | +7770<br>0<br>-0 | +7770<br>0<br>-0 | +7770<br>0<br>-0 | +0<br>7770<br>-0 | +29<br>7741<br>-0 | +206<br>7564<br>-0 | +7770<br>0<br>-0 | +7770<br>0<br>-0 | +478<br>7292<br>-0 | —     | +7770<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-7770 | +0<br>0<br>-7741 | +0<br>0<br>-7564 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-7292 | +0<br>0<br>-7770 | —     |

#### Character Classes - POSIX - Long - Space Separator (`[\p{Space_Separator}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-0 |
| Javascript | +17<br>0<br>-0 | +17<br>0<br>-0 | +17<br>0<br>-0 | +17<br>0<br>-0 | —          | +0<br>17<br>-0 | +0<br>17<br>-0 | +17<br>0<br>-0 | +17<br>0<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +17<br>0<br>-0 |
| Obj-C      | +17<br>0<br>-0 | +17<br>0<br>-0 | +17<br>0<br>-0 | +17<br>0<br>-0 | +0<br>17<br>-0 | —     | +0<br>17<br>-0 | +17<br>0<br>-0 | +17<br>0<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +17<br>0<br>-0 |
| Perl       | +17<br>0<br>-0 | +17<br>0<br>-0 | +17<br>0<br>-0 | +17<br>0<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | —    | +17<br>0<br>-0 | +17<br>0<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +17<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-17 | —   | +0<br>0<br>-0 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-0 | —      | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-0 |
| Ruby       | +17<br>0<br>-0 | +17<br>0<br>-0 | +17<br>0<br>-0 | +17<br>0<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +17<br>0<br>-0 | +17<br>0<br>-0 | —    | +0<br>17<br>-0 | +17<br>0<br>-0 |
| Rust       | +17<br>0<br>-0 | +17<br>0<br>-0 | +17<br>0<br>-0 | +17<br>0<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +17<br>0<br>-0 | +17<br>0<br>-0 | +0<br>17<br>-0 | —    | +17<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-17 | +0<br>0<br>-17 | —     |

#### Character Classes - POSIX - Long - Line Separator (`[\p{Line_Separator}]`)

| Language   | C++ | Go | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | -: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —  | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 |
| Javascript | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | —          | +0<br>1<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 |
| Obj-C      | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | —     | +0<br>1<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 |
| Perl       | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —    | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | —   | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 | —      | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 |
| Ruby       | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | —    | +0<br>1<br>-0 | +1<br>0<br>-0 |
| Rust       | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | —    | +1<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | —     |

#### Character Classes - POSIX - Long - Paragraph Separator (`[\p{Paragraph_Separator}]`)

| Language   | C++ | Go | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | -: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —  | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 |
| Javascript | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | —          | +0<br>1<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 |
| Obj-C      | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | —     | +0<br>1<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 |
| Perl       | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —    | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | —   | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 | —      | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 |
| Ruby       | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | —    | +0<br>1<br>-0 | +1<br>0<br>-0 |
| Rust       | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | —    | +1<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | —     |

#### Character Classes - POSIX - Long - Separator (`[\p{Separator}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-0 |
| Javascript | +19<br>0<br>-0 | +19<br>0<br>-0 | +19<br>0<br>-0 | +19<br>0<br>-0 | —          | +0<br>19<br>-0 | +0<br>19<br>-0 | +19<br>0<br>-0 | +19<br>0<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +19<br>0<br>-0 |
| Obj-C      | +19<br>0<br>-0 | +19<br>0<br>-0 | +19<br>0<br>-0 | +19<br>0<br>-0 | +0<br>19<br>-0 | —     | +0<br>19<br>-0 | +19<br>0<br>-0 | +19<br>0<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +19<br>0<br>-0 |
| Perl       | +19<br>0<br>-0 | +19<br>0<br>-0 | +19<br>0<br>-0 | +19<br>0<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | —    | +19<br>0<br>-0 | +19<br>0<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +19<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-19 | —   | +0<br>0<br>-0 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-0 | —      | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-0 |
| Ruby       | +19<br>0<br>-0 | +19<br>0<br>-0 | +19<br>0<br>-0 | +19<br>0<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +19<br>0<br>-0 | +19<br>0<br>-0 | —    | +0<br>19<br>-0 | +19<br>0<br>-0 |
| Rust       | +19<br>0<br>-0 | +19<br>0<br>-0 | +19<br>0<br>-0 | +19<br>0<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +19<br>0<br>-0 | +19<br>0<br>-0 | +0<br>19<br>-0 | —    | +19<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-19 | +0<br>0<br>-19 | —     |

#### Character Classes - POSIX - Long - Control (`[\p{Control}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —   | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-0 |
| Javascript | +65<br>0<br>-0 | +65<br>0<br>-0 | +65<br>0<br>-0 | +65<br>0<br>-0 | —          | +0<br>65<br>-0 | +0<br>65<br>-0 | +65<br>0<br>-0 | +65<br>0<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +65<br>0<br>-0 |
| Obj-C      | +65<br>0<br>-0 | +65<br>0<br>-0 | +65<br>0<br>-0 | +65<br>0<br>-0 | +0<br>65<br>-0 | —     | +0<br>65<br>-0 | +65<br>0<br>-0 | +65<br>0<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +65<br>0<br>-0 |
| Perl       | +65<br>0<br>-0 | +65<br>0<br>-0 | +65<br>0<br>-0 | +65<br>0<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | —    | +65<br>0<br>-0 | +65<br>0<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +65<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-65 | —   | +0<br>0<br>-0 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-0 | —      | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-0 |
| Ruby       | +65<br>0<br>-0 | +65<br>0<br>-0 | +65<br>0<br>-0 | +65<br>0<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +65<br>0<br>-0 | +65<br>0<br>-0 | —    | +0<br>65<br>-0 | +65<br>0<br>-0 |
| Rust       | +65<br>0<br>-0 | +65<br>0<br>-0 | +65<br>0<br>-0 | +65<br>0<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +65<br>0<br>-0 | +65<br>0<br>-0 | +0<br>65<br>-0 | —    | +65<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-65 | +0<br>0<br>-65 | —     |

#### Character Classes - POSIX - Long - Format (`[\p{Format}]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-170 | +0<br>0<br>-163 | +0<br>0<br>-161 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-161 | +0<br>0<br>-170 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —    | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-170 | +0<br>0<br>-163 | +0<br>0<br>-161 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-161 | +0<br>0<br>-170 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-170 | +0<br>0<br>-163 | +0<br>0<br>-161 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-161 | +0<br>0<br>-170 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —    | +0<br>0<br>-170 | +0<br>0<br>-163 | +0<br>0<br>-161 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-161 | +0<br>0<br>-170 | +0<br>0<br>-0 |
| Javascript | +170<br>0<br>-0 | +170<br>0<br>-0 | +170<br>0<br>-0 | +170<br>0<br>-0 | —          | +7<br>163<br>-0 | +9<br>161<br>-0 | +170<br>0<br>-0 | +170<br>0<br>-0 | +9<br>161<br>-0 | +0<br>170<br>-0 | +170<br>0<br>-0 |
| Obj-C      | +163<br>0<br>-0 | +163<br>0<br>-0 | +163<br>0<br>-0 | +163<br>0<br>-0 | +0<br>163<br>-7 | —     | +2<br>161<br>-0 | +163<br>0<br>-0 | +163<br>0<br>-0 | +2<br>161<br>-0 | +0<br>163<br>-7 | +163<br>0<br>-0 |
| Perl       | +161<br>0<br>-0 | +161<br>0<br>-0 | +161<br>0<br>-0 | +161<br>0<br>-0 | +0<br>161<br>-9 | +0<br>161<br>-2 | —    | +161<br>0<br>-0 | +161<br>0<br>-0 | +0<br>161<br>-0 | +0<br>161<br>-9 | +161<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-170 | +0<br>0<br>-163 | +0<br>0<br>-161 | —    | +0<br>0<br>-0 | +0<br>0<br>-161 | +0<br>0<br>-170 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-170 | +0<br>0<br>-163 | +0<br>0<br>-161 | +0<br>0<br>-0 | —      | +0<br>0<br>-161 | +0<br>0<br>-170 | +0<br>0<br>-0 |
| Ruby       | +161<br>0<br>-0 | +161<br>0<br>-0 | +161<br>0<br>-0 | +161<br>0<br>-0 | +0<br>161<br>-9 | +0<br>161<br>-2 | +0<br>161<br>-0 | +161<br>0<br>-0 | +161<br>0<br>-0 | —    | +0<br>161<br>-9 | +161<br>0<br>-0 |
| Rust       | +170<br>0<br>-0 | +170<br>0<br>-0 | +170<br>0<br>-0 | +170<br>0<br>-0 | +0<br>170<br>-0 | +7<br>163<br>-0 | +9<br>161<br>-0 | +170<br>0<br>-0 | +170<br>0<br>-0 | +9<br>161<br>-0 | —    | +170<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-170 | +0<br>0<br>-163 | +0<br>0<br>-161 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-161 | +0<br>0<br>-170 | —     |

#### Character Classes - POSIX - Long - Surrogate (`[\p{Surrogate}]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —     | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 |
| Javascript | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | —          | +2048<br>0<br>-0 | +0<br>2048<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 |
| Obj-C      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 | —     | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 |
| Perl       | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +0<br>2048<br>-0 | +2048<br>0<br>-0 | —     | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | —      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 |
| Ruby       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-0 | —     | +0<br>0<br>-0 | +0<br>0<br>-0 |
| Rust       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —     | +0<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —     |

#### Character Classes - POSIX - Long - Private Use (`[\p{Private_Use}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-0 |
| Javascript | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +137468<br>0<br>-0 | —          | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +137468<br>0<br>-0 |
| Obj-C      | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | —       | +0<br>137468<br>-0 | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +137468<br>0<br>-0 |
| Perl       | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | —       | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +137468<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | —       | +0<br>0<br>-0 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-0 | —       | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-0 |
| Ruby       | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +137468<br>0<br>-0 | +137468<br>0<br>-0 | —       | +0<br>137468<br>-0 | +137468<br>0<br>-0 |
| Rust       | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +137468<br>0<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | —       | +137468<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | —       |

#### Character Classes - POSIX - Long - Unassigned (`[\p{Unassigned}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-825345 | +0<br>0<br>-829834 | +0<br>0<br>-830672 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-836602 | +0<br>0<br>-825345 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-825345 | +0<br>0<br>-829834 | +0<br>0<br>-830672 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-836602 | +0<br>0<br>-825345 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-825345 | +0<br>0<br>-829834 | +0<br>0<br>-830672 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-836602 | +0<br>0<br>-825345 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-825345 | +0<br>0<br>-829834 | +0<br>0<br>-830672 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-836602 | +0<br>0<br>-825345 | +0<br>0<br>-0 |
| Javascript | +825345<br>0<br>-0 | +825345<br>0<br>-0 | +825345<br>0<br>-0 | +825345<br>0<br>-0 | —          | +0<br>825345<br>-4489 | +0<br>825345<br>-5327 | +825345<br>0<br>-0 | +825345<br>0<br>-0 | +0<br>825345<br>-11257 | +0<br>825345<br>-0 | +825345<br>0<br>-0 |
| Obj-C      | +829834<br>0<br>-0 | +829834<br>0<br>-0 | +829834<br>0<br>-0 | +829834<br>0<br>-0 | +4489<br>825345<br>-0 | —       | +0<br>829834<br>-838 | +829834<br>0<br>-0 | +829834<br>0<br>-0 | +0<br>829834<br>-6768 | +4489<br>825345<br>-0 | +829834<br>0<br>-0 |
| Perl       | +830672<br>0<br>-0 | +830672<br>0<br>-0 | +830672<br>0<br>-0 | +830672<br>0<br>-0 | +5327<br>825345<br>-0 | +838<br>829834<br>-0 | —       | +830672<br>0<br>-0 | +830672<br>0<br>-0 | +0<br>830672<br>-5930 | +5327<br>825345<br>-0 | +830672<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-825345 | +0<br>0<br>-829834 | +0<br>0<br>-830672 | —       | +0<br>0<br>-0 | +0<br>0<br>-836602 | +0<br>0<br>-825345 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-825345 | +0<br>0<br>-829834 | +0<br>0<br>-830672 | +0<br>0<br>-0 | —       | +0<br>0<br>-836602 | +0<br>0<br>-825345 | +0<br>0<br>-0 |
| Ruby       | +836602<br>0<br>-0 | +836602<br>0<br>-0 | +836602<br>0<br>-0 | +836602<br>0<br>-0 | +11257<br>825345<br>-0 | +6768<br>829834<br>-0 | +5930<br>830672<br>-0 | +836602<br>0<br>-0 | +836602<br>0<br>-0 | —       | +11257<br>825345<br>-0 | +836602<br>0<br>-0 |
| Rust       | +825345<br>0<br>-0 | +825345<br>0<br>-0 | +825345<br>0<br>-0 | +825345<br>0<br>-0 | +0<br>825345<br>-0 | +0<br>825345<br>-4489 | +0<br>825345<br>-5327 | +825345<br>0<br>-0 | +825345<br>0<br>-0 | +0<br>825345<br>-11257 | —       | +825345<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-825345 | +0<br>0<br>-829834 | +0<br>0<br>-830672 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-836602 | +0<br>0<br>-825345 | —       |

#### Character Classes - POSIX - Long - Other (`[\p{Other}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-965096 | +0<br>0<br>-967530 | +0<br>0<br>-970414 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-974296 | +0<br>0<br>-963048 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-965096 | +0<br>0<br>-967530 | +0<br>0<br>-970414 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-974296 | +0<br>0<br>-963048 | +0<br>0<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-965096 | +0<br>0<br>-967530 | +0<br>0<br>-970414 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-974296 | +0<br>0<br>-963048 | +0<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-965096 | +0<br>0<br>-967530 | +0<br>0<br>-970414 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-974296 | +0<br>0<br>-963048 | +0<br>0<br>-0 |
| Javascript | +965096<br>0<br>-0 | +965096<br>0<br>-0 | +965096<br>0<br>-0 | +965096<br>0<br>-0 | —          | +2048<br>963048<br>-4482 | +0<br>965096<br>-5318 | +965096<br>0<br>-0 | +965096<br>0<br>-0 | +2048<br>963048<br>-11248 | +2048<br>963048<br>-0 | +965096<br>0<br>-0 |
| Obj-C      | +967530<br>0<br>-0 | +967530<br>0<br>-0 | +967530<br>0<br>-0 | +967530<br>0<br>-0 | +4482<br>963048<br>-2048 | —       | +0<br>967530<br>-2884 | +967530<br>0<br>-0 | +967530<br>0<br>-0 | +0<br>967530<br>-6766 | +4482<br>963048<br>-0 | +967530<br>0<br>-0 |
| Perl       | +970414<br>0<br>-0 | +970414<br>0<br>-0 | +970414<br>0<br>-0 | +970414<br>0<br>-0 | +5318<br>965096<br>-0 | +2884<br>967530<br>-0 | —       | +970414<br>0<br>-0 | +970414<br>0<br>-0 | +2048<br>968366<br>-5930 | +7366<br>963048<br>-0 | +970414<br>0<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-965096 | +0<br>0<br>-967530 | +0<br>0<br>-970414 | —       | +0<br>0<br>-0 | +0<br>0<br>-974296 | +0<br>0<br>-963048 | +0<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-965096 | +0<br>0<br>-967530 | +0<br>0<br>-970414 | +0<br>0<br>-0 | —       | +0<br>0<br>-974296 | +0<br>0<br>-963048 | +0<br>0<br>-0 |
| Ruby       | +974296<br>0<br>-0 | +974296<br>0<br>-0 | +974296<br>0<br>-0 | +974296<br>0<br>-0 | +11248<br>963048<br>-2048 | +6766<br>967530<br>-0 | +5930<br>968366<br>-2048 | +974296<br>0<br>-0 | +974296<br>0<br>-0 | —       | +11248<br>963048<br>-0 | +974296<br>0<br>-0 |
| Rust       | +963048<br>0<br>-0 | +963048<br>0<br>-0 | +963048<br>0<br>-0 | +963048<br>0<br>-0 | +0<br>963048<br>-2048 | +0<br>963048<br>-4482 | +0<br>963048<br>-7366 | +963048<br>0<br>-0 | +963048<br>0<br>-0 | +0<br>963048<br>-11248 | —       | +963048<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-965096 | +0<br>0<br>-967530 | +0<br>0<br>-970414 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-974296 | +0<br>0<br>-963048 | —       |

---

### Character Classes - POSIX - Short

1. [Uppercase Letter](#character-classes---posix---short---uppercase-letter-plu) (`[\p{Lu}]`)
2. [Lowercase Letter](#character-classes---posix---short---lowercase-letter-pll) (`[\p{Ll}]`)
3. [Titlecase Letter](#character-classes---posix---short---titlecase-letter-plt) (`[\p{Lt}]`)
4. [Cased Letter](#character-classes---posix---short---cased-letter-plc) (`[\p{LC}]`)
5. [Cased Letter Amp](#character-classes---posix---short---cased-letter-amp-pl) (`[\p{L&}]`)
6. [Modifier Letter](#character-classes---posix---short---modifier-letter-plm) (`[\p{Lm}]`)
7. [Other Letter](#character-classes---posix---short---other-letter-plo) (`[\p{Lo}]`)
8. [Letter](#character-classes---posix---short---letter-pl) (`[\p{L}]`)
9. [Nonspacing Mark](#character-classes---posix---short---nonspacing-mark-pmn) (`[\p{Mn}]`)
10. [Spacing Mark](#character-classes---posix---short---spacing-mark-pmc) (`[\p{Mc}]`)
11. [Enclosing Mark](#character-classes---posix---short---enclosing-mark-pme) (`[\p{Me}]`)
12. [Mark](#character-classes---posix---short---mark-pm) (`[\p{M}]`)
13. [Decimal Number](#character-classes---posix---short---decimal-number-pnd) (`[\p{Nd}]`)
14. [Letter Number](#character-classes---posix---short---letter-number-pnl) (`[\p{Nl}]`)
15. [Other Number](#character-classes---posix---short---other-number-pno) (`[\p{No}]`)
16. [Number](#character-classes---posix---short---number-pn) (`[\p{N}]`)
17. [Connector Punctuation](#character-classes---posix---short---connector-punctuation-ppc) (`[\p{Pc}]`)
18. [Dash Punctuation](#character-classes---posix---short---dash-punctuation-ppd) (`[\p{Pd}]`)
19. [Open Punctuation](#character-classes---posix---short---open-punctuation-pps) (`[\p{Ps}]`)
20. [Close Punctuation](#character-classes---posix---short---close-punctuation-ppe) (`[\p{Pe}]`)
21. [Initial Punctuation](#character-classes---posix---short---initial-punctuation-ppi) (`[\p{Pi}]`)
22. [Final Punctuation](#character-classes---posix---short---final-punctuation-ppf) (`[\p{Pf}]`)
23. [Other Punctuation](#character-classes---posix---short---other-punctuation-ppo) (`[\p{Po}]`)
24. [Punctuation](#character-classes---posix---short---punctuation-pp) (`[\p{P}]`)
25. [Math Symbol](#character-classes---posix---short---math-symbol-psm) (`[\p{Sm}]`)
26. [Currency Symbol](#character-classes---posix---short---currency-symbol-psc) (`[\p{Sc}]`)
27. [Modifier Symbol](#character-classes---posix---short---modifier-symbol-psk) (`[\p{Sk}]`)
28. [Other Symbol](#character-classes---posix---short---other-symbol-pso) (`[\p{So}]`)
29. [Symbol](#character-classes---posix---short---symbol-ps) (`[\p{S}]`)
30. [Space Separator](#character-classes---posix---short---space-separator-pzs) (`[\p{Zs}]`)
31. [Line Separator](#character-classes---posix---short---line-separator-pzl) (`[\p{Zl}]`)
32. [Paragraph Separator](#character-classes---posix---short---paragraph-separator-pzp) (`[\p{Zp}]`)
33. [Separator](#character-classes---posix---short---separator-pz) (`[\p{Z}]`)
34. [Control](#character-classes---posix---short---control-pcc) (`[\p{Cc}]`)
35. [Format](#character-classes---posix---short---format-pcf) (`[\p{Cf}]`)
36. [Surrogate](#character-classes---posix---short---surrogate-pcs) (`[\p{Cs}]`)
37. [Private Use](#character-classes---posix---short---private-use-pco) (`[\p{Co}]`)
38. [Unassigned](#character-classes---posix---short---unassigned-pcn) (`[\p{Cn}]`)
39. [Other](#character-classes---posix---short---other-pc) (`[\p{C}]`)

#### Character Classes - POSIX - Short - Uppercase Letter (`[\p{Lu}]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>0<br>-1831 | +0<br>0<br>-1818 | +0<br>0<br>-1791 | +0<br>0<br>-1831 | +0<br>0<br>-1831 | +0<br>0<br>-1791 | +0<br>0<br>-1831 | +0<br>0<br>-1831 | +0<br>0<br>-1788 | +0<br>0<br>-1831 | +0<br>0<br>-1791 |
| Go         | +1831<br>0<br>-0 | —     | +1363<br>468<br>-1350 | +40<br>1791<br>-0 | +0<br>1831<br>-0 | +0<br>1831<br>-0 | +40<br>1791<br>-0 | +0<br>1831<br>-0 | +0<br>1831<br>-0 | +43<br>1788<br>-0 | +0<br>1831<br>-0 | +40<br>1791<br>-0 |
| Haskell    | +1818<br>0<br>-0 | +1350<br>468<br>-1363 | —       | +1350<br>468<br>-1323 | +1350<br>468<br>-1363 | +1350<br>468<br>-1363 | +1350<br>468<br>-1323 | +1350<br>468<br>-1363 | +1350<br>468<br>-1363 | +1350<br>468<br>-1320 | +1350<br>468<br>-1363 | +1350<br>468<br>-1323 |
| Java       | +1791<br>0<br>-0 | +0<br>1791<br>-40 | +1323<br>468<br>-1350 | —     | +0<br>1791<br>-40 | +0<br>1791<br>-40 | +0<br>1791<br>-0 | +0<br>1791<br>-40 | +0<br>1791<br>-40 | +3<br>1788<br>-0 | +0<br>1791<br>-40 | +0<br>1791<br>-0 |
| Javascript | +1831<br>0<br>-0 | +0<br>1831<br>-0 | +1363<br>468<br>-1350 | +40<br>1791<br>-0 | —          | +0<br>1831<br>-0 | +40<br>1791<br>-0 | +0<br>1831<br>-0 | +0<br>1831<br>-0 | +43<br>1788<br>-0 | +0<br>1831<br>-0 | +40<br>1791<br>-0 |
| Obj-C      | +1831<br>0<br>-0 | +0<br>1831<br>-0 | +1363<br>468<br>-1350 | +40<br>1791<br>-0 | +0<br>1831<br>-0 | —     | +40<br>1791<br>-0 | +0<br>1831<br>-0 | +0<br>1831<br>-0 | +43<br>1788<br>-0 | +0<br>1831<br>-0 | +40<br>1791<br>-0 |
| Perl       | +1791<br>0<br>-0 | +0<br>1791<br>-40 | +1323<br>468<br>-1350 | +0<br>1791<br>-0 | +0<br>1791<br>-40 | +0<br>1791<br>-40 | —     | +0<br>1791<br>-40 | +0<br>1791<br>-40 | +3<br>1788<br>-0 | +0<br>1791<br>-40 | +0<br>1791<br>-0 |
| PHP        | +1831<br>0<br>-0 | +0<br>1831<br>-0 | +1363<br>468<br>-1350 | +40<br>1791<br>-0 | +0<br>1831<br>-0 | +0<br>1831<br>-0 | +40<br>1791<br>-0 | —     | +0<br>1831<br>-0 | +43<br>1788<br>-0 | +0<br>1831<br>-0 | +40<br>1791<br>-0 |
| Python     | +1831<br>0<br>-0 | +0<br>1831<br>-0 | +1363<br>468<br>-1350 | +40<br>1791<br>-0 | +0<br>1831<br>-0 | +0<br>1831<br>-0 | +40<br>1791<br>-0 | +0<br>1831<br>-0 | —      | +43<br>1788<br>-0 | +0<br>1831<br>-0 | +40<br>1791<br>-0 |
| Ruby       | +1788<br>0<br>-0 | +0<br>1788<br>-43 | +1320<br>468<br>-1350 | +0<br>1788<br>-3 | +0<br>1788<br>-43 | +0<br>1788<br>-43 | +0<br>1788<br>-3 | +0<br>1788<br>-43 | +0<br>1788<br>-43 | —     | +0<br>1788<br>-43 | +0<br>1788<br>-3 |
| Rust       | +1831<br>0<br>-0 | +0<br>1831<br>-0 | +1363<br>468<br>-1350 | +40<br>1791<br>-0 | +0<br>1831<br>-0 | +0<br>1831<br>-0 | +40<br>1791<br>-0 | +0<br>1831<br>-0 | +0<br>1831<br>-0 | +43<br>1788<br>-0 | —     | +40<br>1791<br>-0 |
| Scala      | +1791<br>0<br>-0 | +0<br>1791<br>-40 | +1323<br>468<br>-1350 | +0<br>1791<br>-0 | +0<br>1791<br>-40 | +0<br>1791<br>-40 | +0<br>1791<br>-0 | +0<br>1791<br>-40 | +0<br>1791<br>-40 | +3<br>1788<br>-0 | +0<br>1791<br>-40 | —     |

#### Character Classes - POSIX - Short - Lowercase Letter (`[\p{Ll}]`)

| Language   | C++      | Go       | Haskell  | Java     | Javascript | Obj-C    | Perl     | PHP      | Python   | Ruby     | Rust     | Scala    |
| :--------- | -------: | -------: | -------: | -------: | ---------: | -------: | -------: | -------: | -------: | -------: | -------: | -------: |
| C++        | —        | +0<br>0<br>-2233 | +0<br>0<br>-1112183 | +0<br>0<br>-2155 | +0<br>0<br>-2233 | +0<br>0<br>-2227 | +0<br>0<br>-2155 | +0<br>0<br>-2227 | +0<br>0<br>-2233 | +0<br>0<br>-2151 | +0<br>0<br>-2233 | +0<br>0<br>-2155 |
| Go         | +2233<br>0<br>-0 | —        | +531<br>1702<br>-1110481 | +78<br>2155<br>-0 | +0<br>2233<br>-0 | +6<br>2227<br>-0 | +78<br>2155<br>-0 | +6<br>2227<br>-0 | +0<br>2233<br>-0 | +82<br>2151<br>-0 | +0<br>2233<br>-0 | +78<br>2155<br>-0 |
| Haskell    | +1112183<br>0<br>-0 | +1110481<br>1702<br>-531 | —        | +1110559<br>1624<br>-531 | +1110481<br>1702<br>-531 | +1110487<br>1696<br>-531 | +1110559<br>1624<br>-531 | +1110487<br>1696<br>-531 | +1110481<br>1702<br>-531 | +1110563<br>1620<br>-531 | +1110481<br>1702<br>-531 | +1110559<br>1624<br>-531 |
| Java       | +2155<br>0<br>-0 | +0<br>2155<br>-78 | +531<br>1624<br>-1110559 | —        | +0<br>2155<br>-78 | +0<br>2155<br>-72 | +0<br>2155<br>-0 | +0<br>2155<br>-72 | +0<br>2155<br>-78 | +4<br>2151<br>-0 | +0<br>2155<br>-78 | +0<br>2155<br>-0 |
| Javascript | +2233<br>0<br>-0 | +0<br>2233<br>-0 | +531<br>1702<br>-1110481 | +78<br>2155<br>-0 | —          | +6<br>2227<br>-0 | +78<br>2155<br>-0 | +6<br>2227<br>-0 | +0<br>2233<br>-0 | +82<br>2151<br>-0 | +0<br>2233<br>-0 | +78<br>2155<br>-0 |
| Obj-C      | +2227<br>0<br>-0 | +0<br>2227<br>-6 | +531<br>1696<br>-1110487 | +72<br>2155<br>-0 | +0<br>2227<br>-6 | —        | +72<br>2155<br>-0 | +0<br>2227<br>-0 | +0<br>2227<br>-6 | +76<br>2151<br>-0 | +0<br>2227<br>-6 | +72<br>2155<br>-0 |
| Perl       | +2155<br>0<br>-0 | +0<br>2155<br>-78 | +531<br>1624<br>-1110559 | +0<br>2155<br>-0 | +0<br>2155<br>-78 | +0<br>2155<br>-72 | —        | +0<br>2155<br>-72 | +0<br>2155<br>-78 | +4<br>2151<br>-0 | +0<br>2155<br>-78 | +0<br>2155<br>-0 |
| PHP        | +2227<br>0<br>-0 | +0<br>2227<br>-6 | +531<br>1696<br>-1110487 | +72<br>2155<br>-0 | +0<br>2227<br>-6 | +0<br>2227<br>-0 | +72<br>2155<br>-0 | —        | +0<br>2227<br>-6 | +76<br>2151<br>-0 | +0<br>2227<br>-6 | +72<br>2155<br>-0 |
| Python     | +2233<br>0<br>-0 | +0<br>2233<br>-0 | +531<br>1702<br>-1110481 | +78<br>2155<br>-0 | +0<br>2233<br>-0 | +6<br>2227<br>-0 | +78<br>2155<br>-0 | +6<br>2227<br>-0 | —        | +82<br>2151<br>-0 | +0<br>2233<br>-0 | +78<br>2155<br>-0 |
| Ruby       | +2151<br>0<br>-0 | +0<br>2151<br>-82 | +531<br>1620<br>-1110563 | +0<br>2151<br>-4 | +0<br>2151<br>-82 | +0<br>2151<br>-76 | +0<br>2151<br>-4 | +0<br>2151<br>-76 | +0<br>2151<br>-82 | —        | +0<br>2151<br>-82 | +0<br>2151<br>-4 |
| Rust       | +2233<br>0<br>-0 | +0<br>2233<br>-0 | +531<br>1702<br>-1110481 | +78<br>2155<br>-0 | +0<br>2233<br>-0 | +6<br>2227<br>-0 | +78<br>2155<br>-0 | +6<br>2227<br>-0 | +0<br>2233<br>-0 | +82<br>2151<br>-0 | —        | +78<br>2155<br>-0 |
| Scala      | +2155<br>0<br>-0 | +0<br>2155<br>-78 | +531<br>1624<br>-1110559 | +0<br>2155<br>-0 | +0<br>2155<br>-78 | +0<br>2155<br>-72 | +0<br>2155<br>-0 | +0<br>2155<br>-72 | +0<br>2155<br>-78 | +4<br>2151<br>-0 | +0<br>2155<br>-78 | —        |

#### Character Classes - POSIX - Short - Titlecase Letter (`[\p{Lt}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-31 | +0<br>0<br>-0 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 |
| Go         | +31<br>0<br>-0 | —   | +31<br>0<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-31 | —       | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 | +0<br>0<br>-31 |
| Java       | +31<br>0<br>-0 | +0<br>31<br>-0 | +31<br>0<br>-0 | —    | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 |
| Javascript | +31<br>0<br>-0 | +0<br>31<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | —          | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 |
| Obj-C      | +31<br>0<br>-0 | +0<br>31<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | —     | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 |
| Perl       | +31<br>0<br>-0 | +0<br>31<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | —    | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 |
| PHP        | +31<br>0<br>-0 | +0<br>31<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | —   | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 |
| Python     | +31<br>0<br>-0 | +0<br>31<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | —      | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 |
| Ruby       | +31<br>0<br>-0 | +0<br>31<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | —    | +0<br>31<br>-0 | +0<br>31<br>-0 |
| Rust       | +31<br>0<br>-0 | +0<br>31<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | —    | +0<br>31<br>-0 |
| Scala      | +31<br>0<br>-0 | +0<br>31<br>-0 | +31<br>0<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | +0<br>31<br>-0 | —     |

#### Character Classes - POSIX - Short - Cased Letter (`[\p{LC}]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3977 | +0<br>0<br>-4095 | +0<br>0<br>-4089 | +0<br>0<br>-3977 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3970 | +0<br>0<br>-4095 | +0<br>0<br>-3977 |
| Go         | +0<br>0<br>-0 | —     | +0<br>0<br>-0 | +0<br>0<br>-3977 | +0<br>0<br>-4095 | +0<br>0<br>-4089 | +0<br>0<br>-3977 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3970 | +0<br>0<br>-4095 | +0<br>0<br>-3977 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-3977 | +0<br>0<br>-4095 | +0<br>0<br>-4089 | +0<br>0<br>-3977 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3970 | +0<br>0<br>-4095 | +0<br>0<br>-3977 |
| Java       | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +3977<br>0<br>-0 | —     | +0<br>3977<br>-118 | +0<br>3977<br>-112 | +0<br>3977<br>-0 | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +7<br>3970<br>-0 | +0<br>3977<br>-118 | +0<br>3977<br>-0 |
| Javascript | +4095<br>0<br>-0 | +4095<br>0<br>-0 | +4095<br>0<br>-0 | +118<br>3977<br>-0 | —          | +6<br>4089<br>-0 | +118<br>3977<br>-0 | +4095<br>0<br>-0 | +4095<br>0<br>-0 | +125<br>3970<br>-0 | +0<br>4095<br>-0 | +118<br>3977<br>-0 |
| Obj-C      | +4089<br>0<br>-0 | +4089<br>0<br>-0 | +4089<br>0<br>-0 | +112<br>3977<br>-0 | +0<br>4089<br>-6 | —     | +112<br>3977<br>-0 | +4089<br>0<br>-0 | +4089<br>0<br>-0 | +119<br>3970<br>-0 | +0<br>4089<br>-6 | +112<br>3977<br>-0 |
| Perl       | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +0<br>3977<br>-0 | +0<br>3977<br>-118 | +0<br>3977<br>-112 | —     | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +7<br>3970<br>-0 | +0<br>3977<br>-118 | +0<br>3977<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3977 | +0<br>0<br>-4095 | +0<br>0<br>-4089 | +0<br>0<br>-3977 | —     | +0<br>0<br>-0 | +0<br>0<br>-3970 | +0<br>0<br>-4095 | +0<br>0<br>-3977 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3977 | +0<br>0<br>-4095 | +0<br>0<br>-4089 | +0<br>0<br>-3977 | +0<br>0<br>-0 | —      | +0<br>0<br>-3970 | +0<br>0<br>-4095 | +0<br>0<br>-3977 |
| Ruby       | +3970<br>0<br>-0 | +3970<br>0<br>-0 | +3970<br>0<br>-0 | +0<br>3970<br>-7 | +0<br>3970<br>-125 | +0<br>3970<br>-119 | +0<br>3970<br>-7 | +3970<br>0<br>-0 | +3970<br>0<br>-0 | —     | +0<br>3970<br>-125 | +0<br>3970<br>-7 |
| Rust       | +4095<br>0<br>-0 | +4095<br>0<br>-0 | +4095<br>0<br>-0 | +118<br>3977<br>-0 | +0<br>4095<br>-0 | +6<br>4089<br>-0 | +118<br>3977<br>-0 | +4095<br>0<br>-0 | +4095<br>0<br>-0 | +125<br>3970<br>-0 | —     | +118<br>3977<br>-0 |
| Scala      | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +0<br>3977<br>-0 | +0<br>3977<br>-118 | +0<br>3977<br>-112 | +0<br>3977<br>-0 | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +7<br>3970<br>-0 | +0<br>3977<br>-118 | —     |

#### Character Classes - POSIX - Short - Cased Letter Amp (`[\p{L&}]`)

| Language   | C++      | Go       | Haskell  | Java     | Javascript | Obj-C    | Perl     | PHP      | Python   | Ruby     | Rust     | Scala    |
| :--------- | -------: | -------: | -------: | -------: | ---------: | -------: | -------: | -------: | -------: | -------: | -------: | -------: |
| C++        | —        | +0<br>0<br>-0 | +0<br>0<br>-1113973 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3977 | +0<br>0<br>-4089 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 |
| Go         | +0<br>0<br>-0 | —        | +0<br>0<br>-1113973 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3977 | +0<br>0<br>-4089 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 |
| Haskell    | +1113973<br>0<br>-0 | +1113973<br>0<br>-0 | —        | +1113973<br>0<br>-0 | +1113973<br>0<br>-0 | +1113973<br>0<br>-0 | +1109996<br>3977<br>-0 | +1109884<br>4089<br>-0 | +1113973<br>0<br>-0 | +1113973<br>0<br>-0 | +1113973<br>0<br>-0 | +1113973<br>0<br>-0 |
| Java       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1113973 | —        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3977 | +0<br>0<br>-4089 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 |
| Javascript | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1113973 | +0<br>0<br>-0 | —          | +0<br>0<br>-0 | +0<br>0<br>-3977 | +0<br>0<br>-4089 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 |
| Obj-C      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1113973 | +0<br>0<br>-0 | +0<br>0<br>-0 | —        | +0<br>0<br>-3977 | +0<br>0<br>-4089 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 |
| Perl       | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +0<br>3977<br>-1109996 | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +3977<br>0<br>-0 | —        | +0<br>3977<br>-112 | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +3977<br>0<br>-0 | +3977<br>0<br>-0 |
| PHP        | +4089<br>0<br>-0 | +4089<br>0<br>-0 | +0<br>4089<br>-1109884 | +4089<br>0<br>-0 | +4089<br>0<br>-0 | +4089<br>0<br>-0 | +112<br>3977<br>-0 | —        | +4089<br>0<br>-0 | +4089<br>0<br>-0 | +4089<br>0<br>-0 | +4089<br>0<br>-0 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1113973 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3977 | +0<br>0<br>-4089 | —        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 |
| Ruby       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1113973 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3977 | +0<br>0<br>-4089 | +0<br>0<br>-0 | —        | +0<br>0<br>-0 | +0<br>0<br>-0 |
| Rust       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1113973 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3977 | +0<br>0<br>-4089 | +0<br>0<br>-0 | +0<br>0<br>-0 | —        | +0<br>0<br>-0 |
| Scala      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-1113973 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-3977 | +0<br>0<br>-4089 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —        |

#### Character Classes - POSIX - Short - Modifier Letter (`[\p{Lm}]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>0<br>-397 | +0<br>0<br>-0 | +0<br>0<br>-260 | +0<br>0<br>-397 | +0<br>0<br>-334 | +0<br>0<br>-260 | +0<br>0<br>-334 | +0<br>0<br>-397 | +0<br>0<br>-259 | +0<br>0<br>-397 | +0<br>0<br>-260 |
| Go         | +397<br>0<br>-0 | —    | +397<br>0<br>-0 | +137<br>260<br>-0 | +0<br>397<br>-0 | +63<br>334<br>-0 | +137<br>260<br>-0 | +63<br>334<br>-0 | +0<br>397<br>-0 | +138<br>259<br>-0 | +0<br>397<br>-0 | +137<br>260<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-397 | —       | +0<br>0<br>-260 | +0<br>0<br>-397 | +0<br>0<br>-334 | +0<br>0<br>-260 | +0<br>0<br>-334 | +0<br>0<br>-397 | +0<br>0<br>-259 | +0<br>0<br>-397 | +0<br>0<br>-260 |
| Java       | +260<br>0<br>-0 | +0<br>260<br>-137 | +260<br>0<br>-0 | —    | +0<br>260<br>-137 | +0<br>260<br>-74 | +0<br>260<br>-0 | +0<br>260<br>-74 | +0<br>260<br>-137 | +1<br>259<br>-0 | +0<br>260<br>-137 | +0<br>260<br>-0 |
| Javascript | +397<br>0<br>-0 | +0<br>397<br>-0 | +397<br>0<br>-0 | +137<br>260<br>-0 | —          | +63<br>334<br>-0 | +137<br>260<br>-0 | +63<br>334<br>-0 | +0<br>397<br>-0 | +138<br>259<br>-0 | +0<br>397<br>-0 | +137<br>260<br>-0 |
| Obj-C      | +334<br>0<br>-0 | +0<br>334<br>-63 | +334<br>0<br>-0 | +74<br>260<br>-0 | +0<br>334<br>-63 | —     | +74<br>260<br>-0 | +0<br>334<br>-0 | +0<br>334<br>-63 | +75<br>259<br>-0 | +0<br>334<br>-63 | +74<br>260<br>-0 |
| Perl       | +260<br>0<br>-0 | +0<br>260<br>-137 | +260<br>0<br>-0 | +0<br>260<br>-0 | +0<br>260<br>-137 | +0<br>260<br>-74 | —    | +0<br>260<br>-74 | +0<br>260<br>-137 | +1<br>259<br>-0 | +0<br>260<br>-137 | +0<br>260<br>-0 |
| PHP        | +334<br>0<br>-0 | +0<br>334<br>-63 | +334<br>0<br>-0 | +74<br>260<br>-0 | +0<br>334<br>-63 | +0<br>334<br>-0 | +74<br>260<br>-0 | —    | +0<br>334<br>-63 | +75<br>259<br>-0 | +0<br>334<br>-63 | +74<br>260<br>-0 |
| Python     | +397<br>0<br>-0 | +0<br>397<br>-0 | +397<br>0<br>-0 | +137<br>260<br>-0 | +0<br>397<br>-0 | +63<br>334<br>-0 | +137<br>260<br>-0 | +63<br>334<br>-0 | —      | +138<br>259<br>-0 | +0<br>397<br>-0 | +137<br>260<br>-0 |
| Ruby       | +259<br>0<br>-0 | +0<br>259<br>-138 | +259<br>0<br>-0 | +0<br>259<br>-1 | +0<br>259<br>-138 | +0<br>259<br>-75 | +0<br>259<br>-1 | +0<br>259<br>-75 | +0<br>259<br>-138 | —    | +0<br>259<br>-138 | +0<br>259<br>-1 |
| Rust       | +397<br>0<br>-0 | +0<br>397<br>-0 | +397<br>0<br>-0 | +137<br>260<br>-0 | +0<br>397<br>-0 | +63<br>334<br>-0 | +137<br>260<br>-0 | +63<br>334<br>-0 | +0<br>397<br>-0 | +138<br>259<br>-0 | —    | +137<br>260<br>-0 |
| Scala      | +260<br>0<br>-0 | +0<br>260<br>-137 | +260<br>0<br>-0 | +0<br>260<br>-0 | +0<br>260<br>-137 | +0<br>260<br>-74 | +0<br>260<br>-0 | +0<br>260<br>-74 | +0<br>260<br>-137 | +1<br>259<br>-0 | +0<br>260<br>-137 | —     |

#### Character Classes - POSIX - Short - Other Letter (`[\p{Lo}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-131612 | +0<br>0<br>-99104 | +0<br>0<br>-127004 | +0<br>0<br>-131612 | +0<br>0<br>-127333 | +0<br>0<br>-127004 | +0<br>0<br>-127333 | +0<br>0<br>-131612 | +0<br>0<br>-121414 | +0<br>0<br>-131612 | +0<br>0<br>-127004 |
| Go         | +131612<br>0<br>-0 | —       | +119852<br>11760<br>-87344 | +4608<br>127004<br>-0 | +0<br>131612<br>-0 | +4279<br>127333<br>-0 | +4608<br>127004<br>-0 | +4279<br>127333<br>-0 | +0<br>131612<br>-0 | +10198<br>121414<br>-0 | +0<br>131612<br>-0 | +4608<br>127004<br>-0 |
| Haskell    | +99104<br>0<br>-0 | +87344<br>11760<br>-119852 | —       | +87691<br>11413<br>-115591 | +87344<br>11760<br>-119852 | +87601<br>11503<br>-115830 | +87691<br>11413<br>-115591 | +87601<br>11503<br>-115830 | +87344<br>11760<br>-119852 | +88039<br>11065<br>-110349 | +87344<br>11760<br>-119852 | +87691<br>11413<br>-115591 |
| Java       | +127004<br>0<br>-0 | +0<br>127004<br>-4608 | +115591<br>11413<br>-87691 | —       | +0<br>127004<br>-4608 | +0<br>127004<br>-329 | +0<br>127004<br>-0 | +0<br>127004<br>-329 | +0<br>127004<br>-4608 | +5590<br>121414<br>-0 | +0<br>127004<br>-4608 | +0<br>127004<br>-0 |
| Javascript | +131612<br>0<br>-0 | +0<br>131612<br>-0 | +119852<br>11760<br>-87344 | +4608<br>127004<br>-0 | —          | +4279<br>127333<br>-0 | +4608<br>127004<br>-0 | +4279<br>127333<br>-0 | +0<br>131612<br>-0 | +10198<br>121414<br>-0 | +0<br>131612<br>-0 | +4608<br>127004<br>-0 |
| Obj-C      | +127333<br>0<br>-0 | +0<br>127333<br>-4279 | +115830<br>11503<br>-87601 | +329<br>127004<br>-0 | +0<br>127333<br>-4279 | —       | +329<br>127004<br>-0 | +0<br>127333<br>-0 | +0<br>127333<br>-4279 | +5919<br>121414<br>-0 | +0<br>127333<br>-4279 | +329<br>127004<br>-0 |
| Perl       | +127004<br>0<br>-0 | +0<br>127004<br>-4608 | +115591<br>11413<br>-87691 | +0<br>127004<br>-0 | +0<br>127004<br>-4608 | +0<br>127004<br>-329 | —       | +0<br>127004<br>-329 | +0<br>127004<br>-4608 | +5590<br>121414<br>-0 | +0<br>127004<br>-4608 | +0<br>127004<br>-0 |
| PHP        | +127333<br>0<br>-0 | +0<br>127333<br>-4279 | +115830<br>11503<br>-87601 | +329<br>127004<br>-0 | +0<br>127333<br>-4279 | +0<br>127333<br>-0 | +329<br>127004<br>-0 | —       | +0<br>127333<br>-4279 | +5919<br>121414<br>-0 | +0<br>127333<br>-4279 | +329<br>127004<br>-0 |
| Python     | +131612<br>0<br>-0 | +0<br>131612<br>-0 | +119852<br>11760<br>-87344 | +4608<br>127004<br>-0 | +0<br>131612<br>-0 | +4279<br>127333<br>-0 | +4608<br>127004<br>-0 | +4279<br>127333<br>-0 | —       | +10198<br>121414<br>-0 | +0<br>131612<br>-0 | +4608<br>127004<br>-0 |
| Ruby       | +121414<br>0<br>-0 | +0<br>121414<br>-10198 | +110349<br>11065<br>-88039 | +0<br>121414<br>-5590 | +0<br>121414<br>-10198 | +0<br>121414<br>-5919 | +0<br>121414<br>-5590 | +0<br>121414<br>-5919 | +0<br>121414<br>-10198 | —       | +0<br>121414<br>-10198 | +0<br>121414<br>-5590 |
| Rust       | +131612<br>0<br>-0 | +0<br>131612<br>-0 | +119852<br>11760<br>-87344 | +4608<br>127004<br>-0 | +0<br>131612<br>-0 | +4279<br>127333<br>-0 | +4608<br>127004<br>-0 | +4279<br>127333<br>-0 | +0<br>131612<br>-0 | +10198<br>121414<br>-0 | —       | +4608<br>127004<br>-0 |
| Scala      | +127004<br>0<br>-0 | +0<br>127004<br>-4608 | +115591<br>11413<br>-87691 | +0<br>127004<br>-0 | +0<br>127004<br>-4608 | +0<br>127004<br>-329 | +0<br>127004<br>-0 | +0<br>127004<br>-329 | +0<br>127004<br>-4608 | +5590<br>121414<br>-0 | +0<br>127004<br>-4608 | —       |

#### Character Classes - POSIX - Short - Letter (`[\p{L}]`)

| Language   | C++      | Go      | Haskell  | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | -------: | ------: | -------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —        | +0<br>0<br>-136104 | +0<br>0<br>-1113975 | +0<br>0<br>-131241 | +0<br>0<br>-136104 | +0<br>0<br>-131756 | +0<br>0<br>-131241 | +0<br>0<br>-131756 | +0<br>0<br>-136104 | +0<br>0<br>-125643 | +0<br>0<br>-136104 | +0<br>0<br>-131241 |
| Go         | +136104<br>0<br>-0 | —       | +30<br>136074<br>-977901 | +4863<br>131241<br>-0 | +0<br>136104<br>-0 | +4348<br>131756<br>-0 | +4863<br>131241<br>-0 | +4348<br>131756<br>-0 | +0<br>136104<br>-0 | +10461<br>125643<br>-0 | +0<br>136104<br>-0 | +4863<br>131241<br>-0 |
| Haskell    | +1113975<br>0<br>-0 | +977901<br>136074<br>-30 | —        | +982764<br>131211<br>-30 | +977901<br>136074<br>-30 | +982249<br>131726<br>-30 | +982764<br>131211<br>-30 | +982249<br>131726<br>-30 | +977901<br>136074<br>-30 | +988362<br>125613<br>-30 | +977901<br>136074<br>-30 | +982764<br>131211<br>-30 |
| Java       | +131241<br>0<br>-0 | +0<br>131241<br>-4863 | +30<br>131211<br>-982764 | —       | +0<br>131241<br>-4863 | +0<br>131241<br>-515 | +0<br>131241<br>-0 | +0<br>131241<br>-515 | +0<br>131241<br>-4863 | +5598<br>125643<br>-0 | +0<br>131241<br>-4863 | +0<br>131241<br>-0 |
| Javascript | +136104<br>0<br>-0 | +0<br>136104<br>-0 | +30<br>136074<br>-977901 | +4863<br>131241<br>-0 | —          | +4348<br>131756<br>-0 | +4863<br>131241<br>-0 | +4348<br>131756<br>-0 | +0<br>136104<br>-0 | +10461<br>125643<br>-0 | +0<br>136104<br>-0 | +4863<br>131241<br>-0 |
| Obj-C      | +131756<br>0<br>-0 | +0<br>131756<br>-4348 | +30<br>131726<br>-982249 | +515<br>131241<br>-0 | +0<br>131756<br>-4348 | —       | +515<br>131241<br>-0 | +0<br>131756<br>-0 | +0<br>131756<br>-4348 | +6113<br>125643<br>-0 | +0<br>131756<br>-4348 | +515<br>131241<br>-0 |
| Perl       | +131241<br>0<br>-0 | +0<br>131241<br>-4863 | +30<br>131211<br>-982764 | +0<br>131241<br>-0 | +0<br>131241<br>-4863 | +0<br>131241<br>-515 | —       | +0<br>131241<br>-515 | +0<br>131241<br>-4863 | +5598<br>125643<br>-0 | +0<br>131241<br>-4863 | +0<br>131241<br>-0 |
| PHP        | +131756<br>0<br>-0 | +0<br>131756<br>-4348 | +30<br>131726<br>-982249 | +515<br>131241<br>-0 | +0<br>131756<br>-4348 | +0<br>131756<br>-0 | +515<br>131241<br>-0 | —       | +0<br>131756<br>-4348 | +6113<br>125643<br>-0 | +0<br>131756<br>-4348 | +515<br>131241<br>-0 |
| Python     | +136104<br>0<br>-0 | +0<br>136104<br>-0 | +30<br>136074<br>-977901 | +4863<br>131241<br>-0 | +0<br>136104<br>-0 | +4348<br>131756<br>-0 | +4863<br>131241<br>-0 | +4348<br>131756<br>-0 | —       | +10461<br>125643<br>-0 | +0<br>136104<br>-0 | +4863<br>131241<br>-0 |
| Ruby       | +125643<br>0<br>-0 | +0<br>125643<br>-10461 | +30<br>125613<br>-988362 | +0<br>125643<br>-5598 | +0<br>125643<br>-10461 | +0<br>125643<br>-6113 | +0<br>125643<br>-5598 | +0<br>125643<br>-6113 | +0<br>125643<br>-10461 | —       | +0<br>125643<br>-10461 | +0<br>125643<br>-5598 |
| Rust       | +136104<br>0<br>-0 | +0<br>136104<br>-0 | +30<br>136074<br>-977901 | +4863<br>131241<br>-0 | +0<br>136104<br>-0 | +4348<br>131756<br>-0 | +4863<br>131241<br>-0 | +4348<br>131756<br>-0 | +0<br>136104<br>-0 | +10461<br>125643<br>-0 | —       | +4863<br>131241<br>-0 |
| Scala      | +131241<br>0<br>-0 | +0<br>131241<br>-4863 | +30<br>131211<br>-982764 | +0<br>131241<br>-0 | +0<br>131241<br>-4863 | +0<br>131241<br>-515 | +0<br>131241<br>-0 | +0<br>131241<br>-515 | +0<br>131241<br>-4863 | +5598<br>125643<br>-0 | +0<br>131241<br>-4863 | —       |

#### Character Classes - POSIX - Short - Nonspacing Mark (`[\p{Mn}]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>0<br>-1985 | +0<br>0<br>-0 | +0<br>0<br>-1839 | +0<br>0<br>-1985 | +0<br>0<br>-1950 | +0<br>0<br>-1839 | +0<br>0<br>-1950 | +0<br>0<br>-1985 | +0<br>0<br>-1826 | +0<br>0<br>-1985 | +0<br>0<br>-1839 |
| Go         | +1985<br>0<br>-0 | —     | +1985<br>0<br>-0 | +147<br>1838<br>-1 | +0<br>1985<br>-0 | +35<br>1950<br>-0 | +147<br>1838<br>-1 | +35<br>1950<br>-0 | +0<br>1985<br>-0 | +160<br>1825<br>-1 | +0<br>1985<br>-0 | +147<br>1838<br>-1 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-1985 | —       | +0<br>0<br>-1839 | +0<br>0<br>-1985 | +0<br>0<br>-1950 | +0<br>0<br>-1839 | +0<br>0<br>-1950 | +0<br>0<br>-1985 | +0<br>0<br>-1826 | +0<br>0<br>-1985 | +0<br>0<br>-1839 |
| Java       | +1839<br>0<br>-0 | +1<br>1838<br>-147 | +1839<br>0<br>-0 | —     | +1<br>1838<br>-147 | +1<br>1838<br>-112 | +0<br>1839<br>-0 | +1<br>1838<br>-112 | +1<br>1838<br>-147 | +13<br>1826<br>-0 | +1<br>1838<br>-147 | +0<br>1839<br>-0 |
| Javascript | +1985<br>0<br>-0 | +0<br>1985<br>-0 | +1985<br>0<br>-0 | +147<br>1838<br>-1 | —          | +35<br>1950<br>-0 | +147<br>1838<br>-1 | +35<br>1950<br>-0 | +0<br>1985<br>-0 | +160<br>1825<br>-1 | +0<br>1985<br>-0 | +147<br>1838<br>-1 |
| Obj-C      | +1950<br>0<br>-0 | +0<br>1950<br>-35 | +1950<br>0<br>-0 | +112<br>1838<br>-1 | +0<br>1950<br>-35 | —     | +112<br>1838<br>-1 | +0<br>1950<br>-0 | +0<br>1950<br>-35 | +125<br>1825<br>-1 | +0<br>1950<br>-35 | +112<br>1838<br>-1 |
| Perl       | +1839<br>0<br>-0 | +1<br>1838<br>-147 | +1839<br>0<br>-0 | +0<br>1839<br>-0 | +1<br>1838<br>-147 | +1<br>1838<br>-112 | —     | +1<br>1838<br>-112 | +1<br>1838<br>-147 | +13<br>1826<br>-0 | +1<br>1838<br>-147 | +0<br>1839<br>-0 |
| PHP        | +1950<br>0<br>-0 | +0<br>1950<br>-35 | +1950<br>0<br>-0 | +112<br>1838<br>-1 | +0<br>1950<br>-35 | +0<br>1950<br>-0 | +112<br>1838<br>-1 | —     | +0<br>1950<br>-35 | +125<br>1825<br>-1 | +0<br>1950<br>-35 | +112<br>1838<br>-1 |
| Python     | +1985<br>0<br>-0 | +0<br>1985<br>-0 | +1985<br>0<br>-0 | +147<br>1838<br>-1 | +0<br>1985<br>-0 | +35<br>1950<br>-0 | +147<br>1838<br>-1 | +35<br>1950<br>-0 | —      | +160<br>1825<br>-1 | +0<br>1985<br>-0 | +147<br>1838<br>-1 |
| Ruby       | +1826<br>0<br>-0 | +1<br>1825<br>-160 | +1826<br>0<br>-0 | +0<br>1826<br>-13 | +1<br>1825<br>-160 | +1<br>1825<br>-125 | +0<br>1826<br>-13 | +1<br>1825<br>-125 | +1<br>1825<br>-160 | —     | +1<br>1825<br>-160 | +0<br>1826<br>-13 |
| Rust       | +1985<br>0<br>-0 | +0<br>1985<br>-0 | +1985<br>0<br>-0 | +147<br>1838<br>-1 | +0<br>1985<br>-0 | +35<br>1950<br>-0 | +147<br>1838<br>-1 | +35<br>1950<br>-0 | +0<br>1985<br>-0 | +160<br>1825<br>-1 | —     | +147<br>1838<br>-1 |
| Scala      | +1839<br>0<br>-0 | +1<br>1838<br>-147 | +1839<br>0<br>-0 | +0<br>1839<br>-0 | +1<br>1838<br>-147 | +1<br>1838<br>-112 | +0<br>1839<br>-0 | +1<br>1838<br>-112 | +1<br>1838<br>-147 | +13<br>1826<br>-0 | +1<br>1838<br>-147 | —     |

#### Character Classes - POSIX - Short - Spacing Mark (`[\p{Mc}]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>0<br>-452 | +0<br>0<br>-0 | +0<br>0<br>-443 | +0<br>0<br>-452 | +0<br>0<br>-445 | +0<br>0<br>-443 | +0<br>0<br>-445 | +0<br>0<br>-452 | +0<br>0<br>-429 | +0<br>0<br>-452 | +0<br>0<br>-443 |
| Go         | +452<br>0<br>-0 | —    | +452<br>0<br>-0 | +9<br>443<br>-0 | +0<br>452<br>-0 | +7<br>445<br>-0 | +9<br>443<br>-0 | +7<br>445<br>-0 | +0<br>452<br>-0 | +23<br>429<br>-0 | +0<br>452<br>-0 | +9<br>443<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-452 | —       | +0<br>0<br>-443 | +0<br>0<br>-452 | +0<br>0<br>-445 | +0<br>0<br>-443 | +0<br>0<br>-445 | +0<br>0<br>-452 | +0<br>0<br>-429 | +0<br>0<br>-452 | +0<br>0<br>-443 |
| Java       | +443<br>0<br>-0 | +0<br>443<br>-9 | +443<br>0<br>-0 | —    | +0<br>443<br>-9 | +0<br>443<br>-2 | +0<br>443<br>-0 | +0<br>443<br>-2 | +0<br>443<br>-9 | +14<br>429<br>-0 | +0<br>443<br>-9 | +0<br>443<br>-0 |
| Javascript | +452<br>0<br>-0 | +0<br>452<br>-0 | +452<br>0<br>-0 | +9<br>443<br>-0 | —          | +7<br>445<br>-0 | +9<br>443<br>-0 | +7<br>445<br>-0 | +0<br>452<br>-0 | +23<br>429<br>-0 | +0<br>452<br>-0 | +9<br>443<br>-0 |
| Obj-C      | +445<br>0<br>-0 | +0<br>445<br>-7 | +445<br>0<br>-0 | +2<br>443<br>-0 | +0<br>445<br>-7 | —     | +2<br>443<br>-0 | +0<br>445<br>-0 | +0<br>445<br>-7 | +16<br>429<br>-0 | +0<br>445<br>-7 | +2<br>443<br>-0 |
| Perl       | +443<br>0<br>-0 | +0<br>443<br>-9 | +443<br>0<br>-0 | +0<br>443<br>-0 | +0<br>443<br>-9 | +0<br>443<br>-2 | —    | +0<br>443<br>-2 | +0<br>443<br>-9 | +14<br>429<br>-0 | +0<br>443<br>-9 | +0<br>443<br>-0 |
| PHP        | +445<br>0<br>-0 | +0<br>445<br>-7 | +445<br>0<br>-0 | +2<br>443<br>-0 | +0<br>445<br>-7 | +0<br>445<br>-0 | +2<br>443<br>-0 | —    | +0<br>445<br>-7 | +16<br>429<br>-0 | +0<br>445<br>-7 | +2<br>443<br>-0 |
| Python     | +452<br>0<br>-0 | +0<br>452<br>-0 | +452<br>0<br>-0 | +9<br>443<br>-0 | +0<br>452<br>-0 | +7<br>445<br>-0 | +9<br>443<br>-0 | +7<br>445<br>-0 | —      | +23<br>429<br>-0 | +0<br>452<br>-0 | +9<br>443<br>-0 |
| Ruby       | +429<br>0<br>-0 | +0<br>429<br>-23 | +429<br>0<br>-0 | +0<br>429<br>-14 | +0<br>429<br>-23 | +0<br>429<br>-16 | +0<br>429<br>-14 | +0<br>429<br>-16 | +0<br>429<br>-23 | —    | +0<br>429<br>-23 | +0<br>429<br>-14 |
| Rust       | +452<br>0<br>-0 | +0<br>452<br>-0 | +452<br>0<br>-0 | +9<br>443<br>-0 | +0<br>452<br>-0 | +7<br>445<br>-0 | +9<br>443<br>-0 | +7<br>445<br>-0 | +0<br>452<br>-0 | +23<br>429<br>-0 | —    | +9<br>443<br>-0 |
| Scala      | +443<br>0<br>-0 | +0<br>443<br>-9 | +443<br>0<br>-0 | +0<br>443<br>-0 | +0<br>443<br>-9 | +0<br>443<br>-2 | +0<br>443<br>-0 | +0<br>443<br>-2 | +0<br>443<br>-9 | +14<br>429<br>-0 | +0<br>443<br>-9 | —     |

#### Character Classes - POSIX - Short - Enclosing Mark (`[\p{Me}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-13 | +0<br>0<br>-0 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 |
| Go         | +13<br>0<br>-0 | —   | +13<br>0<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-13 | —       | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 | +0<br>0<br>-13 |
| Java       | +13<br>0<br>-0 | +0<br>13<br>-0 | +13<br>0<br>-0 | —    | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 |
| Javascript | +13<br>0<br>-0 | +0<br>13<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | —          | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 |
| Obj-C      | +13<br>0<br>-0 | +0<br>13<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | —     | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 |
| Perl       | +13<br>0<br>-0 | +0<br>13<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | —    | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 |
| PHP        | +13<br>0<br>-0 | +0<br>13<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | —   | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 |
| Python     | +13<br>0<br>-0 | +0<br>13<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | —      | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 |
| Ruby       | +13<br>0<br>-0 | +0<br>13<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | —    | +0<br>13<br>-0 | +0<br>13<br>-0 |
| Rust       | +13<br>0<br>-0 | +0<br>13<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | —    | +0<br>13<br>-0 |
| Scala      | +13<br>0<br>-0 | +0<br>13<br>-0 | +13<br>0<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | +0<br>13<br>-0 | —     |

#### Character Classes - POSIX - Short - Mark (`[\p{M}]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>0<br>-2450 | +0<br>0<br>-0 | +0<br>0<br>-2295 | +0<br>0<br>-2450 | +0<br>0<br>-2408 | +0<br>0<br>-2295 | +0<br>0<br>-2408 | +0<br>0<br>-2450 | +0<br>0<br>-2268 | +0<br>0<br>-2450 | +0<br>0<br>-2295 |
| Go         | +2450<br>0<br>-0 | —     | +2450<br>0<br>-0 | +155<br>2295<br>-0 | +0<br>2450<br>-0 | +42<br>2408<br>-0 | +155<br>2295<br>-0 | +42<br>2408<br>-0 | +0<br>2450<br>-0 | +182<br>2268<br>-0 | +0<br>2450<br>-0 | +155<br>2295<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-2450 | —       | +0<br>0<br>-2295 | +0<br>0<br>-2450 | +0<br>0<br>-2408 | +0<br>0<br>-2295 | +0<br>0<br>-2408 | +0<br>0<br>-2450 | +0<br>0<br>-2268 | +0<br>0<br>-2450 | +0<br>0<br>-2295 |
| Java       | +2295<br>0<br>-0 | +0<br>2295<br>-155 | +2295<br>0<br>-0 | —     | +0<br>2295<br>-155 | +0<br>2295<br>-113 | +0<br>2295<br>-0 | +0<br>2295<br>-113 | +0<br>2295<br>-155 | +27<br>2268<br>-0 | +0<br>2295<br>-155 | +0<br>2295<br>-0 |
| Javascript | +2450<br>0<br>-0 | +0<br>2450<br>-0 | +2450<br>0<br>-0 | +155<br>2295<br>-0 | —          | +42<br>2408<br>-0 | +155<br>2295<br>-0 | +42<br>2408<br>-0 | +0<br>2450<br>-0 | +182<br>2268<br>-0 | +0<br>2450<br>-0 | +155<br>2295<br>-0 |
| Obj-C      | +2408<br>0<br>-0 | +0<br>2408<br>-42 | +2408<br>0<br>-0 | +113<br>2295<br>-0 | +0<br>2408<br>-42 | —     | +113<br>2295<br>-0 | +0<br>2408<br>-0 | +0<br>2408<br>-42 | +140<br>2268<br>-0 | +0<br>2408<br>-42 | +113<br>2295<br>-0 |
| Perl       | +2295<br>0<br>-0 | +0<br>2295<br>-155 | +2295<br>0<br>-0 | +0<br>2295<br>-0 | +0<br>2295<br>-155 | +0<br>2295<br>-113 | —     | +0<br>2295<br>-113 | +0<br>2295<br>-155 | +27<br>2268<br>-0 | +0<br>2295<br>-155 | +0<br>2295<br>-0 |
| PHP        | +2408<br>0<br>-0 | +0<br>2408<br>-42 | +2408<br>0<br>-0 | +113<br>2295<br>-0 | +0<br>2408<br>-42 | +0<br>2408<br>-0 | +113<br>2295<br>-0 | —     | +0<br>2408<br>-42 | +140<br>2268<br>-0 | +0<br>2408<br>-42 | +113<br>2295<br>-0 |
| Python     | +2450<br>0<br>-0 | +0<br>2450<br>-0 | +2450<br>0<br>-0 | +155<br>2295<br>-0 | +0<br>2450<br>-0 | +42<br>2408<br>-0 | +155<br>2295<br>-0 | +42<br>2408<br>-0 | —      | +182<br>2268<br>-0 | +0<br>2450<br>-0 | +155<br>2295<br>-0 |
| Ruby       | +2268<br>0<br>-0 | +0<br>2268<br>-182 | +2268<br>0<br>-0 | +0<br>2268<br>-27 | +0<br>2268<br>-182 | +0<br>2268<br>-140 | +0<br>2268<br>-27 | +0<br>2268<br>-140 | +0<br>2268<br>-182 | —     | +0<br>2268<br>-182 | +0<br>2268<br>-27 |
| Rust       | +2450<br>0<br>-0 | +0<br>2450<br>-0 | +2450<br>0<br>-0 | +155<br>2295<br>-0 | +0<br>2450<br>-0 | +42<br>2408<br>-0 | +155<br>2295<br>-0 | +42<br>2408<br>-0 | +0<br>2450<br>-0 | +182<br>2268<br>-0 | —     | +155<br>2295<br>-0 |
| Scala      | +2295<br>0<br>-0 | +0<br>2295<br>-155 | +2295<br>0<br>-0 | +0<br>2295<br>-0 | +0<br>2295<br>-155 | +0<br>2295<br>-113 | +0<br>2295<br>-0 | +0<br>2295<br>-113 | +0<br>2295<br>-155 | +27<br>2268<br>-0 | +0<br>2295<br>-155 | —     |

#### Character Classes - POSIX - Short - Decimal Number (`[\p{Nd}]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>0<br>-680 | +0<br>0<br>-10 | +0<br>0<br>-650 | +0<br>0<br>-680 | +0<br>0<br>-660 | +0<br>0<br>-650 | +0<br>0<br>-660 | +0<br>0<br>-680 | +0<br>0<br>-630 | +0<br>0<br>-680 | +0<br>0<br>-650 |
| Go         | +680<br>0<br>-0 | —    | +670<br>10<br>-0 | +30<br>650<br>-0 | +0<br>680<br>-0 | +20<br>660<br>-0 | +30<br>650<br>-0 | +20<br>660<br>-0 | +0<br>680<br>-0 | +50<br>630<br>-0 | +0<br>680<br>-0 | +30<br>650<br>-0 |
| Haskell    | +10<br>0<br>-0 | +0<br>10<br>-670 | —       | +0<br>10<br>-640 | +0<br>10<br>-670 | +0<br>10<br>-650 | +0<br>10<br>-640 | +0<br>10<br>-650 | +0<br>10<br>-670 | +0<br>10<br>-620 | +0<br>10<br>-670 | +0<br>10<br>-640 |
| Java       | +650<br>0<br>-0 | +0<br>650<br>-30 | +640<br>10<br>-0 | —    | +0<br>650<br>-30 | +0<br>650<br>-10 | +0<br>650<br>-0 | +0<br>650<br>-10 | +0<br>650<br>-30 | +20<br>630<br>-0 | +0<br>650<br>-30 | +0<br>650<br>-0 |
| Javascript | +680<br>0<br>-0 | +0<br>680<br>-0 | +670<br>10<br>-0 | +30<br>650<br>-0 | —          | +20<br>660<br>-0 | +30<br>650<br>-0 | +20<br>660<br>-0 | +0<br>680<br>-0 | +50<br>630<br>-0 | +0<br>680<br>-0 | +30<br>650<br>-0 |
| Obj-C      | +660<br>0<br>-0 | +0<br>660<br>-20 | +650<br>10<br>-0 | +10<br>650<br>-0 | +0<br>660<br>-20 | —     | +10<br>650<br>-0 | +0<br>660<br>-0 | +0<br>660<br>-20 | +30<br>630<br>-0 | +0<br>660<br>-20 | +10<br>650<br>-0 |
| Perl       | +650<br>0<br>-0 | +0<br>650<br>-30 | +640<br>10<br>-0 | +0<br>650<br>-0 | +0<br>650<br>-30 | +0<br>650<br>-10 | —    | +0<br>650<br>-10 | +0<br>650<br>-30 | +20<br>630<br>-0 | +0<br>650<br>-30 | +0<br>650<br>-0 |
| PHP        | +660<br>0<br>-0 | +0<br>660<br>-20 | +650<br>10<br>-0 | +10<br>650<br>-0 | +0<br>660<br>-20 | +0<br>660<br>-0 | +10<br>650<br>-0 | —    | +0<br>660<br>-20 | +30<br>630<br>-0 | +0<br>660<br>-20 | +10<br>650<br>-0 |
| Python     | +680<br>0<br>-0 | +0<br>680<br>-0 | +670<br>10<br>-0 | +30<br>650<br>-0 | +0<br>680<br>-0 | +20<br>660<br>-0 | +30<br>650<br>-0 | +20<br>660<br>-0 | —      | +50<br>630<br>-0 | +0<br>680<br>-0 | +30<br>650<br>-0 |
| Ruby       | +630<br>0<br>-0 | +0<br>630<br>-50 | +620<br>10<br>-0 | +0<br>630<br>-20 | +0<br>630<br>-50 | +0<br>630<br>-30 | +0<br>630<br>-20 | +0<br>630<br>-30 | +0<br>630<br>-50 | —    | +0<br>630<br>-50 | +0<br>630<br>-20 |
| Rust       | +680<br>0<br>-0 | +0<br>680<br>-0 | +670<br>10<br>-0 | +30<br>650<br>-0 | +0<br>680<br>-0 | +20<br>660<br>-0 | +30<br>650<br>-0 | +20<br>660<br>-0 | +0<br>680<br>-0 | +50<br>630<br>-0 | —    | +30<br>650<br>-0 |
| Scala      | +650<br>0<br>-0 | +0<br>650<br>-30 | +640<br>10<br>-0 | +0<br>650<br>-0 | +0<br>650<br>-30 | +0<br>650<br>-10 | +0<br>650<br>-0 | +0<br>650<br>-10 | +0<br>650<br>-30 | +20<br>630<br>-0 | +0<br>650<br>-30 | —     |

#### Character Classes - POSIX - Short - Letter Number (`[\p{Nl}]`)

| Language   | C++  | Go   | Haskell | Java | Javascript | Obj-C | Perl | PHP  | Python | Ruby | Rust | Scala |
| :--------- | ---: | ---: | ------: | ---: | ---------: | ----: | ---: | ---: | -----: | ---: | ---: | ----: |
| C++        | —    | +0<br>0<br>-236 | +0<br>0<br>-0 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 |
| Go         | +236<br>0<br>-0 | —    | +236<br>0<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-236 | —       | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 | +0<br>0<br>-236 |
| Java       | +236<br>0<br>-0 | +0<br>236<br>-0 | +236<br>0<br>-0 | —    | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 |
| Javascript | +236<br>0<br>-0 | +0<br>236<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | —          | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 |
| Obj-C      | +236<br>0<br>-0 | +0<br>236<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | —     | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 |
| Perl       | +236<br>0<br>-0 | +0<br>236<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | —    | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 |
| PHP        | +236<br>0<br>-0 | +0<br>236<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | —    | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 |
| Python     | +236<br>0<br>-0 | +0<br>236<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | —      | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 |
| Ruby       | +236<br>0<br>-0 | +0<br>236<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | —    | +0<br>236<br>-0 | +0<br>236<br>-0 |
| Rust       | +236<br>0<br>-0 | +0<br>236<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | —    | +0<br>236<br>-0 |
| Scala      | +236<br>0<br>-0 | +0<br>236<br>-0 | +236<br>0<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | +0<br>236<br>-0 | —     |

#### Character Classes - POSIX - Short - Other Number (`[\p{No}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-915 | +0<br>0<br>-281336 | +0<br>0<br>-895 | +0<br>0<br>-915 | +0<br>0<br>-895 | +0<br>0<br>-895 | +0<br>0<br>-895 | +0<br>0<br>-915 | +0<br>0<br>-888 | +0<br>0<br>-915 | +0<br>0<br>-895 |
| Go         | +915<br>0<br>-0 | —       | +710<br>205<br>-281131 | +20<br>895<br>-0 | +0<br>915<br>-0 | +20<br>895<br>-0 | +20<br>895<br>-0 | +20<br>895<br>-0 | +0<br>915<br>-0 | +27<br>888<br>-0 | +0<br>915<br>-0 | +20<br>895<br>-0 |
| Haskell    | +281336<br>0<br>-0 | +281131<br>205<br>-710 | —       | +281131<br>205<br>-690 | +281131<br>205<br>-710 | +281131<br>205<br>-690 | +281131<br>205<br>-690 | +281131<br>205<br>-690 | +281131<br>205<br>-710 | +281131<br>205<br>-683 | +281131<br>205<br>-710 | +281131<br>205<br>-690 |
| Java       | +895<br>0<br>-0 | +0<br>895<br>-20 | +690<br>205<br>-281131 | —       | +0<br>895<br>-20 | +0<br>895<br>-0 | +0<br>895<br>-0 | +0<br>895<br>-0 | +0<br>895<br>-20 | +7<br>888<br>-0 | +0<br>895<br>-20 | +0<br>895<br>-0 |
| Javascript | +915<br>0<br>-0 | +0<br>915<br>-0 | +710<br>205<br>-281131 | +20<br>895<br>-0 | —          | +20<br>895<br>-0 | +20<br>895<br>-0 | +20<br>895<br>-0 | +0<br>915<br>-0 | +27<br>888<br>-0 | +0<br>915<br>-0 | +20<br>895<br>-0 |
| Obj-C      | +895<br>0<br>-0 | +0<br>895<br>-20 | +690<br>205<br>-281131 | +0<br>895<br>-0 | +0<br>895<br>-20 | —       | +0<br>895<br>-0 | +0<br>895<br>-0 | +0<br>895<br>-20 | +7<br>888<br>-0 | +0<br>895<br>-20 | +0<br>895<br>-0 |
| Perl       | +895<br>0<br>-0 | +0<br>895<br>-20 | +690<br>205<br>-281131 | +0<br>895<br>-0 | +0<br>895<br>-20 | +0<br>895<br>-0 | —       | +0<br>895<br>-0 | +0<br>895<br>-20 | +7<br>888<br>-0 | +0<br>895<br>-20 | +0<br>895<br>-0 |
| PHP        | +895<br>0<br>-0 | +0<br>895<br>-20 | +690<br>205<br>-281131 | +0<br>895<br>-0 | +0<br>895<br>-20 | +0<br>895<br>-0 | +0<br>895<br>-0 | —       | +0<br>895<br>-20 | +7<br>888<br>-0 | +0<br>895<br>-20 | +0<br>895<br>-0 |
| Python     | +915<br>0<br>-0 | +0<br>915<br>-0 | +710<br>205<br>-281131 | +20<br>895<br>-0 | +0<br>915<br>-0 | +20<br>895<br>-0 | +20<br>895<br>-0 | +20<br>895<br>-0 | —       | +27<br>888<br>-0 | +0<br>915<br>-0 | +20<br>895<br>-0 |
| Ruby       | +888<br>0<br>-0 | +0<br>888<br>-27 | +683<br>205<br>-281131 | +0<br>888<br>-7 | +0<br>888<br>-27 | +0<br>888<br>-7 | +0<br>888<br>-7 | +0<br>888<br>-7 | +0<br>888<br>-27 | —       | +0<br>888<br>-27 | +0<br>888<br>-7 |
| Rust       | +915<br>0<br>-0 | +0<br>915<br>-0 | +710<br>205<br>-281131 | +20<br>895<br>-0 | +0<br>915<br>-0 | +20<br>895<br>-0 | +20<br>895<br>-0 | +20<br>895<br>-0 | +0<br>915<br>-0 | +27<br>888<br>-0 | —       | +20<br>895<br>-0 |
| Scala      | +895<br>0<br>-0 | +0<br>895<br>-20 | +690<br>205<br>-281131 | +0<br>895<br>-0 | +0<br>895<br>-20 | +0<br>895<br>-0 | +0<br>895<br>-0 | +0<br>895<br>-0 | +0<br>895<br>-20 | +7<br>888<br>-0 | +0<br>895<br>-20 | —       |

#### Character Classes - POSIX - Short - Number (`[\p{N}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-1831 | +0<br>0<br>-281346 | +0<br>0<br>-1781 | +0<br>0<br>-1831 | +0<br>0<br>-1791 | +0<br>0<br>-1781 | +0<br>0<br>-1791 | +0<br>0<br>-1831 | +0<br>0<br>-1754 | +0<br>0<br>-1831 | +0<br>0<br>-1781 |
| Go         | +1831<br>0<br>-0 | —       | +1508<br>323<br>-281023 | +50<br>1781<br>-0 | +0<br>1831<br>-0 | +40<br>1791<br>-0 | +50<br>1781<br>-0 | +40<br>1791<br>-0 | +0<br>1831<br>-0 | +77<br>1754<br>-0 | +0<br>1831<br>-0 | +50<br>1781<br>-0 |
| Haskell    | +281346<br>0<br>-0 | +281023<br>323<br>-1508 | —       | +281036<br>310<br>-1471 | +281023<br>323<br>-1508 | +281036<br>310<br>-1481 | +281036<br>310<br>-1471 | +281036<br>310<br>-1481 | +281023<br>323<br>-1508 | +281039<br>307<br>-1447 | +281023<br>323<br>-1508 | +281036<br>310<br>-1471 |
| Java       | +1781<br>0<br>-0 | +0<br>1781<br>-50 | +1471<br>310<br>-281036 | —       | +0<br>1781<br>-50 | +0<br>1781<br>-10 | +0<br>1781<br>-0 | +0<br>1781<br>-10 | +0<br>1781<br>-50 | +27<br>1754<br>-0 | +0<br>1781<br>-50 | +0<br>1781<br>-0 |
| Javascript | +1831<br>0<br>-0 | +0<br>1831<br>-0 | +1508<br>323<br>-281023 | +50<br>1781<br>-0 | —          | +40<br>1791<br>-0 | +50<br>1781<br>-0 | +40<br>1791<br>-0 | +0<br>1831<br>-0 | +77<br>1754<br>-0 | +0<br>1831<br>-0 | +50<br>1781<br>-0 |
| Obj-C      | +1791<br>0<br>-0 | +0<br>1791<br>-40 | +1481<br>310<br>-281036 | +10<br>1781<br>-0 | +0<br>1791<br>-40 | —       | +10<br>1781<br>-0 | +0<br>1791<br>-0 | +0<br>1791<br>-40 | +37<br>1754<br>-0 | +0<br>1791<br>-40 | +10<br>1781<br>-0 |
| Perl       | +1781<br>0<br>-0 | +0<br>1781<br>-50 | +1471<br>310<br>-281036 | +0<br>1781<br>-0 | +0<br>1781<br>-50 | +0<br>1781<br>-10 | —       | +0<br>1781<br>-10 | +0<br>1781<br>-50 | +27<br>1754<br>-0 | +0<br>1781<br>-50 | +0<br>1781<br>-0 |
| PHP        | +1791<br>0<br>-0 | +0<br>1791<br>-40 | +1481<br>310<br>-281036 | +10<br>1781<br>-0 | +0<br>1791<br>-40 | +0<br>1791<br>-0 | +10<br>1781<br>-0 | —       | +0<br>1791<br>-40 | +37<br>1754<br>-0 | +0<br>1791<br>-40 | +10<br>1781<br>-0 |
| Python     | +1831<br>0<br>-0 | +0<br>1831<br>-0 | +1508<br>323<br>-281023 | +50<br>1781<br>-0 | +0<br>1831<br>-0 | +40<br>1791<br>-0 | +50<br>1781<br>-0 | +40<br>1791<br>-0 | —       | +77<br>1754<br>-0 | +0<br>1831<br>-0 | +50<br>1781<br>-0 |
| Ruby       | +1754<br>0<br>-0 | +0<br>1754<br>-77 | +1447<br>307<br>-281039 | +0<br>1754<br>-27 | +0<br>1754<br>-77 | +0<br>1754<br>-37 | +0<br>1754<br>-27 | +0<br>1754<br>-37 | +0<br>1754<br>-77 | —       | +0<br>1754<br>-77 | +0<br>1754<br>-27 |
| Rust       | +1831<br>0<br>-0 | +0<br>1831<br>-0 | +1508<br>323<br>-281023 | +50<br>1781<br>-0 | +0<br>1831<br>-0 | +40<br>1791<br>-0 | +50<br>1781<br>-0 | +40<br>1791<br>-0 | +0<br>1831<br>-0 | +77<br>1754<br>-0 | —       | +50<br>1781<br>-0 |
| Scala      | +1781<br>0<br>-0 | +0<br>1781<br>-50 | +1471<br>310<br>-281036 | +0<br>1781<br>-0 | +0<br>1781<br>-50 | +0<br>1781<br>-10 | +0<br>1781<br>-0 | +0<br>1781<br>-10 | +0<br>1781<br>-50 | +27<br>1754<br>-0 | +0<br>1781<br>-50 | —       |

#### Character Classes - POSIX - Short - Connector Punctuation (`[\p{Pc}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-10 | +0<br>0<br>-1 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 |
| Go         | +10<br>0<br>-0 | —   | +9<br>1<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 |
| Haskell    | +1<br>0<br>-0 | +0<br>1<br>-9 | —       | +0<br>1<br>-9 | +0<br>1<br>-9 | +0<br>1<br>-9 | +0<br>1<br>-9 | +0<br>1<br>-9 | +0<br>1<br>-9 | +0<br>1<br>-9 | +0<br>1<br>-9 | +0<br>1<br>-9 |
| Java       | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-0 | —    | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 |
| Javascript | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-0 | +0<br>10<br>-0 | —          | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 |
| Obj-C      | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —     | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 |
| Perl       | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —    | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 |
| PHP        | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —   | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 |
| Python     | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —      | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 |
| Ruby       | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —    | +0<br>10<br>-0 | +0<br>10<br>-0 |
| Rust       | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —    | +0<br>10<br>-0 |
| Scala      | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —     |

#### Character Classes - POSIX - Short - Dash Punctuation (`[\p{Pd}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-26 | +0<br>0<br>-1 | +0<br>0<br>-25 | +0<br>0<br>-26 | +0<br>0<br>-26 | +0<br>0<br>-25 | +0<br>0<br>-26 | +0<br>0<br>-26 | +0<br>0<br>-24 | +0<br>0<br>-26 | +0<br>0<br>-25 |
| Go         | +26<br>0<br>-0 | —   | +25<br>1<br>-0 | +1<br>25<br>-0 | +0<br>26<br>-0 | +0<br>26<br>-0 | +1<br>25<br>-0 | +0<br>26<br>-0 | +0<br>26<br>-0 | +2<br>24<br>-0 | +0<br>26<br>-0 | +1<br>25<br>-0 |
| Haskell    | +1<br>0<br>-0 | +0<br>1<br>-25 | —       | +0<br>1<br>-24 | +0<br>1<br>-25 | +0<br>1<br>-25 | +0<br>1<br>-24 | +0<br>1<br>-25 | +0<br>1<br>-25 | +0<br>1<br>-23 | +0<br>1<br>-25 | +0<br>1<br>-24 |
| Java       | +25<br>0<br>-0 | +0<br>25<br>-1 | +24<br>1<br>-0 | —    | +0<br>25<br>-1 | +0<br>25<br>-1 | +0<br>25<br>-0 | +0<br>25<br>-1 | +0<br>25<br>-1 | +1<br>24<br>-0 | +0<br>25<br>-1 | +0<br>25<br>-0 |
| Javascript | +26<br>0<br>-0 | +0<br>26<br>-0 | +25<br>1<br>-0 | +1<br>25<br>-0 | —          | +0<br>26<br>-0 | +1<br>25<br>-0 | +0<br>26<br>-0 | +0<br>26<br>-0 | +2<br>24<br>-0 | +0<br>26<br>-0 | +1<br>25<br>-0 |
| Obj-C      | +26<br>0<br>-0 | +0<br>26<br>-0 | +25<br>1<br>-0 | +1<br>25<br>-0 | +0<br>26<br>-0 | —     | +1<br>25<br>-0 | +0<br>26<br>-0 | +0<br>26<br>-0 | +2<br>24<br>-0 | +0<br>26<br>-0 | +1<br>25<br>-0 |
| Perl       | +25<br>0<br>-0 | +0<br>25<br>-1 | +24<br>1<br>-0 | +0<br>25<br>-0 | +0<br>25<br>-1 | +0<br>25<br>-1 | —    | +0<br>25<br>-1 | +0<br>25<br>-1 | +1<br>24<br>-0 | +0<br>25<br>-1 | +0<br>25<br>-0 |
| PHP        | +26<br>0<br>-0 | +0<br>26<br>-0 | +25<br>1<br>-0 | +1<br>25<br>-0 | +0<br>26<br>-0 | +0<br>26<br>-0 | +1<br>25<br>-0 | —   | +0<br>26<br>-0 | +2<br>24<br>-0 | +0<br>26<br>-0 | +1<br>25<br>-0 |
| Python     | +26<br>0<br>-0 | +0<br>26<br>-0 | +25<br>1<br>-0 | +1<br>25<br>-0 | +0<br>26<br>-0 | +0<br>26<br>-0 | +1<br>25<br>-0 | +0<br>26<br>-0 | —      | +2<br>24<br>-0 | +0<br>26<br>-0 | +1<br>25<br>-0 |
| Ruby       | +24<br>0<br>-0 | +0<br>24<br>-2 | +23<br>1<br>-0 | +0<br>24<br>-1 | +0<br>24<br>-2 | +0<br>24<br>-2 | +0<br>24<br>-1 | +0<br>24<br>-2 | +0<br>24<br>-2 | —    | +0<br>24<br>-2 | +0<br>24<br>-1 |
| Rust       | +26<br>0<br>-0 | +0<br>26<br>-0 | +25<br>1<br>-0 | +1<br>25<br>-0 | +0<br>26<br>-0 | +0<br>26<br>-0 | +1<br>25<br>-0 | +0<br>26<br>-0 | +0<br>26<br>-0 | +2<br>24<br>-0 | —    | +1<br>25<br>-0 |
| Scala      | +25<br>0<br>-0 | +0<br>25<br>-1 | +24<br>1<br>-0 | +0<br>25<br>-0 | +0<br>25<br>-1 | +0<br>25<br>-1 | +0<br>25<br>-0 | +0<br>25<br>-1 | +0<br>25<br>-1 | +1<br>24<br>-0 | +0<br>25<br>-1 | —     |

#### Character Classes - POSIX - Short - Open Punctuation (`[\p{Ps}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-79 | +0<br>0<br>-3 | +0<br>0<br>-75 | +0<br>0<br>-79 | +0<br>0<br>-79 | +0<br>0<br>-75 | +0<br>0<br>-79 | +0<br>0<br>-79 | +0<br>0<br>-75 | +0<br>0<br>-79 | +0<br>0<br>-75 |
| Go         | +79<br>0<br>-0 | —   | +76<br>3<br>-0 | +4<br>75<br>-0 | +0<br>79<br>-0 | +0<br>79<br>-0 | +4<br>75<br>-0 | +0<br>79<br>-0 | +0<br>79<br>-0 | +4<br>75<br>-0 | +0<br>79<br>-0 | +4<br>75<br>-0 |
| Haskell    | +3<br>0<br>-0 | +0<br>3<br>-76 | —       | +0<br>3<br>-72 | +0<br>3<br>-76 | +0<br>3<br>-76 | +0<br>3<br>-72 | +0<br>3<br>-76 | +0<br>3<br>-76 | +0<br>3<br>-72 | +0<br>3<br>-76 | +0<br>3<br>-72 |
| Java       | +75<br>0<br>-0 | +0<br>75<br>-4 | +72<br>3<br>-0 | —    | +0<br>75<br>-4 | +0<br>75<br>-4 | +0<br>75<br>-0 | +0<br>75<br>-4 | +0<br>75<br>-4 | +0<br>75<br>-0 | +0<br>75<br>-4 | +0<br>75<br>-0 |
| Javascript | +79<br>0<br>-0 | +0<br>79<br>-0 | +76<br>3<br>-0 | +4<br>75<br>-0 | —          | +0<br>79<br>-0 | +4<br>75<br>-0 | +0<br>79<br>-0 | +0<br>79<br>-0 | +4<br>75<br>-0 | +0<br>79<br>-0 | +4<br>75<br>-0 |
| Obj-C      | +79<br>0<br>-0 | +0<br>79<br>-0 | +76<br>3<br>-0 | +4<br>75<br>-0 | +0<br>79<br>-0 | —     | +4<br>75<br>-0 | +0<br>79<br>-0 | +0<br>79<br>-0 | +4<br>75<br>-0 | +0<br>79<br>-0 | +4<br>75<br>-0 |
| Perl       | +75<br>0<br>-0 | +0<br>75<br>-4 | +72<br>3<br>-0 | +0<br>75<br>-0 | +0<br>75<br>-4 | +0<br>75<br>-4 | —    | +0<br>75<br>-4 | +0<br>75<br>-4 | +0<br>75<br>-0 | +0<br>75<br>-4 | +0<br>75<br>-0 |
| PHP        | +79<br>0<br>-0 | +0<br>79<br>-0 | +76<br>3<br>-0 | +4<br>75<br>-0 | +0<br>79<br>-0 | +0<br>79<br>-0 | +4<br>75<br>-0 | —   | +0<br>79<br>-0 | +4<br>75<br>-0 | +0<br>79<br>-0 | +4<br>75<br>-0 |
| Python     | +79<br>0<br>-0 | +0<br>79<br>-0 | +76<br>3<br>-0 | +4<br>75<br>-0 | +0<br>79<br>-0 | +0<br>79<br>-0 | +4<br>75<br>-0 | +0<br>79<br>-0 | —      | +4<br>75<br>-0 | +0<br>79<br>-0 | +4<br>75<br>-0 |
| Ruby       | +75<br>0<br>-0 | +0<br>75<br>-4 | +72<br>3<br>-0 | +0<br>75<br>-0 | +0<br>75<br>-4 | +0<br>75<br>-4 | +0<br>75<br>-0 | +0<br>75<br>-4 | +0<br>75<br>-4 | —    | +0<br>75<br>-4 | +0<br>75<br>-0 |
| Rust       | +79<br>0<br>-0 | +0<br>79<br>-0 | +76<br>3<br>-0 | +4<br>75<br>-0 | +0<br>79<br>-0 | +0<br>79<br>-0 | +4<br>75<br>-0 | +0<br>79<br>-0 | +0<br>79<br>-0 | +4<br>75<br>-0 | —    | +4<br>75<br>-0 |
| Scala      | +75<br>0<br>-0 | +0<br>75<br>-4 | +72<br>3<br>-0 | +0<br>75<br>-0 | +0<br>75<br>-4 | +0<br>75<br>-4 | +0<br>75<br>-0 | +0<br>75<br>-4 | +0<br>75<br>-4 | +0<br>75<br>-0 | +0<br>75<br>-4 | —     |

#### Character Classes - POSIX - Short - Close Punctuation (`[\p{Pe}]`)

| Language   | C++ | Go  | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | --: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-77 | +0<br>0<br>-3 | +0<br>0<br>-73 | +0<br>0<br>-77 | +0<br>0<br>-77 | +0<br>0<br>-73 | +0<br>0<br>-77 | +0<br>0<br>-77 | +0<br>0<br>-73 | +0<br>0<br>-77 | +0<br>0<br>-73 |
| Go         | +77<br>0<br>-0 | —   | +74<br>3<br>-0 | +4<br>73<br>-0 | +0<br>77<br>-0 | +0<br>77<br>-0 | +4<br>73<br>-0 | +0<br>77<br>-0 | +0<br>77<br>-0 | +4<br>73<br>-0 | +0<br>77<br>-0 | +4<br>73<br>-0 |
| Haskell    | +3<br>0<br>-0 | +0<br>3<br>-74 | —       | +0<br>3<br>-70 | +0<br>3<br>-74 | +0<br>3<br>-74 | +0<br>3<br>-70 | +0<br>3<br>-74 | +0<br>3<br>-74 | +0<br>3<br>-70 | +0<br>3<br>-74 | +0<br>3<br>-70 |
| Java       | +73<br>0<br>-0 | +0<br>73<br>-4 | +70<br>3<br>-0 | —    | +0<br>73<br>-4 | +0<br>73<br>-4 | +0<br>73<br>-0 | +0<br>73<br>-4 | +0<br>73<br>-4 | +0<br>73<br>-0 | +0<br>73<br>-4 | +0<br>73<br>-0 |
| Javascript | +77<br>0<br>-0 | +0<br>77<br>-0 | +74<br>3<br>-0 | +4<br>73<br>-0 | —          | +0<br>77<br>-0 | +4<br>73<br>-0 | +0<br>77<br>-0 | +0<br>77<br>-0 | +4<br>73<br>-0 | +0<br>77<br>-0 | +4<br>73<br>-0 |
| Obj-C      | +77<br>0<br>-0 | +0<br>77<br>-0 | +74<br>3<br>-0 | +4<br>73<br>-0 | +0<br>77<br>-0 | —     | +4<br>73<br>-0 | +0<br>77<br>-0 | +0<br>77<br>-0 | +4<br>73<br>-0 | +0<br>77<br>-0 | +4<br>73<br>-0 |
| Perl       | +73<br>0<br>-0 | +0<br>73<br>-4 | +70<br>3<br>-0 | +0<br>73<br>-0 | +0<br>73<br>-4 | +0<br>73<br>-4 | —    | +0<br>73<br>-4 | +0<br>73<br>-4 | +0<br>73<br>-0 | +0<br>73<br>-4 | +0<br>73<br>-0 |
| PHP        | +77<br>0<br>-0 | +0<br>77<br>-0 | +74<br>3<br>-0 | +4<br>73<br>-0 | +0<br>77<br>-0 | +0<br>77<br>-0 | +4<br>73<br>-0 | —   | +0<br>77<br>-0 | +4<br>73<br>-0 | +0<br>77<br>-0 | +4<br>73<br>-0 |
| Python     | +77<br>0<br>-0 | +0<br>77<br>-0 | +74<br>3<br>-0 | +4<br>73<br>-0 | +0<br>77<br>-0 | +0<br>77<br>-0 | +4<br>73<br>-0 | +0<br>77<br>-0 | —      | +4<br>73<br>-0 | +0<br>77<br>-0 | +4<br>73<br>-0 |
| Ruby       | +73<br>0<br>-0 | +0<br>73<br>-4 | +70<br>3<br>-0 | +0<br>73<br>-0 | +0<br>73<br>-4 | +0<br>73<br>-4 | +0<br>73<br>-0 | +0<br>73<br>-4 | +0<br>73<br>-4 | —    | +0<br>73<br>-4 | +0<br>73<br>-0 |
| Rust       | +77<br>0<br>-0 | +0<br>77<br>-0 | +74<br>3<br>-0 | +4<br>73<br>-0 | +0<br>77<br>-0 | +0<br>77<br>-0 | +4<br>73<br>-0 | +0<br>77<br>-0 | +0<br>77<br>-0 | +4<br>73<br>-0 | —    | +4<br>73<br>-0 |
| Scala      | +73<br>0<br>-0 | +0<br>73<br>-4 | +70<br>3<br>-0 | +0<br>73<br>-0 | +0<br>73<br>-4 | +0<br>73<br>-4 | +0<br>73<br>-0 | +0<br>73<br>-4 | +0<br>73<br>-4 | +0<br>73<br>-0 | +0<br>73<br>-4 | —     |

#### Character Classes - POSIX - Short - Initial Punctuation (`[\p{Pi}]`)

| Language   | C++    | Go     | Haskell | Java   | Javascript | Obj-C  | Perl   | PHP    | Python | Ruby   | Rust   | Scala  |
| :--------- | -----: | -----: | ------: | -----: | ---------: | -----: | -----: | -----: | -----: | -----: | -----: | -----: |
| C++        | —      | +0<br>0<br>-12 | +0<br>0<br>-50323 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-12 | +0<br>0<br>-12 |
| Go         | +12<br>0<br>-0 | —      | +11<br>1<br>-50322 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 |
| Haskell    | +50323<br>0<br>-0 | +50322<br>1<br>-11 | —       | +50322<br>1<br>-11 | +50322<br>1<br>-11 | +50322<br>1<br>-11 | +50322<br>1<br>-11 | +50322<br>1<br>-11 | +50322<br>1<br>-11 | +50322<br>1<br>-11 | +50322<br>1<br>-11 | +50322<br>1<br>-11 |
| Java       | +12<br>0<br>-0 | +0<br>12<br>-0 | +11<br>1<br>-50322 | —      | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 |
| Javascript | +12<br>0<br>-0 | +0<br>12<br>-0 | +11<br>1<br>-50322 | +0<br>12<br>-0 | —          | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 |
| Obj-C      | +12<br>0<br>-0 | +0<br>12<br>-0 | +11<br>1<br>-50322 | +0<br>12<br>-0 | +0<br>12<br>-0 | —      | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 |
| Perl       | +12<br>0<br>-0 | +0<br>12<br>-0 | +11<br>1<br>-50322 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | —      | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 |
| PHP        | +12<br>0<br>-0 | +0<br>12<br>-0 | +11<br>1<br>-50322 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | —      | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 |
| Python     | +12<br>0<br>-0 | +0<br>12<br>-0 | +11<br>1<br>-50322 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | —      | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 |
| Ruby       | +12<br>0<br>-0 | +0<br>12<br>-0 | +11<br>1<br>-50322 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | —      | +0<br>12<br>-0 | +0<br>12<br>-0 |
| Rust       | +12<br>0<br>-0 | +0<br>12<br>-0 | +11<br>1<br>-50322 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | —      | +0<br>12<br>-0 |
| Scala      | +12<br>0<br>-0 | +0<br>12<br>-0 | +11<br>1<br>-50322 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | +0<br>12<br>-0 | —      |

#### Character Classes - POSIX - Short - Final Punctuation (`[\p{Pf}]`)

| Language   | C++    | Go     | Haskell | Java   | Javascript | Obj-C  | Perl   | PHP    | Python | Ruby   | Rust   | Scala  |
| :--------- | -----: | -----: | ------: | -----: | ---------: | -----: | -----: | -----: | -----: | -----: | -----: | -----: |
| C++        | —      | +0<br>0<br>-10 | +0<br>0<br>-50323 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 | +0<br>0<br>-10 |
| Go         | +10<br>0<br>-0 | —      | +9<br>1<br>-50322 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 |
| Haskell    | +50323<br>0<br>-0 | +50322<br>1<br>-9 | —       | +50322<br>1<br>-9 | +50322<br>1<br>-9 | +50322<br>1<br>-9 | +50322<br>1<br>-9 | +50322<br>1<br>-9 | +50322<br>1<br>-9 | +50322<br>1<br>-9 | +50322<br>1<br>-9 | +50322<br>1<br>-9 |
| Java       | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-50322 | —      | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 |
| Javascript | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-50322 | +0<br>10<br>-0 | —          | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 |
| Obj-C      | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-50322 | +0<br>10<br>-0 | +0<br>10<br>-0 | —      | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 |
| Perl       | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-50322 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —      | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 |
| PHP        | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-50322 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —      | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 |
| Python     | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-50322 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —      | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 |
| Ruby       | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-50322 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —      | +0<br>10<br>-0 | +0<br>10<br>-0 |
| Rust       | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-50322 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —      | +0<br>10<br>-0 |
| Scala      | +10<br>0<br>-0 | +0<br>10<br>-0 | +9<br>1<br>-50322 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | +0<br>10<br>-0 | —      |

#### Character Classes - POSIX - Short - Other Punctuation (`[\p{Po}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-628 | +0<br>0<br>-238498 | +0<br>0<br>-593 | +0<br>0<br>-628 | +0<br>0<br>-605 | +0<br>0<br>-593 | +0<br>0<br>-605 | +0<br>0<br>-628 | +0<br>0<br>-588 | +0<br>0<br>-628 | +0<br>0<br>-593 |
| Go         | +628<br>0<br>-0 | —       | +537<br>91<br>-238407 | +35<br>593<br>-0 | +0<br>628<br>-0 | +23<br>605<br>-0 | +35<br>593<br>-0 | +23<br>605<br>-0 | +0<br>628<br>-0 | +40<br>588<br>-0 | +0<br>628<br>-0 | +35<br>593<br>-0 |
| Haskell    | +238498<br>0<br>-0 | +238407<br>91<br>-537 | —       | +238409<br>89<br>-504 | +238407<br>91<br>-537 | +238407<br>91<br>-514 | +238409<br>89<br>-504 | +238407<br>91<br>-514 | +238407<br>91<br>-537 | +238409<br>89<br>-499 | +238407<br>91<br>-537 | +238409<br>89<br>-504 |
| Java       | +593<br>0<br>-0 | +0<br>593<br>-35 | +504<br>89<br>-238409 | —       | +0<br>593<br>-35 | +0<br>593<br>-12 | +0<br>593<br>-0 | +0<br>593<br>-12 | +0<br>593<br>-35 | +5<br>588<br>-0 | +0<br>593<br>-35 | +0<br>593<br>-0 |
| Javascript | +628<br>0<br>-0 | +0<br>628<br>-0 | +537<br>91<br>-238407 | +35<br>593<br>-0 | —          | +23<br>605<br>-0 | +35<br>593<br>-0 | +23<br>605<br>-0 | +0<br>628<br>-0 | +40<br>588<br>-0 | +0<br>628<br>-0 | +35<br>593<br>-0 |
| Obj-C      | +605<br>0<br>-0 | +0<br>605<br>-23 | +514<br>91<br>-238407 | +12<br>593<br>-0 | +0<br>605<br>-23 | —       | +12<br>593<br>-0 | +0<br>605<br>-0 | +0<br>605<br>-23 | +17<br>588<br>-0 | +0<br>605<br>-23 | +12<br>593<br>-0 |
| Perl       | +593<br>0<br>-0 | +0<br>593<br>-35 | +504<br>89<br>-238409 | +0<br>593<br>-0 | +0<br>593<br>-35 | +0<br>593<br>-12 | —       | +0<br>593<br>-12 | +0<br>593<br>-35 | +5<br>588<br>-0 | +0<br>593<br>-35 | +0<br>593<br>-0 |
| PHP        | +605<br>0<br>-0 | +0<br>605<br>-23 | +514<br>91<br>-238407 | +12<br>593<br>-0 | +0<br>605<br>-23 | +0<br>605<br>-0 | +12<br>593<br>-0 | —       | +0<br>605<br>-23 | +17<br>588<br>-0 | +0<br>605<br>-23 | +12<br>593<br>-0 |
| Python     | +628<br>0<br>-0 | +0<br>628<br>-0 | +537<br>91<br>-238407 | +35<br>593<br>-0 | +0<br>628<br>-0 | +23<br>605<br>-0 | +35<br>593<br>-0 | +23<br>605<br>-0 | —       | +40<br>588<br>-0 | +0<br>628<br>-0 | +35<br>593<br>-0 |
| Ruby       | +588<br>0<br>-0 | +0<br>588<br>-40 | +499<br>89<br>-238409 | +0<br>588<br>-5 | +0<br>588<br>-40 | +0<br>588<br>-17 | +0<br>588<br>-5 | +0<br>588<br>-17 | +0<br>588<br>-40 | —       | +0<br>588<br>-40 | +0<br>588<br>-5 |
| Rust       | +628<br>0<br>-0 | +0<br>628<br>-0 | +537<br>91<br>-238407 | +35<br>593<br>-0 | +0<br>628<br>-0 | +23<br>605<br>-0 | +35<br>593<br>-0 | +23<br>605<br>-0 | +0<br>628<br>-0 | +40<br>588<br>-0 | —       | +35<br>593<br>-0 |
| Scala      | +593<br>0<br>-0 | +0<br>593<br>-35 | +504<br>89<br>-238409 | +0<br>593<br>-0 | +0<br>593<br>-35 | +0<br>593<br>-12 | +0<br>593<br>-0 | +0<br>593<br>-12 | +0<br>593<br>-35 | +5<br>588<br>-0 | +0<br>593<br>-35 | —       |

#### Character Classes - POSIX - Short - Punctuation (`[\p{P}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-842 | +0<br>0<br>-322790 | +0<br>0<br>-798 | +0<br>0<br>-842 | +0<br>0<br>-819 | +0<br>0<br>-798 | +0<br>0<br>-819 | +0<br>0<br>-842 | +0<br>0<br>-792 | +0<br>0<br>-842 | +0<br>0<br>-798 |
| Go         | +842<br>0<br>-0 | —       | +689<br>153<br>-322637 | +44<br>798<br>-0 | +0<br>842<br>-0 | +23<br>819<br>-0 | +44<br>798<br>-0 | +23<br>819<br>-0 | +0<br>842<br>-0 | +50<br>792<br>-0 | +0<br>842<br>-0 | +44<br>798<br>-0 |
| Haskell    | +322790<br>0<br>-0 | +322637<br>153<br>-689 | —       | +322639<br>151<br>-647 | +322637<br>153<br>-689 | +322637<br>153<br>-666 | +322639<br>151<br>-647 | +322637<br>153<br>-666 | +322637<br>153<br>-689 | +322639<br>151<br>-641 | +322637<br>153<br>-689 | +322639<br>151<br>-647 |
| Java       | +798<br>0<br>-0 | +0<br>798<br>-44 | +647<br>151<br>-322639 | —       | +0<br>798<br>-44 | +0<br>798<br>-21 | +0<br>798<br>-0 | +0<br>798<br>-21 | +0<br>798<br>-44 | +6<br>792<br>-0 | +0<br>798<br>-44 | +0<br>798<br>-0 |
| Javascript | +842<br>0<br>-0 | +0<br>842<br>-0 | +689<br>153<br>-322637 | +44<br>798<br>-0 | —          | +23<br>819<br>-0 | +44<br>798<br>-0 | +23<br>819<br>-0 | +0<br>842<br>-0 | +50<br>792<br>-0 | +0<br>842<br>-0 | +44<br>798<br>-0 |
| Obj-C      | +819<br>0<br>-0 | +0<br>819<br>-23 | +666<br>153<br>-322637 | +21<br>798<br>-0 | +0<br>819<br>-23 | —       | +21<br>798<br>-0 | +0<br>819<br>-0 | +0<br>819<br>-23 | +27<br>792<br>-0 | +0<br>819<br>-23 | +21<br>798<br>-0 |
| Perl       | +798<br>0<br>-0 | +0<br>798<br>-44 | +647<br>151<br>-322639 | +0<br>798<br>-0 | +0<br>798<br>-44 | +0<br>798<br>-21 | —       | +0<br>798<br>-21 | +0<br>798<br>-44 | +6<br>792<br>-0 | +0<br>798<br>-44 | +0<br>798<br>-0 |
| PHP        | +819<br>0<br>-0 | +0<br>819<br>-23 | +666<br>153<br>-322637 | +21<br>798<br>-0 | +0<br>819<br>-23 | +0<br>819<br>-0 | +21<br>798<br>-0 | —       | +0<br>819<br>-23 | +27<br>792<br>-0 | +0<br>819<br>-23 | +21<br>798<br>-0 |
| Python     | +842<br>0<br>-0 | +0<br>842<br>-0 | +689<br>153<br>-322637 | +44<br>798<br>-0 | +0<br>842<br>-0 | +23<br>819<br>-0 | +44<br>798<br>-0 | +23<br>819<br>-0 | —       | +50<br>792<br>-0 | +0<br>842<br>-0 | +44<br>798<br>-0 |
| Ruby       | +792<br>0<br>-0 | +0<br>792<br>-50 | +641<br>151<br>-322639 | +0<br>792<br>-6 | +0<br>792<br>-50 | +0<br>792<br>-27 | +0<br>792<br>-6 | +0<br>792<br>-27 | +0<br>792<br>-50 | —       | +0<br>792<br>-50 | +0<br>792<br>-6 |
| Rust       | +842<br>0<br>-0 | +0<br>842<br>-0 | +689<br>153<br>-322637 | +44<br>798<br>-0 | +0<br>842<br>-0 | +23<br>819<br>-0 | +44<br>798<br>-0 | +23<br>819<br>-0 | +0<br>842<br>-0 | +50<br>792<br>-0 | —       | +44<br>798<br>-0 |
| Scala      | +798<br>0<br>-0 | +0<br>798<br>-44 | +647<br>151<br>-322639 | +0<br>798<br>-0 | +0<br>798<br>-44 | +0<br>798<br>-21 | +0<br>798<br>-0 | +0<br>798<br>-21 | +0<br>798<br>-44 | +6<br>792<br>-0 | +0<br>798<br>-44 | —       |

#### Character Classes - POSIX - Short - Math Symbol (`[\p{Sm}]`)

| Language   | C++    | Go     | Haskell | Java   | Javascript | Obj-C  | Perl   | PHP    | Python | Ruby   | Rust   | Scala  |
| :--------- | -----: | -----: | ------: | -----: | ---------: | -----: | -----: | -----: | -----: | -----: | -----: | -----: |
| C++        | —      | +0<br>0<br>-948 | +0<br>0<br>-99172 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-948 | +0<br>0<br>-948 |
| Go         | +948<br>0<br>-0 | —      | +894<br>54<br>-99118 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 |
| Haskell    | +99172<br>0<br>-0 | +99118<br>54<br>-894 | —       | +99118<br>54<br>-894 | +99118<br>54<br>-894 | +99118<br>54<br>-894 | +99118<br>54<br>-894 | +99118<br>54<br>-894 | +99118<br>54<br>-894 | +99118<br>54<br>-894 | +99118<br>54<br>-894 | +99118<br>54<br>-894 |
| Java       | +948<br>0<br>-0 | +0<br>948<br>-0 | +894<br>54<br>-99118 | —      | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 |
| Javascript | +948<br>0<br>-0 | +0<br>948<br>-0 | +894<br>54<br>-99118 | +0<br>948<br>-0 | —          | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 |
| Obj-C      | +948<br>0<br>-0 | +0<br>948<br>-0 | +894<br>54<br>-99118 | +0<br>948<br>-0 | +0<br>948<br>-0 | —      | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 |
| Perl       | +948<br>0<br>-0 | +0<br>948<br>-0 | +894<br>54<br>-99118 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | —      | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 |
| PHP        | +948<br>0<br>-0 | +0<br>948<br>-0 | +894<br>54<br>-99118 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | —      | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 |
| Python     | +948<br>0<br>-0 | +0<br>948<br>-0 | +894<br>54<br>-99118 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | —      | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 |
| Ruby       | +948<br>0<br>-0 | +0<br>948<br>-0 | +894<br>54<br>-99118 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | —      | +0<br>948<br>-0 | +0<br>948<br>-0 |
| Rust       | +948<br>0<br>-0 | +0<br>948<br>-0 | +894<br>54<br>-99118 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | —      | +0<br>948<br>-0 |
| Scala      | +948<br>0<br>-0 | +0<br>948<br>-0 | +894<br>54<br>-99118 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | +0<br>948<br>-0 | —      |

#### Character Classes - POSIX - Short - Currency Symbol (`[\p{Sc}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-63 | +0<br>0<br>-192137 | +0<br>0<br>-62 | +0<br>0<br>-63 | +0<br>0<br>-63 | +0<br>0<br>-62 | +0<br>0<br>-63 | +0<br>0<br>-63 | +0<br>0<br>-62 | +0<br>0<br>-63 | +0<br>0<br>-62 |
| Go         | +63<br>0<br>-0 | —       | +53<br>10<br>-192127 | +1<br>62<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +1<br>62<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +1<br>62<br>-0 | +0<br>63<br>-0 | +1<br>62<br>-0 |
| Haskell    | +192137<br>0<br>-0 | +192127<br>10<br>-53 | —       | +192127<br>10<br>-52 | +192127<br>10<br>-53 | +192127<br>10<br>-53 | +192127<br>10<br>-52 | +192127<br>10<br>-53 | +192127<br>10<br>-53 | +192127<br>10<br>-52 | +192127<br>10<br>-53 | +192127<br>10<br>-52 |
| Java       | +62<br>0<br>-0 | +0<br>62<br>-1 | +52<br>10<br>-192127 | —       | +0<br>62<br>-1 | +0<br>62<br>-1 | +0<br>62<br>-0 | +0<br>62<br>-1 | +0<br>62<br>-1 | +0<br>62<br>-0 | +0<br>62<br>-1 | +0<br>62<br>-0 |
| Javascript | +63<br>0<br>-0 | +0<br>63<br>-0 | +53<br>10<br>-192127 | +1<br>62<br>-0 | —          | +0<br>63<br>-0 | +1<br>62<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +1<br>62<br>-0 | +0<br>63<br>-0 | +1<br>62<br>-0 |
| Obj-C      | +63<br>0<br>-0 | +0<br>63<br>-0 | +53<br>10<br>-192127 | +1<br>62<br>-0 | +0<br>63<br>-0 | —       | +1<br>62<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +1<br>62<br>-0 | +0<br>63<br>-0 | +1<br>62<br>-0 |
| Perl       | +62<br>0<br>-0 | +0<br>62<br>-1 | +52<br>10<br>-192127 | +0<br>62<br>-0 | +0<br>62<br>-1 | +0<br>62<br>-1 | —       | +0<br>62<br>-1 | +0<br>62<br>-1 | +0<br>62<br>-0 | +0<br>62<br>-1 | +0<br>62<br>-0 |
| PHP        | +63<br>0<br>-0 | +0<br>63<br>-0 | +53<br>10<br>-192127 | +1<br>62<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +1<br>62<br>-0 | —       | +0<br>63<br>-0 | +1<br>62<br>-0 | +0<br>63<br>-0 | +1<br>62<br>-0 |
| Python     | +63<br>0<br>-0 | +0<br>63<br>-0 | +53<br>10<br>-192127 | +1<br>62<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +1<br>62<br>-0 | +0<br>63<br>-0 | —       | +1<br>62<br>-0 | +0<br>63<br>-0 | +1<br>62<br>-0 |
| Ruby       | +62<br>0<br>-0 | +0<br>62<br>-1 | +52<br>10<br>-192127 | +0<br>62<br>-0 | +0<br>62<br>-1 | +0<br>62<br>-1 | +0<br>62<br>-0 | +0<br>62<br>-1 | +0<br>62<br>-1 | —       | +0<br>62<br>-1 | +0<br>62<br>-0 |
| Rust       | +63<br>0<br>-0 | +0<br>63<br>-0 | +53<br>10<br>-192127 | +1<br>62<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +1<br>62<br>-0 | +0<br>63<br>-0 | +0<br>63<br>-0 | +1<br>62<br>-0 | —       | +1<br>62<br>-0 |
| Scala      | +62<br>0<br>-0 | +0<br>62<br>-1 | +52<br>10<br>-192127 | +0<br>62<br>-0 | +0<br>62<br>-1 | +0<br>62<br>-1 | +0<br>62<br>-0 | +0<br>62<br>-1 | +0<br>62<br>-1 | +0<br>62<br>-0 | +0<br>62<br>-1 | —       |

#### Character Classes - POSIX - Short - Modifier Symbol (`[\p{Sk}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-125 | +0<br>0<br>-192138 | +0<br>0<br>-123 | +0<br>0<br>-125 | +0<br>0<br>-125 | +0<br>0<br>-123 | +0<br>0<br>-125 | +0<br>0<br>-125 | +0<br>0<br>-121 | +0<br>0<br>-125 | +0<br>0<br>-123 |
| Go         | +125<br>0<br>-0 | —       | +109<br>16<br>-192122 | +2<br>123<br>-0 | +0<br>125<br>-0 | +0<br>125<br>-0 | +2<br>123<br>-0 | +0<br>125<br>-0 | +0<br>125<br>-0 | +4<br>121<br>-0 | +0<br>125<br>-0 | +2<br>123<br>-0 |
| Haskell    | +192138<br>0<br>-0 | +192122<br>16<br>-109 | —       | +192123<br>15<br>-108 | +192122<br>16<br>-109 | +192122<br>16<br>-109 | +192123<br>15<br>-108 | +192122<br>16<br>-109 | +192122<br>16<br>-109 | +192123<br>15<br>-106 | +192122<br>16<br>-109 | +192123<br>15<br>-108 |
| Java       | +123<br>0<br>-0 | +0<br>123<br>-2 | +108<br>15<br>-192123 | —       | +0<br>123<br>-2 | +0<br>123<br>-2 | +0<br>123<br>-0 | +0<br>123<br>-2 | +0<br>123<br>-2 | +2<br>121<br>-0 | +0<br>123<br>-2 | +0<br>123<br>-0 |
| Javascript | +125<br>0<br>-0 | +0<br>125<br>-0 | +109<br>16<br>-192122 | +2<br>123<br>-0 | —          | +0<br>125<br>-0 | +2<br>123<br>-0 | +0<br>125<br>-0 | +0<br>125<br>-0 | +4<br>121<br>-0 | +0<br>125<br>-0 | +2<br>123<br>-0 |
| Obj-C      | +125<br>0<br>-0 | +0<br>125<br>-0 | +109<br>16<br>-192122 | +2<br>123<br>-0 | +0<br>125<br>-0 | —       | +2<br>123<br>-0 | +0<br>125<br>-0 | +0<br>125<br>-0 | +4<br>121<br>-0 | +0<br>125<br>-0 | +2<br>123<br>-0 |
| Perl       | +123<br>0<br>-0 | +0<br>123<br>-2 | +108<br>15<br>-192123 | +0<br>123<br>-0 | +0<br>123<br>-2 | +0<br>123<br>-2 | —       | +0<br>123<br>-2 | +0<br>123<br>-2 | +2<br>121<br>-0 | +0<br>123<br>-2 | +0<br>123<br>-0 |
| PHP        | +125<br>0<br>-0 | +0<br>125<br>-0 | +109<br>16<br>-192122 | +2<br>123<br>-0 | +0<br>125<br>-0 | +0<br>125<br>-0 | +2<br>123<br>-0 | —       | +0<br>125<br>-0 | +4<br>121<br>-0 | +0<br>125<br>-0 | +2<br>123<br>-0 |
| Python     | +125<br>0<br>-0 | +0<br>125<br>-0 | +109<br>16<br>-192122 | +2<br>123<br>-0 | +0<br>125<br>-0 | +0<br>125<br>-0 | +2<br>123<br>-0 | +0<br>125<br>-0 | —       | +4<br>121<br>-0 | +0<br>125<br>-0 | +2<br>123<br>-0 |
| Ruby       | +121<br>0<br>-0 | +0<br>121<br>-4 | +106<br>15<br>-192123 | +0<br>121<br>-2 | +0<br>121<br>-4 | +0<br>121<br>-4 | +0<br>121<br>-2 | +0<br>121<br>-4 | +0<br>121<br>-4 | —       | +0<br>121<br>-4 | +0<br>121<br>-2 |
| Rust       | +125<br>0<br>-0 | +0<br>125<br>-0 | +109<br>16<br>-192122 | +2<br>123<br>-0 | +0<br>125<br>-0 | +0<br>125<br>-0 | +2<br>123<br>-0 | +0<br>125<br>-0 | +0<br>125<br>-0 | +4<br>121<br>-0 | —       | +2<br>123<br>-0 |
| Scala      | +123<br>0<br>-0 | +0<br>123<br>-2 | +108<br>15<br>-192123 | +0<br>123<br>-0 | +0<br>123<br>-2 | +0<br>123<br>-2 | +0<br>123<br>-0 | +0<br>123<br>-2 | +0<br>123<br>-2 | +2<br>121<br>-0 | +0<br>123<br>-2 | —       |

#### Character Classes - POSIX - Short - Other Symbol (`[\p{So}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-8682 | +0<br>0<br>-192136 | +0<br>0<br>-6431 | +0<br>0<br>-6634 | +0<br>0<br>-6605 | +0<br>0<br>-6431 | +0<br>0<br>-6605 | +0<br>0<br>-6634 | +0<br>0<br>-6161 | +0<br>0<br>-6634 | +0<br>0<br>-6431 |
| Go         | +8682<br>0<br>-0 | —       | +7961<br>721<br>-191415 | +2251<br>6431<br>-0 | +2048<br>6634<br>-0 | +2077<br>6605<br>-0 | +2251<br>6431<br>-0 | +2077<br>6605<br>-0 | +2048<br>6634<br>-0 | +2521<br>6161<br>-0 | +2048<br>6634<br>-0 | +2251<br>6431<br>-0 |
| Haskell    | +192136<br>0<br>-0 | +191415<br>721<br>-7961 | —       | +191434<br>702<br>-5729 | +191415<br>721<br>-5913 | +191419<br>717<br>-5888 | +191434<br>702<br>-5729 | +191419<br>717<br>-5888 | +191415<br>721<br>-5913 | +191516<br>620<br>-5541 | +191415<br>721<br>-5913 | +191434<br>702<br>-5729 |
| Java       | +6431<br>0<br>-0 | +0<br>6431<br>-2251 | +5729<br>702<br>-191434 | —       | +0<br>6431<br>-203 | +0<br>6431<br>-174 | +0<br>6431<br>-0 | +0<br>6431<br>-174 | +0<br>6431<br>-203 | +270<br>6161<br>-0 | +0<br>6431<br>-203 | +0<br>6431<br>-0 |
| Javascript | +6634<br>0<br>-0 | +0<br>6634<br>-2048 | +5913<br>721<br>-191415 | +203<br>6431<br>-0 | —          | +29<br>6605<br>-0 | +203<br>6431<br>-0 | +29<br>6605<br>-0 | +0<br>6634<br>-0 | +473<br>6161<br>-0 | +0<br>6634<br>-0 | +203<br>6431<br>-0 |
| Obj-C      | +6605<br>0<br>-0 | +0<br>6605<br>-2077 | +5888<br>717<br>-191419 | +174<br>6431<br>-0 | +0<br>6605<br>-29 | —       | +174<br>6431<br>-0 | +0<br>6605<br>-0 | +0<br>6605<br>-29 | +444<br>6161<br>-0 | +0<br>6605<br>-29 | +174<br>6431<br>-0 |
| Perl       | +6431<br>0<br>-0 | +0<br>6431<br>-2251 | +5729<br>702<br>-191434 | +0<br>6431<br>-0 | +0<br>6431<br>-203 | +0<br>6431<br>-174 | —       | +0<br>6431<br>-174 | +0<br>6431<br>-203 | +270<br>6161<br>-0 | +0<br>6431<br>-203 | +0<br>6431<br>-0 |
| PHP        | +6605<br>0<br>-0 | +0<br>6605<br>-2077 | +5888<br>717<br>-191419 | +174<br>6431<br>-0 | +0<br>6605<br>-29 | +0<br>6605<br>-0 | +174<br>6431<br>-0 | —       | +0<br>6605<br>-29 | +444<br>6161<br>-0 | +0<br>6605<br>-29 | +174<br>6431<br>-0 |
| Python     | +6634<br>0<br>-0 | +0<br>6634<br>-2048 | +5913<br>721<br>-191415 | +203<br>6431<br>-0 | +0<br>6634<br>-0 | +29<br>6605<br>-0 | +203<br>6431<br>-0 | +29<br>6605<br>-0 | —       | +473<br>6161<br>-0 | +0<br>6634<br>-0 | +203<br>6431<br>-0 |
| Ruby       | +6161<br>0<br>-0 | +0<br>6161<br>-2521 | +5541<br>620<br>-191516 | +0<br>6161<br>-270 | +0<br>6161<br>-473 | +0<br>6161<br>-444 | +0<br>6161<br>-270 | +0<br>6161<br>-444 | +0<br>6161<br>-473 | —       | +0<br>6161<br>-473 | +0<br>6161<br>-270 |
| Rust       | +6634<br>0<br>-0 | +0<br>6634<br>-2048 | +5913<br>721<br>-191415 | +203<br>6431<br>-0 | +0<br>6634<br>-0 | +29<br>6605<br>-0 | +203<br>6431<br>-0 | +29<br>6605<br>-0 | +0<br>6634<br>-0 | +473<br>6161<br>-0 | —       | +203<br>6431<br>-0 |
| Scala      | +6431<br>0<br>-0 | +0<br>6431<br>-2251 | +5729<br>702<br>-191434 | +0<br>6431<br>-0 | +0<br>6431<br>-203 | +0<br>6431<br>-174 | +0<br>6431<br>-0 | +0<br>6431<br>-174 | +0<br>6431<br>-203 | +270<br>6161<br>-0 | +0<br>6431<br>-203 | —       |

#### Character Classes - POSIX - Short - Symbol (`[\p{S}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-9818 | +0<br>0<br>-572995 | +0<br>0<br>-7564 | +0<br>0<br>-7770 | +0<br>0<br>-7741 | +0<br>0<br>-7564 | +0<br>0<br>-7741 | +0<br>0<br>-7770 | +0<br>0<br>-7292 | +0<br>0<br>-7770 | +0<br>0<br>-7564 |
| Go         | +9818<br>0<br>-0 | —       | +6944<br>2874<br>-570121 | +2254<br>7564<br>-0 | +2048<br>7770<br>-0 | +2077<br>7741<br>-0 | +2254<br>7564<br>-0 | +2077<br>7741<br>-0 | +2048<br>7770<br>-0 | +2526<br>7292<br>-0 | +2048<br>7770<br>-0 | +2254<br>7564<br>-0 |
| Haskell    | +572995<br>0<br>-0 | +570121<br>2874<br>-6944 | —       | +570175<br>2820<br>-4744 | +570121<br>2874<br>-4896 | +570129<br>2866<br>-4875 | +570175<br>2820<br>-4744 | +570129<br>2866<br>-4875 | +570121<br>2874<br>-4896 | +570351<br>2644<br>-4648 | +570121<br>2874<br>-4896 | +570175<br>2820<br>-4744 |
| Java       | +7564<br>0<br>-0 | +0<br>7564<br>-2254 | +4744<br>2820<br>-570175 | —       | +0<br>7564<br>-206 | +0<br>7564<br>-177 | +0<br>7564<br>-0 | +0<br>7564<br>-177 | +0<br>7564<br>-206 | +272<br>7292<br>-0 | +0<br>7564<br>-206 | +0<br>7564<br>-0 |
| Javascript | +7770<br>0<br>-0 | +0<br>7770<br>-2048 | +4896<br>2874<br>-570121 | +206<br>7564<br>-0 | —          | +29<br>7741<br>-0 | +206<br>7564<br>-0 | +29<br>7741<br>-0 | +0<br>7770<br>-0 | +478<br>7292<br>-0 | +0<br>7770<br>-0 | +206<br>7564<br>-0 |
| Obj-C      | +7741<br>0<br>-0 | +0<br>7741<br>-2077 | +4875<br>2866<br>-570129 | +177<br>7564<br>-0 | +0<br>7741<br>-29 | —       | +177<br>7564<br>-0 | +0<br>7741<br>-0 | +0<br>7741<br>-29 | +449<br>7292<br>-0 | +0<br>7741<br>-29 | +177<br>7564<br>-0 |
| Perl       | +7564<br>0<br>-0 | +0<br>7564<br>-2254 | +4744<br>2820<br>-570175 | +0<br>7564<br>-0 | +0<br>7564<br>-206 | +0<br>7564<br>-177 | —       | +0<br>7564<br>-177 | +0<br>7564<br>-206 | +272<br>7292<br>-0 | +0<br>7564<br>-206 | +0<br>7564<br>-0 |
| PHP        | +7741<br>0<br>-0 | +0<br>7741<br>-2077 | +4875<br>2866<br>-570129 | +177<br>7564<br>-0 | +0<br>7741<br>-29 | +0<br>7741<br>-0 | +177<br>7564<br>-0 | —       | +0<br>7741<br>-29 | +449<br>7292<br>-0 | +0<br>7741<br>-29 | +177<br>7564<br>-0 |
| Python     | +7770<br>0<br>-0 | +0<br>7770<br>-2048 | +4896<br>2874<br>-570121 | +206<br>7564<br>-0 | +0<br>7770<br>-0 | +29<br>7741<br>-0 | +206<br>7564<br>-0 | +29<br>7741<br>-0 | —       | +478<br>7292<br>-0 | +0<br>7770<br>-0 | +206<br>7564<br>-0 |
| Ruby       | +7292<br>0<br>-0 | +0<br>7292<br>-2526 | +4648<br>2644<br>-570351 | +0<br>7292<br>-272 | +0<br>7292<br>-478 | +0<br>7292<br>-449 | +0<br>7292<br>-272 | +0<br>7292<br>-449 | +0<br>7292<br>-478 | —       | +0<br>7292<br>-478 | +0<br>7292<br>-272 |
| Rust       | +7770<br>0<br>-0 | +0<br>7770<br>-2048 | +4896<br>2874<br>-570121 | +206<br>7564<br>-0 | +0<br>7770<br>-0 | +29<br>7741<br>-0 | +206<br>7564<br>-0 | +29<br>7741<br>-0 | +0<br>7770<br>-0 | +478<br>7292<br>-0 | —       | +206<br>7564<br>-0 |
| Scala      | +7564<br>0<br>-0 | +0<br>7564<br>-2254 | +4744<br>2820<br>-570175 | +0<br>7564<br>-0 | +0<br>7564<br>-206 | +0<br>7564<br>-177 | +0<br>7564<br>-0 | +0<br>7564<br>-177 | +0<br>7564<br>-206 | +272<br>7292<br>-0 | +0<br>7564<br>-206 | —       |

#### Character Classes - POSIX - Short - Space Separator (`[\p{Zs}]`)

| Language   | C++    | Go     | Haskell | Java   | Javascript | Obj-C  | Perl   | PHP    | Python | Ruby   | Rust   | Scala  |
| :--------- | -----: | -----: | ------: | -----: | ---------: | -----: | -----: | -----: | -----: | -----: | -----: | -----: |
| C++        | —      | +0<br>0<br>-17 | +0<br>0<br>-50324 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-17 | +0<br>0<br>-17 |
| Go         | +17<br>0<br>-0 | —      | +15<br>2<br>-50322 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 |
| Haskell    | +50324<br>0<br>-0 | +50322<br>2<br>-15 | —       | +50322<br>2<br>-15 | +50322<br>2<br>-15 | +50322<br>2<br>-15 | +50322<br>2<br>-15 | +50322<br>2<br>-15 | +50322<br>2<br>-15 | +50322<br>2<br>-15 | +50322<br>2<br>-15 | +50322<br>2<br>-15 |
| Java       | +17<br>0<br>-0 | +0<br>17<br>-0 | +15<br>2<br>-50322 | —      | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 |
| Javascript | +17<br>0<br>-0 | +0<br>17<br>-0 | +15<br>2<br>-50322 | +0<br>17<br>-0 | —          | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 |
| Obj-C      | +17<br>0<br>-0 | +0<br>17<br>-0 | +15<br>2<br>-50322 | +0<br>17<br>-0 | +0<br>17<br>-0 | —      | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 |
| Perl       | +17<br>0<br>-0 | +0<br>17<br>-0 | +15<br>2<br>-50322 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | —      | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 |
| PHP        | +17<br>0<br>-0 | +0<br>17<br>-0 | +15<br>2<br>-50322 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | —      | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 |
| Python     | +17<br>0<br>-0 | +0<br>17<br>-0 | +15<br>2<br>-50322 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | —      | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 |
| Ruby       | +17<br>0<br>-0 | +0<br>17<br>-0 | +15<br>2<br>-50322 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | —      | +0<br>17<br>-0 | +0<br>17<br>-0 |
| Rust       | +17<br>0<br>-0 | +0<br>17<br>-0 | +15<br>2<br>-50322 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | —      | +0<br>17<br>-0 |
| Scala      | +17<br>0<br>-0 | +0<br>17<br>-0 | +15<br>2<br>-50322 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | +0<br>17<br>-0 | —      |

#### Character Classes - POSIX - Short - Line Separator (`[\p{Zl}]`)

| Language   | C++ | Go | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | -: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-1 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 |
| Go         | +1<br>0<br>-0 | —  | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-1 | —       | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 |
| Java       | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | —    | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 |
| Javascript | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | —          | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 |
| Obj-C      | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —     | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 |
| Perl       | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —    | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 |
| PHP        | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —   | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 |
| Python     | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —      | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 |
| Ruby       | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —    | +0<br>1<br>-0 | +0<br>1<br>-0 |
| Rust       | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —    | +0<br>1<br>-0 |
| Scala      | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —     |

#### Character Classes - POSIX - Short - Paragraph Separator (`[\p{Zp}]`)

| Language   | C++ | Go | Haskell | Java | Javascript | Obj-C | Perl | PHP | Python | Ruby | Rust | Scala |
| :--------- | --: | -: | ------: | ---: | ---------: | ----: | ---: | --: | -----: | ---: | ---: | ----: |
| C++        | —   | +0<br>0<br>-1 | +0<br>0<br>-0 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 |
| Go         | +1<br>0<br>-0 | —  | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-1 | —       | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 | +0<br>0<br>-1 |
| Java       | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | —    | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 |
| Javascript | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | —          | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 |
| Obj-C      | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —     | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 |
| Perl       | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —    | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 |
| PHP        | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —   | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 |
| Python     | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —      | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 |
| Ruby       | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —    | +0<br>1<br>-0 | +0<br>1<br>-0 |
| Rust       | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —    | +0<br>1<br>-0 |
| Scala      | +1<br>0<br>-0 | +0<br>1<br>-0 | +1<br>0<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | +0<br>1<br>-0 | —     |

#### Character Classes - POSIX - Short - Separator (`[\p{Z}]`)

| Language   | C++    | Go     | Haskell | Java   | Javascript | Obj-C  | Perl   | PHP    | Python | Ruby   | Rust   | Scala  |
| :--------- | -----: | -----: | ------: | -----: | ---------: | -----: | -----: | -----: | -----: | -----: | -----: | -----: |
| C++        | —      | +0<br>0<br>-19 | +0<br>0<br>-50324 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-19 | +0<br>0<br>-19 |
| Go         | +19<br>0<br>-0 | —      | +17<br>2<br>-50322 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 |
| Haskell    | +50324<br>0<br>-0 | +50322<br>2<br>-17 | —       | +50322<br>2<br>-17 | +50322<br>2<br>-17 | +50322<br>2<br>-17 | +50322<br>2<br>-17 | +50322<br>2<br>-17 | +50322<br>2<br>-17 | +50322<br>2<br>-17 | +50322<br>2<br>-17 | +50322<br>2<br>-17 |
| Java       | +19<br>0<br>-0 | +0<br>19<br>-0 | +17<br>2<br>-50322 | —      | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 |
| Javascript | +19<br>0<br>-0 | +0<br>19<br>-0 | +17<br>2<br>-50322 | +0<br>19<br>-0 | —          | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 |
| Obj-C      | +19<br>0<br>-0 | +0<br>19<br>-0 | +17<br>2<br>-50322 | +0<br>19<br>-0 | +0<br>19<br>-0 | —      | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 |
| Perl       | +19<br>0<br>-0 | +0<br>19<br>-0 | +17<br>2<br>-50322 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | —      | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 |
| PHP        | +19<br>0<br>-0 | +0<br>19<br>-0 | +17<br>2<br>-50322 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | —      | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 |
| Python     | +19<br>0<br>-0 | +0<br>19<br>-0 | +17<br>2<br>-50322 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | —      | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 |
| Ruby       | +19<br>0<br>-0 | +0<br>19<br>-0 | +17<br>2<br>-50322 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | —      | +0<br>19<br>-0 | +0<br>19<br>-0 |
| Rust       | +19<br>0<br>-0 | +0<br>19<br>-0 | +17<br>2<br>-50322 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | —      | +0<br>19<br>-0 |
| Scala      | +19<br>0<br>-0 | +0<br>19<br>-0 | +17<br>2<br>-50322 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | +0<br>19<br>-0 | —      |

#### Character Classes - POSIX - Short - Control (`[\p{Cc}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-65 | +0<br>0<br>-964576 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-65 | +0<br>0<br>-65 |
| Go         | +65<br>0<br>-0 | —       | +1<br>64<br>-964512 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 |
| Haskell    | +964576<br>0<br>-0 | +964512<br>64<br>-1 | —       | +964512<br>64<br>-1 | +964512<br>64<br>-1 | +964512<br>64<br>-1 | +964512<br>64<br>-1 | +964512<br>64<br>-1 | +964512<br>64<br>-1 | +964512<br>64<br>-1 | +964512<br>64<br>-1 | +964512<br>64<br>-1 |
| Java       | +65<br>0<br>-0 | +0<br>65<br>-0 | +1<br>64<br>-964512 | —       | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 |
| Javascript | +65<br>0<br>-0 | +0<br>65<br>-0 | +1<br>64<br>-964512 | +0<br>65<br>-0 | —          | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 |
| Obj-C      | +65<br>0<br>-0 | +0<br>65<br>-0 | +1<br>64<br>-964512 | +0<br>65<br>-0 | +0<br>65<br>-0 | —       | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 |
| Perl       | +65<br>0<br>-0 | +0<br>65<br>-0 | +1<br>64<br>-964512 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | —       | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 |
| PHP        | +65<br>0<br>-0 | +0<br>65<br>-0 | +1<br>64<br>-964512 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | —       | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 |
| Python     | +65<br>0<br>-0 | +0<br>65<br>-0 | +1<br>64<br>-964512 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | —       | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 |
| Ruby       | +65<br>0<br>-0 | +0<br>65<br>-0 | +1<br>64<br>-964512 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | —       | +0<br>65<br>-0 | +0<br>65<br>-0 |
| Rust       | +65<br>0<br>-0 | +0<br>65<br>-0 | +1<br>64<br>-964512 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | —       | +0<br>65<br>-0 |
| Scala      | +65<br>0<br>-0 | +0<br>65<br>-0 | +1<br>64<br>-964512 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | +0<br>65<br>-0 | —       |

#### Character Classes - POSIX - Short - Format (`[\p{Cf}]`)

| Language   | C++    | Go     | Haskell | Java   | Javascript | Obj-C  | Perl   | PHP    | Python | Ruby   | Rust   | Scala  |
| :--------- | -----: | -----: | ------: | -----: | ---------: | -----: | -----: | -----: | -----: | -----: | -----: | -----: |
| C++        | —      | +0<br>0<br>-170 | +0<br>0<br>-50323 | +0<br>0<br>-161 | +0<br>0<br>-170 | +0<br>0<br>-163 | +0<br>0<br>-161 | +0<br>0<br>-163 | +0<br>0<br>-170 | +0<br>0<br>-161 | +0<br>0<br>-170 | +0<br>0<br>-161 |
| Go         | +170<br>0<br>-0 | —      | +165<br>5<br>-50318 | +9<br>161<br>-0 | +0<br>170<br>-0 | +7<br>163<br>-0 | +9<br>161<br>-0 | +7<br>163<br>-0 | +0<br>170<br>-0 | +9<br>161<br>-0 | +0<br>170<br>-0 | +9<br>161<br>-0 |
| Haskell    | +50323<br>0<br>-0 | +50318<br>5<br>-165 | —       | +50318<br>5<br>-156 | +50318<br>5<br>-165 | +50318<br>5<br>-158 | +50318<br>5<br>-156 | +50318<br>5<br>-158 | +50318<br>5<br>-165 | +50318<br>5<br>-156 | +50318<br>5<br>-165 | +50318<br>5<br>-156 |
| Java       | +161<br>0<br>-0 | +0<br>161<br>-9 | +156<br>5<br>-50318 | —      | +0<br>161<br>-9 | +0<br>161<br>-2 | +0<br>161<br>-0 | +0<br>161<br>-2 | +0<br>161<br>-9 | +0<br>161<br>-0 | +0<br>161<br>-9 | +0<br>161<br>-0 |
| Javascript | +170<br>0<br>-0 | +0<br>170<br>-0 | +165<br>5<br>-50318 | +9<br>161<br>-0 | —          | +7<br>163<br>-0 | +9<br>161<br>-0 | +7<br>163<br>-0 | +0<br>170<br>-0 | +9<br>161<br>-0 | +0<br>170<br>-0 | +9<br>161<br>-0 |
| Obj-C      | +163<br>0<br>-0 | +0<br>163<br>-7 | +158<br>5<br>-50318 | +2<br>161<br>-0 | +0<br>163<br>-7 | —      | +2<br>161<br>-0 | +0<br>163<br>-0 | +0<br>163<br>-7 | +2<br>161<br>-0 | +0<br>163<br>-7 | +2<br>161<br>-0 |
| Perl       | +161<br>0<br>-0 | +0<br>161<br>-9 | +156<br>5<br>-50318 | +0<br>161<br>-0 | +0<br>161<br>-9 | +0<br>161<br>-2 | —      | +0<br>161<br>-2 | +0<br>161<br>-9 | +0<br>161<br>-0 | +0<br>161<br>-9 | +0<br>161<br>-0 |
| PHP        | +163<br>0<br>-0 | +0<br>163<br>-7 | +158<br>5<br>-50318 | +2<br>161<br>-0 | +0<br>163<br>-7 | +0<br>163<br>-0 | +2<br>161<br>-0 | —      | +0<br>163<br>-7 | +2<br>161<br>-0 | +0<br>163<br>-7 | +2<br>161<br>-0 |
| Python     | +170<br>0<br>-0 | +0<br>170<br>-0 | +165<br>5<br>-50318 | +9<br>161<br>-0 | +0<br>170<br>-0 | +7<br>163<br>-0 | +9<br>161<br>-0 | +7<br>163<br>-0 | —      | +9<br>161<br>-0 | +0<br>170<br>-0 | +9<br>161<br>-0 |
| Ruby       | +161<br>0<br>-0 | +0<br>161<br>-9 | +156<br>5<br>-50318 | +0<br>161<br>-0 | +0<br>161<br>-9 | +0<br>161<br>-2 | +0<br>161<br>-0 | +0<br>161<br>-2 | +0<br>161<br>-9 | —      | +0<br>161<br>-9 | +0<br>161<br>-0 |
| Rust       | +170<br>0<br>-0 | +0<br>170<br>-0 | +165<br>5<br>-50318 | +9<br>161<br>-0 | +0<br>170<br>-0 | +7<br>163<br>-0 | +9<br>161<br>-0 | +7<br>163<br>-0 | +0<br>170<br>-0 | +9<br>161<br>-0 | —      | +9<br>161<br>-0 |
| Scala      | +161<br>0<br>-0 | +0<br>161<br>-9 | +156<br>5<br>-50318 | +0<br>161<br>-0 | +0<br>161<br>-9 | +0<br>161<br>-2 | +0<br>161<br>-0 | +0<br>161<br>-2 | +0<br>161<br>-9 | +0<br>161<br>-0 | +0<br>161<br>-9 | —      |

#### Character Classes - POSIX - Short - Surrogate (`[\p{Cs}]`)

| Language   | C++   | Go    | Haskell | Java  | Javascript | Obj-C | Perl  | PHP   | Python | Ruby  | Rust  | Scala |
| :--------- | ----: | ----: | ------: | ----: | ---------: | ----: | ----: | ----: | -----: | ----: | ----: | ----: |
| C++        | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 |
| Go         | +0<br>0<br>-0 | —     | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-2048 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 |
| Java       | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | —     | +0<br>2048<br>-0 | +2048<br>0<br>-0 | +0<br>2048<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +0<br>2048<br>-0 |
| Javascript | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +0<br>2048<br>-0 | —          | +2048<br>0<br>-0 | +0<br>2048<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +0<br>2048<br>-0 |
| Obj-C      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-2048 | —     | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 |
| Perl       | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +0<br>2048<br>-0 | +0<br>2048<br>-0 | +2048<br>0<br>-0 | —     | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +0<br>2048<br>-0 |
| PHP        | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | —     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | —      | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 |
| Ruby       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-0 | —     | +0<br>0<br>-0 | +0<br>0<br>-2048 |
| Rust       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-2048 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | —     | +0<br>0<br>-2048 |
| Scala      | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +0<br>2048<br>-0 | +0<br>2048<br>-0 | +2048<br>0<br>-0 | +0<br>2048<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | +2048<br>0<br>-0 | —     |

#### Character Classes - POSIX - Short - Private Use (`[\p{Co}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-137468 | +0<br>0<br>-0 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 |
| Go         | +137468<br>0<br>-0 | —       | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-137468 | —       | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 | +0<br>0<br>-137468 |
| Java       | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +137468<br>0<br>-0 | —       | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 |
| Javascript | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | —          | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 |
| Obj-C      | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | —       | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 |
| Perl       | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | —       | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 |
| PHP        | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | —       | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 |
| Python     | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | —       | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 |
| Ruby       | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | —       | +0<br>137468<br>-0 | +0<br>137468<br>-0 |
| Rust       | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | —       | +0<br>137468<br>-0 |
| Scala      | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +137468<br>0<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | +0<br>137468<br>-0 | —       |

#### Character Classes - POSIX - Short - Unassigned (`[\p{Cn}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-830672 | +0<br>0<br>-825345 | +0<br>0<br>-829834 | +0<br>0<br>-830672 | +0<br>0<br>-829834 | +0<br>0<br>-0 | +0<br>0<br>-836602 | +0<br>0<br>-825345 | +0<br>0<br>-830672 |
| Go         | +0<br>0<br>-0 | —       | +0<br>0<br>-0 | +0<br>0<br>-830672 | +0<br>0<br>-825345 | +0<br>0<br>-829834 | +0<br>0<br>-830672 | +0<br>0<br>-829834 | +0<br>0<br>-0 | +0<br>0<br>-836602 | +0<br>0<br>-825345 | +0<br>0<br>-830672 |
| Haskell    | +0<br>0<br>-0 | +0<br>0<br>-0 | —       | +0<br>0<br>-830672 | +0<br>0<br>-825345 | +0<br>0<br>-829834 | +0<br>0<br>-830672 | +0<br>0<br>-829834 | +0<br>0<br>-0 | +0<br>0<br>-836602 | +0<br>0<br>-825345 | +0<br>0<br>-830672 |
| Java       | +830672<br>0<br>-0 | +830672<br>0<br>-0 | +830672<br>0<br>-0 | —       | +5327<br>825345<br>-0 | +838<br>829834<br>-0 | +0<br>830672<br>-0 | +838<br>829834<br>-0 | +830672<br>0<br>-0 | +0<br>830672<br>-5930 | +5327<br>825345<br>-0 | +0<br>830672<br>-0 |
| Javascript | +825345<br>0<br>-0 | +825345<br>0<br>-0 | +825345<br>0<br>-0 | +0<br>825345<br>-5327 | —          | +0<br>825345<br>-4489 | +0<br>825345<br>-5327 | +0<br>825345<br>-4489 | +825345<br>0<br>-0 | +0<br>825345<br>-11257 | +0<br>825345<br>-0 | +0<br>825345<br>-5327 |
| Obj-C      | +829834<br>0<br>-0 | +829834<br>0<br>-0 | +829834<br>0<br>-0 | +0<br>829834<br>-838 | +4489<br>825345<br>-0 | —       | +0<br>829834<br>-838 | +0<br>829834<br>-0 | +829834<br>0<br>-0 | +0<br>829834<br>-6768 | +4489<br>825345<br>-0 | +0<br>829834<br>-838 |
| Perl       | +830672<br>0<br>-0 | +830672<br>0<br>-0 | +830672<br>0<br>-0 | +0<br>830672<br>-0 | +5327<br>825345<br>-0 | +838<br>829834<br>-0 | —       | +838<br>829834<br>-0 | +830672<br>0<br>-0 | +0<br>830672<br>-5930 | +5327<br>825345<br>-0 | +0<br>830672<br>-0 |
| PHP        | +829834<br>0<br>-0 | +829834<br>0<br>-0 | +829834<br>0<br>-0 | +0<br>829834<br>-838 | +4489<br>825345<br>-0 | +0<br>829834<br>-0 | +0<br>829834<br>-838 | —       | +829834<br>0<br>-0 | +0<br>829834<br>-6768 | +4489<br>825345<br>-0 | +0<br>829834<br>-838 |
| Python     | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-0 | +0<br>0<br>-830672 | +0<br>0<br>-825345 | +0<br>0<br>-829834 | +0<br>0<br>-830672 | +0<br>0<br>-829834 | —       | +0<br>0<br>-836602 | +0<br>0<br>-825345 | +0<br>0<br>-830672 |
| Ruby       | +836602<br>0<br>-0 | +836602<br>0<br>-0 | +836602<br>0<br>-0 | +5930<br>830672<br>-0 | +11257<br>825345<br>-0 | +6768<br>829834<br>-0 | +5930<br>830672<br>-0 | +6768<br>829834<br>-0 | +836602<br>0<br>-0 | —       | +11257<br>825345<br>-0 | +5930<br>830672<br>-0 |
| Rust       | +825345<br>0<br>-0 | +825345<br>0<br>-0 | +825345<br>0<br>-0 | +0<br>825345<br>-5327 | +0<br>825345<br>-0 | +0<br>825345<br>-4489 | +0<br>825345<br>-5327 | +0<br>825345<br>-4489 | +825345<br>0<br>-0 | +0<br>825345<br>-11257 | —       | +0<br>825345<br>-5327 |
| Scala      | +830672<br>0<br>-0 | +830672<br>0<br>-0 | +830672<br>0<br>-0 | +0<br>830672<br>-0 | +5327<br>825345<br>-0 | +838<br>829834<br>-0 | +0<br>830672<br>-0 | +838<br>829834<br>-0 | +830672<br>0<br>-0 | +0<br>830672<br>-5930 | +5327<br>825345<br>-0 | —       |

#### Character Classes - POSIX - Short - Other (`[\p{C}]`)

| Language   | C++     | Go      | Haskell | Java    | Javascript | Obj-C   | Perl    | PHP     | Python  | Ruby    | Rust    | Scala   |
| :--------- | ------: | ------: | ------: | ------: | ---------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| C++        | —       | +0<br>0<br>-137703 | +0<br>0<br>-977459 | +0<br>0<br>-970414 | +0<br>0<br>-965096 | +0<br>0<br>-967530 | +0<br>0<br>-970414 | +0<br>0<br>-967530 | +0<br>0<br>-137703 | +0<br>0<br>-974296 | +0<br>0<br>-963048 | +0<br>0<br>-970414 |
| Go         | +137703<br>0<br>-0 | —       | +16465<br>121238<br>-856221 | +0<br>137703<br>-832711 | +0<br>137703<br>-827393 | +0<br>137703<br>-829827 | +0<br>137703<br>-832711 | +0<br>137703<br>-829827 | +0<br>137703<br>-0 | +0<br>137703<br>-836593 | +0<br>137703<br>-825345 | +0<br>137703<br>-832711 |
| Haskell    | +977459<br>0<br>-0 | +856221<br>121238<br>-16465 | —       | +115849<br>861610<br>-108804 | +120180<br>857279<br>-107817 | +116660<br>860799<br>-106731 | +115849<br>861610<br>-108804 | +116660<br>860799<br>-106731 | +856221<br>121238<br>-16465 | +110907<br>866552<br>-107744 | +120180<br>857279<br>-105769 | +115849<br>861610<br>-108804 |
| Java       | +970414<br>0<br>-0 | +832711<br>137703<br>-0 | +108804<br>861610<br>-115849 | —       | +5318<br>965096<br>-0 | +2884<br>967530<br>-0 | +0<br>970414<br>-0 | +2884<br>967530<br>-0 | +832711<br>137703<br>-0 | +2048<br>968366<br>-5930 | +7366<br>963048<br>-0 | +0<br>970414<br>-0 |
| Javascript | +965096<br>0<br>-0 | +827393<br>137703<br>-0 | +107817<br>857279<br>-120180 | +0<br>965096<br>-5318 | —          | +2048<br>963048<br>-4482 | +0<br>965096<br>-5318 | +2048<br>963048<br>-4482 | +827393<br>137703<br>-0 | +2048<br>963048<br>-11248 | +2048<br>963048<br>-0 | +0<br>965096<br>-5318 |
| Obj-C      | +967530<br>0<br>-0 | +829827<br>137703<br>-0 | +106731<br>860799<br>-116660 | +0<br>967530<br>-2884 | +4482<br>963048<br>-2048 | —       | +0<br>967530<br>-2884 | +0<br>967530<br>-0 | +829827<br>137703<br>-0 | +0<br>967530<br>-6766 | +4482<br>963048<br>-0 | +0<br>967530<br>-2884 |
| Perl       | +970414<br>0<br>-0 | +832711<br>137703<br>-0 | +108804<br>861610<br>-115849 | +0<br>970414<br>-0 | +5318<br>965096<br>-0 | +2884<br>967530<br>-0 | —       | +2884<br>967530<br>-0 | +832711<br>137703<br>-0 | +2048<br>968366<br>-5930 | +7366<br>963048<br>-0 | +0<br>970414<br>-0 |
| PHP        | +967530<br>0<br>-0 | +829827<br>137703<br>-0 | +106731<br>860799<br>-116660 | +0<br>967530<br>-2884 | +4482<br>963048<br>-2048 | +0<br>967530<br>-0 | +0<br>967530<br>-2884 | —       | +829827<br>137703<br>-0 | +0<br>967530<br>-6766 | +4482<br>963048<br>-0 | +0<br>967530<br>-2884 |
| Python     | +137703<br>0<br>-0 | +0<br>137703<br>-0 | +16465<br>121238<br>-856221 | +0<br>137703<br>-832711 | +0<br>137703<br>-827393 | +0<br>137703<br>-829827 | +0<br>137703<br>-832711 | +0<br>137703<br>-829827 | —       | +0<br>137703<br>-836593 | +0<br>137703<br>-825345 | +0<br>137703<br>-832711 |
| Ruby       | +974296<br>0<br>-0 | +836593<br>137703<br>-0 | +107744<br>866552<br>-110907 | +5930<br>968366<br>-2048 | +11248<br>963048<br>-2048 | +6766<br>967530<br>-0 | +5930<br>968366<br>-2048 | +6766<br>967530<br>-0 | +836593<br>137703<br>-0 | —       | +11248<br>963048<br>-0 | +5930<br>968366<br>-2048 |
| Rust       | +963048<br>0<br>-0 | +825345<br>137703<br>-0 | +105769<br>857279<br>-120180 | +0<br>963048<br>-7366 | +0<br>963048<br>-2048 | +0<br>963048<br>-4482 | +0<br>963048<br>-7366 | +0<br>963048<br>-4482 | +825345<br>137703<br>-0 | +0<br>963048<br>-11248 | —       | +0<br>963048<br>-7366 |
| Scala      | +970414<br>0<br>-0 | +832711<br>137703<br>-0 | +108804<br>861610<br>-115849 | +0<br>970414<br>-0 | +5318<br>965096<br>-0 | +2884<br>967530<br>-0 | +0<br>970414<br>-0 | +2884<br>967530<br>-0 | +832711<br>137703<br>-0 | +2048<br>968366<br>-5930 | +7366<br>963048<br>-0 | —       |
