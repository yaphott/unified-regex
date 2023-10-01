# C++

## Tables of Contents

[Go back to the overall results](../)

- [Usage](#usage)
  - [Build](#build)
  - [Run](#run)
  - [Clean up](#clean-up)
- [Match Statistics](#match-statistics)
- [Cardinalities](#cardinalities)
  - [Compare with Go](#compare-with-go)
  - [Compare with Haskell](#compare-with-haskell)
  - [Compare with Java](#compare-with-java)
  - [Compare with Javascript](#compare-with-javascript)
  - [Compare with Obj-C](#compare-with-obj-c)
  - [Compare with Perl](#compare-with-perl)
  - [Compare with PHP](#compare-with-php)
  - [Compare with Python](#compare-with-python)
  - [Compare with Ruby](#compare-with-ruby)
  - [Compare with Rust](#compare-with-rust)
  - [Compare with Scala](#compare-with-scala)

## Usage

### Build

Build the application with the following command:

```bash
g++ main.cpp -o main
```

### Run

Run the application with the following command:

```bash
./main <pattern> <file_path>
```

### Clean up

Clean up the application with the following command:

```bash
rm -f main
```

## Match Statistics

| Category                          | Name                  | Value                         | Total | Percentile (%)<br>(include zero) | Percentile (%)<br>(exclude 0) |
| :-------------------------------- | :-------------------- | :---------------------------- | ----: | -------------: | -------------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 26    | 66.67          | 63.64          |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 26    | 66.67          | 63.64          |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 62    | 66.67          | 63.64          |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 52    | 66.67          | 63.64          |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0     | 16.67          | —              |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 2     | 50.00          | 45.45          |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 33    | 75.00          | 72.73          |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 10    | 66.67          | 63.64          |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 94    | 66.67          | 63.64          |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 95    | 66.67          | 63.64          |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 32    | 66.67          | 63.64          |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 6     | 66.67          | 63.64          |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0     | 16.67          | —              |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 22    | 83.33          | 81.82          |
| Character Classes - Common        | Digit                 | `[\d]`                        | 10    | 66.67          | 66.67          |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 6     | 58.33          | 58.33          |
| Character Classes - Common        | Word Character        | `[\w]`                        | 63    | 66.67          | 66.67          |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0     | 83.33          | —              |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0     | 58.33          | —              |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0     | 58.33          | —              |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0     | 16.67          | —              |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0     | 41.67          | —              |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0     | 75.00          | —              |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0     | 16.67          | —              |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0     | 16.67          | —              |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0     | 16.67          | —              |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0     | 16.67          | —              |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0     | 16.67          | —              |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0     | 16.67          | —              |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0     | 16.67          | —              |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0     | 16.67          | —              |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0     | 8.33           | —              |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0     | 66.67          | —              |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0     | 16.67          | —              |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0     | 33.33          | —              |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0     | 8.33           | —              |

## Cardinalities

### Compare with [Go](../go)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 128     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 32     | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 63      |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 0      | 1831    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 0      | 2233    |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 0      | 31      |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 0      | 397     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 0      | 131612  |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 0      | 136104  |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 0      | 1985    |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 0      | 452     |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 0      | 13      |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 0      | 2450    |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 0      | 680     |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 0      | 236     |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 0      | 915     |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 0      | 1831    |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 0      | 26      |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 0      | 79      |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 0      | 77      |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 0      | 12      |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 0      | 628     |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 0      | 842     |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 0      | 948     |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 0      | 63      |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 0      | 125     |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 0      | 8682    |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 0      | 9818    |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 0      | 17      |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 0      | 19      |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 0      | 65      |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 0      | 170     |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 0      | 137468  |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 0      | 137703  |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 1      | 5      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0      | 0      | 0       |

### Compare with [Haskell](../haskell)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 127     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 1      | 32     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 32     | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 63      |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 0      | 1818    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 0      | 1112183 |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 1113973 |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 0      | 99104   |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 0      | 1113975 |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 0      | 281336  |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 0      | 281346  |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 0      | 3       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 0      | 3       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 0      | 50323   |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 0      | 50323   |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 0      | 238498  |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 0      | 322790  |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 0      | 99172   |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 0      | 192137  |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 0      | 192138  |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 0      | 192136  |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 0      | 572995  |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 0      | 50324   |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 0      | 50324   |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 0      | 964576  |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 0      | 50323   |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 0      | 977459  |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0      | 0      | 0       |

### Compare with [Java](../java)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 26     | 0      | 5       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 21     | 5      | 1       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 57     | 5      | 1       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 48     | 4      | 1       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 5       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 2      | 0      | 6       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 33     | 0      | 6       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 10     | 0      | 5       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 88     | 6      | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 89     | 6      | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 31     | 1      | 5       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 6      | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 5       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 21     | 1      | 5       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 0      | 1791    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 0      | 2155    |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 0      | 31      |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 3977    |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 0      | 260     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 0      | 127004  |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 0      | 131241  |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 0      | 1839    |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 0      | 443     |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 0      | 13      |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 0      | 2295    |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 0      | 650     |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 0      | 236     |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 0      | 895     |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 0      | 1781    |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 0      | 25      |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 0      | 75      |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 0      | 73      |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 0      | 12      |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 0      | 593     |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 0      | 798     |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 0      | 948     |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 0      | 62      |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 0      | 123     |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 0      | 6431    |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 0      | 7564    |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 0      | 17      |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 0      | 19      |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 0      | 65      |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 0      | 161     |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 2048    |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 0      | 137468  |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 0      | 830672  |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 0      | 970414  |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0      | 0      | 0       |

### Compare with [Javascript](../javascript)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 26     | 0      | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 26     | 0      | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 62     | 0      | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 52     | 0      | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 2      | 0      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 33     | 0      | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 10     | 0      | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 94     | 0      | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 95     | 0      | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 32     | 0      | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 6      | 0      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 22     | 0      | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 0      | 1831    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 0      | 2233    |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 0      | 31      |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 4095    |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 0      | 397     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 0      | 131612  |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 0      | 136104  |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 0      | 1985    |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 0      | 452     |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 0      | 13      |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 0      | 2450    |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 0      | 680     |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 0      | 236     |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 0      | 915     |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 0      | 1831    |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 0      | 26      |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 0      | 79      |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 0      | 77      |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 0      | 12      |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 0      | 628     |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 0      | 842     |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 0      | 948     |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 0      | 63      |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 0      | 125     |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 0      | 6634    |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 0      | 7770    |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 0      | 17      |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 0      | 19      |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 0      | 65      |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 0      | 170     |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 2048    |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 0      | 137468  |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 0      | 825345  |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 0      | 965096  |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 19      |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 0      | 1831    |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 0      | 2233    |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 0      | 31      |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 0      | 4095    |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 0      | 397     |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 0      | 131612  |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 0      | 136104  |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 0      | 1985    |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 0      | 452     |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 0      | 13      |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 0      | 2450    |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 0      | 680     |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 0      | 236     |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 0      | 915     |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 0      | 1831    |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 0      | 10      |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 0      | 26      |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 0      | 79      |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 0      | 77      |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 0      | 12      |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 0      | 10      |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 0      | 628     |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 0      | 842     |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 0      | 948     |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 0      | 63      |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 0      | 125     |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 0      | 6634    |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 0      | 7770    |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 0      | 17      |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 0      | 1       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 0      | 1       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 0      | 19      |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 0      | 65      |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 0      | 170     |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 2048    |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 0      | 137468  |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 0      | 825345  |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0      | 0      | 965096  |

### Compare with [Obj-C](../objc)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 26     | 1925    |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 26     | 2445    |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 62     | 133994  |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 52     | 133344  |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 128     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 2      | 16      |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 33     | 32      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 10     | 650     |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 94     | 282052  |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 95     | 282068  |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 9      | 23     | 796     |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 6      | 19      |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 135202  |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 662     |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 0      | 1831    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 0      | 2227    |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 0      | 31      |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 4089    |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 0      | 334     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 0      | 127333  |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 0      | 131756  |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 0      | 1950    |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 0      | 445     |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 0      | 13      |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 0      | 2408    |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 0      | 660     |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 0      | 236     |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 0      | 895     |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 0      | 1791    |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 0      | 26      |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 0      | 79      |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 0      | 77      |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 0      | 12      |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 0      | 605     |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 0      | 819     |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 0      | 948     |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 0      | 63      |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 0      | 125     |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 0      | 6605    |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 0      | 7741    |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 0      | 17      |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 0      | 19      |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 0      | 65      |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 0      | 163     |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 0      | 137468  |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 0      | 829834  |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 0      | 967530  |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 650     |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 19      |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 135139  |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 0      | 1831    |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 0      | 2227    |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 0      | 31      |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 0      | 4089    |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 0      | 334     |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 0      | 127333  |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 0      | 131756  |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 0      | 1950    |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 0      | 445     |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 0      | 13      |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 0      | 2408    |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 0      | 660     |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 0      | 236     |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 0      | 895     |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 0      | 1791    |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 0      | 10      |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 0      | 26      |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 0      | 79      |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 0      | 77      |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 0      | 12      |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 0      | 10      |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 0      | 605     |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 0      | 819     |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 0      | 948     |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 0      | 63      |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 0      | 125     |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 0      | 6605    |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 0      | 7741    |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 0      | 17      |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 0      | 1       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 0      | 1       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 0      | 19      |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 0      | 65      |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 0      | 163     |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 0      | 137468  |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 0      | 829834  |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0      | 0      | 967530  |

### Compare with [Perl](../perl)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 26     | 1855    |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 26     | 2283    |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 62     | 133398  |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 52     | 132758  |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 128     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 2      | 15      |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 10     | 640     |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 94     | 281119  |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 95     | 281134  |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 32     | 768     |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 6      | 17      |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 134499  |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 22      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 0      | 1791    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 0      | 2155    |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 0      | 31      |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 3977    |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 3977    |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 0      | 260     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 0      | 127004  |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 0      | 131241  |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 0      | 1839    |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 0      | 443     |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 0      | 13      |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 0      | 2295    |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 0      | 650     |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 0      | 236     |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 0      | 895     |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 0      | 1781    |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 0      | 25      |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 0      | 75      |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 0      | 73      |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 0      | 12      |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 0      | 593     |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 0      | 798     |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 0      | 948     |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 0      | 62      |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 0      | 123     |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 0      | 6431    |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 0      | 7564    |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 0      | 17      |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 0      | 19      |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 0      | 65      |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 0      | 161     |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 2048    |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 0      | 137468  |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 0      | 830672  |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 0      | 970414  |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 640     |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 17      |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 134436  |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 0      | 1791    |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 0      | 2155    |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 0      | 31      |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 0      | 3977    |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 0      | 260     |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 0      | 127004  |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 0      | 131241  |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 0      | 1839    |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 0      | 443     |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 0      | 13      |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 0      | 2295    |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 0      | 650     |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 0      | 236     |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 0      | 895     |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 0      | 1781    |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 0      | 10      |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 0      | 25      |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 0      | 75      |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 0      | 73      |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 0      | 12      |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 0      | 10      |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 0      | 593     |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 0      | 798     |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 0      | 948     |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 0      | 62      |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 0      | 123     |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 0      | 6431    |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 0      | 7564    |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 0      | 17      |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 0      | 1       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 0      | 1       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 0      | 19      |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 0      | 65      |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 0      | 161     |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 2048    |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 0      | 137468  |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 0      | 830672  |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0      | 0      | 970414  |

### Compare with [PHP](../php)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 26     | 1805    |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 26     | 2201    |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 62     | 133485  |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 52     | 131704  |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 128     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 2      | 17      |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 33     | 32      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 10     | 650     |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 94     | 144578  |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 95     | 144595  |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 32     | 796     |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 6      | 20      |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 133548  |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 0      | 1831    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 0      | 2227    |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 0      | 31      |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 4089    |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 0      | 334     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 0      | 127333  |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 0      | 131756  |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 0      | 1950    |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 0      | 445     |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 0      | 13      |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 0      | 2408    |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 0      | 660     |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 0      | 236     |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 0      | 895     |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 0      | 1791    |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 0      | 26      |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 0      | 79      |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 0      | 77      |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 0      | 12      |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 0      | 605     |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 0      | 819     |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 0      | 948     |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 0      | 63      |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 0      | 125     |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 0      | 6605    |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 0      | 7741    |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 0      | 17      |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 0      | 19      |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 0      | 65      |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 0      | 163     |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 0      | 137468  |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 0      | 829834  |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 0      | 967530  |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 650     |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 20      |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 133485  |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0      | 0      | 0       |

### Compare with [Python](../python)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 128     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 32     | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 63      |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 0      | 1831    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 0      | 2233    |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 0      | 31      |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 0      | 397     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 0      | 131612  |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 0      | 136104  |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 0      | 1985    |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 0      | 452     |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 0      | 13      |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 0      | 2450    |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 0      | 680     |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 0      | 236     |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 0      | 915     |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 0      | 1831    |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 0      | 26      |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 0      | 79      |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 0      | 77      |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 0      | 12      |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 0      | 628     |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 0      | 842     |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 0      | 948     |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 0      | 63      |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 0      | 125     |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 0      | 6634    |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 0      | 7770    |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 0      | 17      |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 0      | 19      |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 0      | 65      |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 0      | 170     |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 0      | 137468  |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 0      | 137703  |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 1      | 5      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0      | 0      | 0       |

### Compare with [Ruby](../ruby)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 26     | 1882    |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 26     | 2314    |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 62     | 127824  |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 52     | 127204  |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 128     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 2      | 16      |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 33     | 32      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 10     | 620     |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 94     | 275284  |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 95     | 275300  |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 32     | 769     |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 6      | 19      |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 128917  |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 0      | 1788    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 0      | 2151    |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 0      | 31      |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 3970    |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 0      | 259     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 0      | 121414  |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 0      | 125643  |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 0      | 1826    |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 0      | 429     |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 0      | 13      |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 0      | 2268    |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 0      | 630     |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 0      | 236     |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 0      | 888     |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 0      | 1754    |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 0      | 24      |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 0      | 75      |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 0      | 73      |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 0      | 12      |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 0      | 588     |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 0      | 792     |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 0      | 948     |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 0      | 62      |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 0      | 121     |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 0      | 6161    |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 0      | 7292    |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 0      | 17      |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 0      | 19      |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 0      | 65      |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 0      | 161     |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 0      | 137468  |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 0      | 836602  |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 0      | 974296  |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 0      | 1788    |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 0      | 2151    |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 0      | 31      |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 0      | 3970    |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 0      | 259     |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 0      | 121414  |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 0      | 125643  |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 0      | 1826    |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 0      | 429     |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 0      | 13      |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 0      | 2268    |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 0      | 630     |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 0      | 236     |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 0      | 888     |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 0      | 1754    |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 0      | 10      |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 0      | 24      |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 0      | 75      |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 0      | 73      |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 0      | 12      |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 0      | 10      |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 0      | 588     |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 0      | 792     |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 0      | 948     |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 0      | 62      |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 0      | 121     |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 0      | 6161    |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 0      | 7292    |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 0      | 17      |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 0      | 1       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 0      | 1       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 0      | 19      |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 0      | 65      |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 0      | 161     |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 0      | 137468  |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 0      | 836602  |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0      | 0      | 974296  |

### Compare with [Rust](../rust)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 128     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 32     | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 63      |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 0      | 1831    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 0      | 2233    |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 0      | 31      |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 4095    |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 0      | 397     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 0      | 131612  |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 0      | 136104  |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 0      | 1985    |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 0      | 452     |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 0      | 13      |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 0      | 2450    |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 0      | 680     |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 0      | 236     |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 0      | 915     |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 0      | 1831    |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 0      | 26      |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 0      | 79      |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 0      | 77      |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 0      | 12      |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 0      | 628     |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 0      | 842     |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 0      | 948     |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 0      | 63      |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 0      | 125     |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 0      | 6634    |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 0      | 7770    |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 0      | 17      |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 0      | 19      |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 0      | 65      |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 0      | 170     |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 0      | 137468  |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 0      | 825345  |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 0      | 963048  |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 670     |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 19      |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 139549  |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 0      | 1831    |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 0      | 2233    |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 0      | 31      |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 0      | 4095    |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 0      | 397     |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 0      | 131612  |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 0      | 136104  |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 0      | 1985    |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 0      | 452     |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 0      | 13      |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 0      | 2450    |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 0      | 680     |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 0      | 236     |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 0      | 915     |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 0      | 1831    |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 0      | 10      |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 0      | 26      |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 0      | 79      |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 0      | 77      |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 0      | 12      |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 0      | 10      |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 0      | 628     |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 0      | 842     |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 0      | 948     |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 0      | 63      |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 0      | 125     |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 0      | 6634    |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 0      | 7770    |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 0      | 17      |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 0      | 1       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 0      | 1       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 0      | 19      |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 0      | 65      |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 0      | 170     |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 0      | 137468  |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 0      | 825345  |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0      | 0      | 963048  |

### Compare with [Scala](../scala)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 26     | 0      | 5       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 21     | 5      | 1       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 57     | 5      | 1       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 48     | 4      | 1       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 5       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 2      | 0      | 6       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 33     | 0      | 6       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 10     | 0      | 5       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 88     | 6      | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 89     | 6      | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 31     | 1      | 5       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 6      | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 5       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 21     | 1      | 5       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 0      | 1791    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 0      | 2155    |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 0      | 31      |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 3977    |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 0      | 260     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 0      | 127004  |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 0      | 131241  |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 0      | 1839    |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 0      | 443     |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 0      | 13      |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 0      | 2295    |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 0      | 650     |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 0      | 236     |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 0      | 895     |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 0      | 1781    |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 0      | 25      |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 0      | 75      |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 0      | 73      |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 0      | 12      |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 0      | 10      |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 0      | 593     |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 0      | 798     |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 0      | 948     |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 0      | 62      |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 0      | 123     |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 0      | 6431    |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 0      | 7564    |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 0      | 17      |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 0      | 1       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 0      | 19      |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 0      | 65      |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 0      | 161     |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 2048    |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 0      | 137468  |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 0      | 830672  |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 0      | 970414  |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0      | 0      | 0       |

