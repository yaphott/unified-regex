# Javascript

## Tables of Contents

[Go back to the overall results](../)

- [Usage](#usage)
  - [Run](#run)
- [Match Statistics](#match-statistics)
- [Cardinalities](#cardinalities)
  - [Compare with C++](#compare-with-c)
  - [Compare with Go](#compare-with-go)
  - [Compare with Haskell](#compare-with-haskell)
  - [Compare with Java](#compare-with-java)
  - [Compare with Obj-C](#compare-with-obj-c)
  - [Compare with Perl](#compare-with-perl)
  - [Compare with PHP](#compare-with-php)
  - [Compare with Python](#compare-with-python)
  - [Compare with Ruby](#compare-with-ruby)
  - [Compare with Rust](#compare-with-rust)
  - [Compare with Scala](#compare-with-scala)

## Usage

### Run

Run the application with the following command:

```bash
node main.js <pattern> <file_path>
```

## Match Statistics

| Category                          | Name                  | Value                         | Total  | Percentile (%)<br>(include zero) | Percentile (%)<br>(exclude 0) |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -------------: | -------------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 8.33           | —              |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 8.33           | —              |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 8.33           | —              |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 8.33           | —              |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 16.67          | —              |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 8.33           | —              |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 8.33           | —              |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 8.33           | —              |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 8.33           | —              |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 8.33           | —              |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 8.33           | —              |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 8.33           | —              |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 16.67          | —              |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 8.33           | —              |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 1831   | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 2233   | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 31     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 4095   | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 75.00          | —              |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 397    | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 131612 | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 136104 | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1985   | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 452    | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 13     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 2450   | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 680    | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 236    | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 915    | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 1831   | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 10     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 26     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 79     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 77     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 12     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 10     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 628    | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 842    | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 948    | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 63     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 125    | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 6634   | 83.33          | 81.82          |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 7770   | 83.33          | 81.82          |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 17     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 1      | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 1      | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 19     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 65     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 170    | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 137468 | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 825345 | 50.00          | 25.00          |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 965096 | 41.67          | 36.36          |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2233   | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4095   | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 397    | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 131612 | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 136104 | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1985   | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 452    | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2450   | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 680    | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 915    | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1831   | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 628    | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 842    | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6634   | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7770   | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 170    | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 2048   | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 825345 | 75.00          | 40.00          |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 965096 | 75.00          | 40.00          |

## Cardinalities

### Compare with [C++](../c++)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 0      | 26      |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 0      | 26      |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 0      | 62      |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 0      | 52      |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 0      | 2       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 0      | 33      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 0      | 10      |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 0      | 94      |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 0      | 95      |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 0      | 32      |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 0      | 22      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 1831   | 0      | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 2233   | 0      | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 31     | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 4095   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 397    | 0      | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 131612 | 0      | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 136104 | 0      | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1985   | 0      | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 452    | 0      | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 13     | 0      | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 2450   | 0      | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 680    | 0      | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 236    | 0      | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 915    | 0      | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 1831   | 0      | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 10     | 0      | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 26     | 0      | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 79     | 0      | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 77     | 0      | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 12     | 0      | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 10     | 0      | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 628    | 0      | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 842    | 0      | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 948    | 0      | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 63     | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 125    | 0      | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 6634   | 0      | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 7770   | 0      | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 17     | 0      | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 19     | 0      | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 65     | 0      | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 170    | 0      | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 137468 | 0      | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 825345 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 965096 | 0      | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2233   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4095   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 397    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 131612 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 136104 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1985   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 452    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2450   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 680    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 915    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 628    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 842    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6634   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7770   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 170    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 2048   | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 825345 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 965096 | 0      | 0       |

### Compare with [Go](../go)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 0      | 26      |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 0      | 26      |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 0      | 62      |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 0      | 52      |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 128     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 0      | 2       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 0      | 33      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 0      | 10      |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 0      | 94      |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 0      | 95      |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 0      | 32      |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 63      |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 0      | 22      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2233   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 4095   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 397    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 131612 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 136104 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 1985   | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 452    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2450   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 680    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 915    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 26     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 79     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 77     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 628    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 842    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 63     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 125    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6634   | 2048    |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7770   | 2048    |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 170    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 825345 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 827393 | 137703 | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2233   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4095   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 397    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 131612 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 136104 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1985   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 452    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2450   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 680    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 915    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 628    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 842    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6634   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7770   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 170    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 2048   | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 825345 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 965096 | 0      | 0       |

### Compare with [Haskell](../haskell)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 0      | 26      |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 0      | 26      |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 0      | 62      |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 0      | 52      |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 127     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 0      | 2       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 0      | 32      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 0      | 10      |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 0      | 94      |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 0      | 95      |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 0      | 32      |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 63      |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 0      | 22      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 1363   | 468    | 1350    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 531    | 1702   | 1110481 |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 31     | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 4095   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 1113973 |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 397    | 0      | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 119852 | 11760  | 87344   |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 30     | 136074 | 977901  |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1985   | 0      | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 452    | 0      | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 13     | 0      | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 2450   | 0      | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 670    | 10     | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 236    | 0      | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 710    | 205    | 281131  |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 1508   | 323    | 281023  |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 9      | 1      | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 25     | 1      | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 76     | 3      | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 74     | 3      | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 11     | 1      | 50322   |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 9      | 1      | 50322   |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 537    | 91     | 238407  |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 689    | 153    | 322637  |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 894    | 54     | 99118   |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 53     | 10     | 192127  |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 109    | 16     | 192122  |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 5913   | 721    | 191415  |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 4896   | 2874   | 570121  |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 15     | 2      | 50322   |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 17     | 2      | 50322   |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 1      | 64     | 964512  |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 165    | 5      | 50318   |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 137468 | 0      | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 825345 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 107817 | 857279 | 120180  |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2233   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4095   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 397    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 131612 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 136104 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1985   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 452    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2450   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 680    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 915    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 628    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 842    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6634   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7770   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 170    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 2048   | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 825345 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 965096 | 0      | 0       |

### Compare with [Java](../java)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 0      | 5       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 0      | 5       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 5       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 0      | 5       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 5       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 0      | 6       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 40     | 1791   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 78     | 2155   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 118    | 3977   | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 137    | 260    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 4608   | 127004 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 4863   | 131241 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 147    | 1838   | 1       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 9      | 443    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 155    | 2295   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 30     | 650    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 20     | 895    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 50     | 1781   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 1      | 25     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 4      | 75     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 4      | 73     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 35     | 593    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 44     | 798    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 1      | 62     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 2      | 123    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 203    | 6431   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 206    | 7564   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 9      | 161    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 2048   | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 825345 | 5327    |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 965096 | 5318    |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2233   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4095   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 397    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 131612 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 136104 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1985   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 452    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2450   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 680    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 915    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 628    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 842    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6634   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7770   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 170    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 2048   | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 825345 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 965096 | 0      | 0       |

### Compare with [Obj-C](../objc)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 0      | 1951    |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 0      | 2471    |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 0      | 134056  |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 0      | 133396  |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 128     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 0      | 18      |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 0      | 65      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 0      | 660     |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 0      | 282146  |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 0      | 282163  |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 0      | 819     |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 0      | 25      |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 135202  |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 0      | 684     |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 6      | 2227   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 6      | 4089   | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 63     | 334    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 4279   | 127333 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 4348   | 131756 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 35     | 1950   | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 7      | 445    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 42     | 2408   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 20     | 660    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 20     | 895    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 40     | 1791   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 26     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 79     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 77     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 23     | 605    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 23     | 819    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 63     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 125    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 29     | 6605   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 29     | 7741   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 7      | 163    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 825345 | 4489    |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 2048   | 963048 | 4482    |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 1831   | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 6      | 2227   | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 31     | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 6      | 4089   | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 63     | 334    | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 4279   | 127333 | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 4348   | 131756 | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 35     | 1950   | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 7      | 445    | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 13     | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 42     | 2408   | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 20     | 660    | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 236    | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 20     | 895    | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 40     | 1791   | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 26     | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 79     | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 77     | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 12     | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 23     | 605    | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 23     | 819    | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 948    | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 125    | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 29     | 6605   | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 29     | 7741   | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 17     | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 19     | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 65     | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 7      | 163    | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 2048   | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 137468 | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 825345 | 4489    |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 2048   | 963048 | 4482    |

### Compare with [Perl](../perl)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 0      | 1881    |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 0      | 2309    |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 0      | 133460  |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 0      | 132810  |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 128     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 0      | 17      |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 0      | 33      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 0      | 650     |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 0      | 281213  |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 0      | 281229  |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 0      | 800     |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 0      | 23      |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 134499  |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 0      | 44      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 40     | 1791   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 78     | 2155   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 118    | 3977   | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 3977    |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 137    | 260    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 4608   | 127004 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 4863   | 131241 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 147    | 1838   | 1       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 9      | 443    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 155    | 2295   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 30     | 650    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 20     | 895    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 50     | 1781   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 1      | 25     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 4      | 75     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 4      | 73     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 35     | 593    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 44     | 798    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 1      | 62     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 2      | 123    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 203    | 6431   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 206    | 7564   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 9      | 161    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 2048   | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 825345 | 5327    |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 965096 | 5318    |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 40     | 1791   | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 78     | 2155   | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 31     | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 118    | 3977   | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 137    | 260    | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 4608   | 127004 | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 4863   | 131241 | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 147    | 1838   | 1       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 9      | 443    | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 13     | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 155    | 2295   | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 30     | 650    | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 236    | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 20     | 895    | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 50     | 1781   | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 1      | 25     | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 4      | 75     | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 4      | 73     | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 12     | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 35     | 593    | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 44     | 798    | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 948    | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 1      | 62     | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 2      | 123    | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 203    | 6431   | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 206    | 7564   | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 17     | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 19     | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 65     | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 9      | 161    | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 2048   | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 137468 | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 825345 | 5327    |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0      | 965096 | 5318    |

### Compare with [PHP](../php)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 0      | 1831    |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 0      | 2227    |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 0      | 133547  |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 0      | 131756  |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 128     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 0      | 19      |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 0      | 65      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 0      | 660     |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 0      | 144672  |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 0      | 144690  |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 0      | 828     |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 0      | 26      |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 133548  |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 0      | 22      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 6      | 2227   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 4095   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 4089    |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 63     | 334    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 4279   | 127333 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 4348   | 131756 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 35     | 1950   | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 7      | 445    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 42     | 2408   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 20     | 660    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 20     | 895    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 40     | 1791   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 26     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 79     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 77     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 23     | 605    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 23     | 819    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 63     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 125    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 29     | 6605   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 29     | 7741   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 7      | 163    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 825345 | 4489    |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 2048   | 963048 | 4482    |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2233   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4095   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 397    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 131612 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 136104 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1985   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 452    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2450   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 680    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 915    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 628    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 842    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6634   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7770   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 170    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 2048   | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 825345 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 965096 | 0      | 0       |

### Compare with [Python](../python)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 0      | 26      |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 0      | 26      |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 0      | 62      |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 0      | 52      |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 128     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 0      | 2       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 0      | 33      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 0      | 10      |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 0      | 94      |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 0      | 95      |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 0      | 32      |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 63      |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 0      | 22      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2233   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 4095   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 397    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 131612 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 136104 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 1985   | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 452    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2450   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 680    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 915    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 26     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 79     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 77     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 628    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 842    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 63     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 125    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6634   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7770   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 170    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 825345 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 827393 | 137703 | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2233   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4095   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 397    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 131612 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 136104 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1985   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 452    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2450   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 680    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 915    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 628    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 842    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6634   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7770   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 170    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 2048   | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 825345 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 965096 | 0      | 0       |

### Compare with [Ruby](../ruby)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 0      | 1908    |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 0      | 2340    |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 0      | 127886  |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 0      | 127256  |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 128     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 0      | 18      |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 0      | 65      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 0      | 630     |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 0      | 275378  |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 0      | 275395  |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 0      | 801     |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 0      | 25      |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 128917  |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 0      | 22      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 43     | 1788   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 82     | 2151   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 125    | 3970   | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 138    | 259    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 10198  | 121414 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 10461  | 125643 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 160    | 1825   | 1       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 23     | 429    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 182    | 2268   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 50     | 630    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 27     | 888    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 77     | 1754   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 2      | 24     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 4      | 75     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 4      | 73     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 40     | 588    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 50     | 792    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 1      | 62     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 4      | 121    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 473    | 6161   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 478    | 7292   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 9      | 161    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 825345 | 11257   |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 2048   | 963048 | 11248   |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 43     | 1788   | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 82     | 2151   | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 31     | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 125    | 3970   | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 138    | 259    | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 10198  | 121414 | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 10461  | 125643 | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 160    | 1825   | 1       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 23     | 429    | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 13     | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 182    | 2268   | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 50     | 630    | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 236    | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 27     | 888    | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 77     | 1754   | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 2      | 24     | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 4      | 75     | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 4      | 73     | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 12     | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 40     | 588    | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 50     | 792    | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 948    | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 1      | 62     | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 4      | 121    | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 473    | 6161   | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 478    | 7292   | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 17     | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 19     | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 65     | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 9      | 161    | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 2048   | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 137468 | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 825345 | 11257   |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 2048   | 963048 | 11248   |

### Compare with [Rust](../rust)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 0      | 26      |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 0      | 26      |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 0      | 62      |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 0      | 52      |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 128     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 0      | 2       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 0      | 33      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 0      | 10      |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 0      | 94      |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 0      | 95      |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 0      | 32      |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 63      |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 0      | 22      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2233   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 4095   | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 397    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 131612 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 136104 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 1985   | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 452    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2450   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 680    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 915    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 26     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 79     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 77     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 628    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 842    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 63     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 125    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6634   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7770   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 170    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 825345 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 2048   | 963048 | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 1831   | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 2233   | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 31     | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 4095   | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 397    | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 131612 | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 136104 | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 1985   | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 452    | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 13     | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 2450   | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 680    | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 236    | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 915    | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 1831   | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 26     | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 79     | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 77     | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 12     | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 628    | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 842    | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 948    | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 125    | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 6634   | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 7770   | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 17     | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 19     | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 65     | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 170    | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 2048   | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 137468 | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 825345 | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 2048   | 963048 | 0       |

### Compare with [Scala](../scala)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 0      | 5       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 0      | 5       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 0      | 5       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 0      | 5       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 0      | 5       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 0      | 6       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 40     | 1791   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 78     | 2155   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 118    | 3977   | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 137    | 260    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 4608   | 127004 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 4863   | 131241 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 147    | 1838   | 1       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 9      | 443    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 155    | 2295   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 30     | 650    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 20     | 895    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 50     | 1781   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 1      | 25     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 4      | 75     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 4      | 73     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 35     | 593    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 44     | 798    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 1      | 62     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 2      | 123    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 203    | 6431   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 206    | 7564   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 9      | 161    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 2048   | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 825345 | 5327    |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 965096 | 5318    |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2233   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4095   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 397    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 131612 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 136104 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1985   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 452    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2450   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 680    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 915    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 628    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 842    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6634   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7770   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 170    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 2048   | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 825345 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 965096 | 0      | 0       |

