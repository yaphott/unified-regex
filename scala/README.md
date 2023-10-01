# Scala

## Tables of Contents

[Go back to the overall results](../)

- [Usage](#usage)
  - [Run](#run)
  - [Clean up](#clean-up)
- [Match Statistics](#match-statistics)
- [Cardinalities](#cardinalities)
  - [Compare with C++](#compare-with-c)
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

## Usage

### Run

Run the application with the following command:

```bash
sbt "run <pattern> <file_path>"
```

### Clean up

Clean up the application with the following command:

```bash
rm -rf target
```

## Match Statistics

| Category                          | Name                  | Value                         | Total  | Percentile (%)<br>(include zero) | Percentile (%)<br>(exclude 0) |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -------------: | -------------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 5      | 25.00          | 18.18          |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 6      | 25.00          | 18.18          |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 6      | 25.00          | 18.18          |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 5      | 25.00          | 18.18          |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 5      | 33.33          | 20.00          |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 6      | 66.67          | 63.64          |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 6      | 25.00          | 18.18          |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 5      | 25.00          | 18.18          |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 6      | 25.00          | 18.18          |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 6      | 25.00          | 18.18          |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 6      | 25.00          | 18.18          |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 6      | 66.67          | 63.64          |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 5      | 33.33          | 20.00          |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 6      | 25.00          | 18.18          |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 1791   | 41.67          | 36.36          |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 2155   | 41.67          | 36.36          |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 31     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 3977   | 75.00          | 57.14          |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 75.00          | —              |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 260    | 50.00          | 40.00          |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 127004 | 50.00          | 45.45          |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 131241 | 41.67          | 36.36          |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1839   | 50.00          | 40.00          |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 443    | 50.00          | 40.00          |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 13     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 2295   | 50.00          | 40.00          |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 650    | 50.00          | 45.45          |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 236    | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 895    | 58.33          | 54.55          |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 1781   | 41.67          | 36.36          |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 10     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 25     | 50.00          | 45.45          |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 75     | 50.00          | 45.45          |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 73     | 50.00          | 45.45          |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 12     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 10     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 593    | 41.67          | 36.36          |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 798    | 41.67          | 36.36          |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 948    | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 62     | 41.67          | 36.36          |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 123    | 41.67          | 36.36          |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 6431   | 41.67          | 36.36          |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 7564   | 41.67          | 36.36          |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 17     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 1      | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 1      | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 19     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 65     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 161    | 41.67          | 36.36          |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 137468 | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 830672 | 91.67          | 87.50          |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 970414 | 83.33          | 81.82          |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 83.33          | —              |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 58.33          | —              |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0      | 58.33          | —              |

## Cardinalities

### Compare with [C++](../c++)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 5      | 0      | 26      |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 1      | 5      | 21      |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 1      | 5      | 57      |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 1      | 4      | 48      |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 5      | 0      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 6      | 0      | 2       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 6      | 0      | 33      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 5      | 0      | 10      |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 6      | 88      |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 6      | 89      |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 5      | 1      | 31      |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 6      | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 5      | 0      | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 5      | 1      | 21      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 1791   | 0      | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 2155   | 0      | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 31     | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 3977   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 260    | 0      | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 127004 | 0      | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 131241 | 0      | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1839   | 0      | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 443    | 0      | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 13     | 0      | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 2295   | 0      | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 650    | 0      | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 236    | 0      | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 895    | 0      | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 1781   | 0      | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 10     | 0      | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 25     | 0      | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 75     | 0      | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 73     | 0      | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 12     | 0      | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 10     | 0      | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 593    | 0      | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 798    | 0      | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 948    | 0      | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 62     | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 123    | 0      | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 6431   | 0      | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 7564   | 0      | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 17     | 0      | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 19     | 0      | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 65     | 0      | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 161    | 0      | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 137468 | 0      | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 830672 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 970414 | 0      | 0       |
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

### Compare with [Go](../go)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 5      | 0      | 26      |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 1      | 5      | 21      |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 1      | 5      | 57      |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 1      | 4      | 48      |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 5      | 123     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 6      | 0      | 2       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 6      | 0      | 33      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 5      | 0      | 10      |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 6      | 88      |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 6      | 89      |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 5      | 1      | 31      |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 6      | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 1      | 4      | 59      |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 5      | 1      | 21      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1791   | 40      |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2155   | 78      |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 3977   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 260    | 137     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 127004 | 4608    |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 131241 | 4863    |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1      | 1838   | 147     |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 443    | 9       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2295   | 155     |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 650    | 30      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 20      |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1781   | 50      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 25     | 1       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 4       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 4       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 593    | 35      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 798    | 44      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 1       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 123    | 2       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6431   | 2251    |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7564   | 2254    |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 9       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 830672 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 832711 | 137703 | 0       |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 5      | 0      | 26      |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 1      | 5      | 21      |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 1      | 5      | 57      |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 1      | 4      | 48      |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 5      | 122     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 6      | 0      | 2       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 6      | 0      | 32      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 5      | 0      | 10      |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 6      | 88      |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 6      | 89      |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 5      | 1      | 31      |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 6      | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 1      | 4      | 59      |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 5      | 1      | 21      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 1323   | 468    | 1350    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 531    | 1624   | 1110559 |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 31     | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 3977   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 1113973 |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 260    | 0      | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 115591 | 11413  | 87691   |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 30     | 131211 | 982764  |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1839   | 0      | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 443    | 0      | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 13     | 0      | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 2295   | 0      | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 640    | 10     | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 236    | 0      | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 690    | 205    | 281131  |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 1471   | 310    | 281036  |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 9      | 1      | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 24     | 1      | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 72     | 3      | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 70     | 3      | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 11     | 1      | 50322   |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 9      | 1      | 50322   |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 504    | 89     | 238409  |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 647    | 151    | 322639  |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 894    | 54     | 99118   |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 52     | 10     | 192127  |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 108    | 15     | 192123  |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 5729   | 702    | 191434  |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 4744   | 2820   | 570175  |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 15     | 2      | 50322   |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 17     | 2      | 50322   |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 1      | 64     | 964512  |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 156    | 5      | 50318   |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 137468 | 0      | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 830672 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 108804 | 861610 | 115849  |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 5      | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 6      | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 6      | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 5      | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 5      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 6      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 6      | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 5      | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 6      | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 6      | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 6      | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 5      | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 6      | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1791   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2155   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 3977   | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 260    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 127004 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 131241 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 1839   | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 443    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2295   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 650    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1781   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 25     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 593    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 798    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 123    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6431   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7564   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 2048   | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 830672 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 970414 | 0       |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 5      | 0      | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 6      | 0      | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 6      | 0      | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 5      | 0      | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 5      | 0      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 6      | 0      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 6      | 0      | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 5      | 0      | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 6      | 0      | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 6      | 0      | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 6      | 0      | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 6      | 0      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 5      | 0      | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 6      | 0      | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1791   | 40      |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2155   | 78      |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 3977   | 118     |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 260    | 137     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 127004 | 4608    |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 131241 | 4863    |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1      | 1838   | 147     |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 443    | 9       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2295   | 155     |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 650    | 30      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 20      |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1781   | 50      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 25     | 1       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 4       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 4       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 593    | 35      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 798    | 44      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 1       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 123    | 2       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6431   | 203     |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7564   | 206     |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 9       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 2048   | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 5327   | 825345 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 5318   | 965096 | 0       |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 5      | 0      | 1951    |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 1      | 5      | 2466    |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 1      | 5      | 134051  |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 1      | 4      | 133392  |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 5      | 123     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 6      | 0      | 18      |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 6      | 0      | 65      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 5      | 0      | 660     |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 6      | 282140  |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 6      | 282157  |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 5      | 1      | 818     |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 6      | 0      | 25      |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 1      | 4      | 135198  |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 5      | 1      | 683     |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1791   | 40      |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2155   | 72      |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 3977   | 112     |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 260    | 74      |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 127004 | 329     |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 131241 | 515     |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1      | 1838   | 112     |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 443    | 2       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2295   | 113     |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 650    | 10      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1781   | 10      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 25     | 1       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 4       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 4       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 593    | 12      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 798    | 21      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 1       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 123    | 2       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6431   | 174     |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7564   | 177     |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 2       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 838    | 829834 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 2884   | 967530 | 0       |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 5      | 0      | 1881    |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 1      | 5      | 2304    |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 1      | 5      | 133455  |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 1      | 4      | 132806  |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 5      | 123     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 6      | 0      | 17      |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 6      | 0      | 33      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 5      | 0      | 650     |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 6      | 281207  |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 6      | 281223  |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 5      | 1      | 799     |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 6      | 0      | 23      |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 1      | 4      | 134495  |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 5      | 1      | 43      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1791   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2155   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 3977   | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 3977    |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 260    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 127004 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 131241 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 1839   | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 443    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2295   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 650    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1781   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 25     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 593    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 798    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 123    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6431   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7564   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 2048   | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 830672 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 970414 | 0       |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 5      | 0      | 1831    |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 1      | 5      | 2222    |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 1      | 5      | 133542  |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 1      | 4      | 131752  |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 5      | 123     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 6      | 0      | 19      |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 6      | 0      | 65      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 5      | 0      | 660     |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 6      | 144666  |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 6      | 144684  |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 5      | 1      | 827     |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 6      | 0      | 26      |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 1      | 4      | 133544  |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 5      | 1      | 21      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1791   | 40      |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2155   | 72      |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 3977   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 4089    |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 260    | 74      |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 127004 | 329     |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 131241 | 515     |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1      | 1838   | 112     |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 443    | 2       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2295   | 113     |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 650    | 10      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1781   | 10      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 25     | 1       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 4       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 4       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 593    | 12      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 798    | 21      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 1       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 123    | 2       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6431   | 174     |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7564   | 177     |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 2       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 838    | 829834 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 2884   | 967530 | 0       |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 5      | 0      | 26      |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 1      | 5      | 21      |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 1      | 5      | 57      |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 1      | 4      | 48      |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 5      | 123     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 6      | 0      | 2       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 6      | 0      | 33      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 5      | 0      | 10      |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 6      | 88      |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 6      | 89      |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 5      | 1      | 31      |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 6      | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 1      | 4      | 59      |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 5      | 1      | 21      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1791   | 40      |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2155   | 78      |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 3977   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 260    | 137     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 127004 | 4608    |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 131241 | 4863    |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1      | 1838   | 147     |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 443    | 9       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2295   | 155     |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 650    | 30      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 20      |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1781   | 50      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 25     | 1       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 4       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 4       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 593    | 35      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 798    | 44      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 1       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 123    | 2       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6431   | 203     |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7564   | 206     |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 9       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 830672 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 832711 | 137703 | 0       |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 5      | 0      | 1908    |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 1      | 5      | 2335    |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 1      | 5      | 127881  |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 1      | 4      | 127252  |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 5      | 123     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 6      | 0      | 18      |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 6      | 0      | 65      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 5      | 0      | 630     |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 6      | 275372  |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 6      | 275389  |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 5      | 1      | 800     |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 6      | 0      | 25      |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 1      | 4      | 128913  |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 5      | 1      | 21      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 3      | 1788   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 4      | 2151   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 7      | 3970   | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 1      | 259    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 5590   | 121414 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 5598   | 125643 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 13     | 1826   | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 14     | 429    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 27     | 2268   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 20     | 630    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 7      | 888    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 27     | 1754   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 1      | 24     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 5      | 588    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 6      | 792    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 2      | 121    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 270    | 6161   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 272    | 7292   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 830672 | 5930    |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 2048   | 968366 | 5930    |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 5      | 0      | 26      |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 1      | 5      | 21      |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 1      | 5      | 57      |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 1      | 4      | 48      |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 5      | 123     |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 6      | 0      | 2       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 6      | 0      | 33      |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 5      | 0      | 10      |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 6      | 88      |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 6      | 89      |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 5      | 1      | 31      |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 6      | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 1      | 4      | 59      |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 5      | 1      | 21      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1791   | 40      |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2155   | 78      |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 3977   | 118     |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 260    | 137     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 127004 | 4608    |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 131241 | 4863    |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1      | 1838   | 147     |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 443    | 9       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2295   | 155     |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 650    | 30      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 20      |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1781   | 50      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 25     | 1       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 4       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 4       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 593    | 35      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 798    | 44      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 1       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 123    | 2       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6431   | 203     |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7564   | 206     |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 9       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 2048   | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 5327   | 825345 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 7366   | 963048 | 0       |
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

