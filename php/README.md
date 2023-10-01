# PHP

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
  - [Compare with Javascript](#compare-with-javascript)
  - [Compare with Obj-C](#compare-with-obj-c)
  - [Compare with Perl](#compare-with-perl)
  - [Compare with Python](#compare-with-python)
  - [Compare with Ruby](#compare-with-ruby)
  - [Compare with Rust](#compare-with-rust)
  - [Compare with Scala](#compare-with-scala)

## Usage

### Run

Run the application with the following command:

```bash
php main.php <pattern> <file_path>
```

## Match Statistics

| Category                          | Name                  | Value                         | Total  | Percentile (%)<br>(include zero) | Percentile (%)<br>(exclude 0) |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -------------: | -------------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1831   | 75.00          | 72.73          |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2227   | 75.00          | 72.73          |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 133547 | 91.67          | 90.91          |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 131756 | 83.33          | 81.82          |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 128    | 100.00         | 100.00         |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 19     | 100.00         | 100.00         |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 65     | 100.00         | 100.00         |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 660    | 100.00         | 100.00         |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 144672 | 75.00          | 72.73          |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 144690 | 75.00          | 72.73          |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 828    | 100.00         | 100.00         |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 26     | 100.00         | 100.00         |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 133548 | 83.33          | 80.00          |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 22     | 83.33          | 81.82          |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 1831   | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 2227   | 58.33          | 54.55          |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 31     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 41.67          | —              |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 4089   | 91.67          | 66.67          |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 334    | 66.67          | 60.00          |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 127333 | 66.67          | 63.64          |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 131756 | 58.33          | 54.55          |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1950   | 66.67          | 60.00          |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 445    | 66.67          | 60.00          |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 13     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 2408   | 66.67          | 60.00          |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 660    | 66.67          | 63.64          |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 236    | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 895    | 58.33          | 54.55          |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 1791   | 58.33          | 54.55          |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 10     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 26     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 79     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 77     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 12     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 10     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 605    | 58.33          | 54.55          |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 819    | 58.33          | 54.55          |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 948    | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 63     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 125    | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 6605   | 58.33          | 54.55          |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 7741   | 58.33          | 54.55          |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 17     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 1      | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 1      | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 19     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 65     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 163    | 58.33          | 54.55          |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 66.67          | —              |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 137468 | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 829834 | 66.67          | 50.00          |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 967530 | 58.33          | 54.55          |
| Character Classes - Common        | Digit                 | `[\d]`                        | 660    | 91.67          | 91.67          |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 26     | 100.00         | 100.00         |
| Character Classes - Common        | Word Character        | `[\w]`                        | 133548 | 75.00          | 75.00          |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1805   | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2201   | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 133485 | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 131704 | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 128    | 0      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 17     | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 32     | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 650    | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 144578 | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 144595 | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 796    | 32     | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 20     | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 133548 | 0      | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 1831   | 0      | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 2227   | 0      | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 31     | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 4089   | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 334    | 0      | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 127333 | 0      | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 131756 | 0      | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1950   | 0      | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 445    | 0      | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 13     | 0      | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 2408   | 0      | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 660    | 0      | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 236    | 0      | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 895    | 0      | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 1791   | 0      | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 10     | 0      | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 26     | 0      | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 79     | 0      | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 77     | 0      | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 12     | 0      | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 10     | 0      | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 605    | 0      | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 819    | 0      | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 948    | 0      | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 63     | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 125    | 0      | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 6605   | 0      | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 7741   | 0      | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 17     | 0      | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 19     | 0      | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 65     | 0      | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 163    | 0      | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 137468 | 0      | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 829834 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 967530 | 0      | 0       |
| Character Classes - Common        | Digit                 | `[\d]`                        | 650    | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 20     | 6      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 133485 | 63     | 0       |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1805   | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2201   | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 133485 | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 131704 | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 17     | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 32     | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 650    | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 144578 | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 144595 | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 796    | 32     | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 20     | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 133485 | 63     | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2227   | 6       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 4089   | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 334    | 63      |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 127333 | 4279    |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 131756 | 4348    |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 1950   | 35      |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 445    | 7       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2408   | 42      |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 660    | 20      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 20      |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1791   | 40      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 26     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 79     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 77     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 605    | 23      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 819    | 23      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 63     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 125    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6605   | 2077    |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7741   | 2077    |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 163    | 7       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 829834 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 829827 | 137703 | 0       |
| Character Classes - Common        | Digit                 | `[\d]`                        | 650    | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 21     | 5      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 133485 | 63     | 0       |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1805   | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2201   | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 133485 | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 131704 | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 1      | 127    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 17     | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 33     | 32     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 650    | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 144578 | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 144595 | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 796    | 32     | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 20     | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 133485 | 63     | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 1363   | 468    | 1350    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 531    | 1696   | 1110487 |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 31     | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 4089   | 1109884 |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 334    | 0      | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 115830 | 11503  | 87601   |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 30     | 131726 | 982249  |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1950   | 0      | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 445    | 0      | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 13     | 0      | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 2408   | 0      | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 650    | 10     | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 236    | 0      | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 690    | 205    | 281131  |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 1481   | 310    | 281036  |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 9      | 1      | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 25     | 1      | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 76     | 3      | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 74     | 3      | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 11     | 1      | 50322   |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 9      | 1      | 50322   |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 514    | 91     | 238407  |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 666    | 153    | 322637  |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 894    | 54     | 99118   |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 53     | 10     | 192127  |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 109    | 16     | 192122  |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 5888   | 717    | 191419  |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 4875   | 2866   | 570129  |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 15     | 2      | 50322   |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 17     | 2      | 50322   |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 1      | 64     | 964512  |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 158    | 5      | 50318   |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 137468 | 0      | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 829834 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 106731 | 860799 | 116660  |
| Character Classes - Common        | Digit                 | `[\d]`                        | 650    | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 20     | 6      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 133485 | 63     | 0       |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1831   | 0      | 5       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2222   | 5      | 1       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 133542 | 5      | 1       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 131752 | 4      | 1       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 123    | 5      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 19     | 0      | 6       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 65     | 0      | 6       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 660    | 0      | 5       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 144666 | 6      | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 144684 | 6      | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 827    | 1      | 5       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 26     | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 133544 | 4      | 1       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 21     | 1      | 5       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 40     | 1791   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 72     | 2155   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 3977    |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 4089   | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 74     | 260    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 329    | 127004 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 515    | 131241 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 112    | 1838   | 1       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 2      | 443    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 113    | 2295   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 10     | 650    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 10     | 1781   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 1      | 25     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 4      | 75     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 4      | 73     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 12     | 593    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 21     | 798    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 1      | 62     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 2      | 123    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 174    | 6431   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 177    | 7564   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 2      | 161    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 2048    |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 829834 | 838     |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 967530 | 2884    |
| Character Classes - Common        | Digit                 | `[\d]`                        | 650    | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 20     | 6      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 133485 | 63     | 0       |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1831   | 0      | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2227   | 0      | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 133547 | 0      | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 131756 | 0      | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 128    | 0      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 19     | 0      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 65     | 0      | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 660    | 0      | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 144672 | 0      | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 144690 | 0      | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 828    | 0      | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 26     | 0      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 133548 | 0      | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 22     | 0      | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2227   | 6       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 4095    |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 4089   | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 334    | 63      |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 127333 | 4279    |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 131756 | 4348    |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 1950   | 35      |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 445    | 7       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2408   | 42      |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 660    | 20      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 20      |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1791   | 40      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 26     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 79     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 77     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 605    | 23      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 819    | 23      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 63     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 125    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6605   | 29      |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7741   | 29      |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 163    | 7       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 2048    |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 4489   | 825345 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 4482   | 963048 | 2048    |
| Character Classes - Common        | Digit                 | `[\d]`                        | 650    | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 2      | 24     | 1       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 133485 | 63     | 0       |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 1831   | 120     |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 2227   | 244     |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 895    | 132652 | 1404    |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 131756 | 1640    |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 1      | 18     | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 65     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 660    | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 144672 | 137474  |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 144690 | 137473  |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 9      | 819    | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 1      | 25     | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 895    | 132653 | 2549    |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 662     |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2227   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 4089    |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 4089   | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 334    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 127333 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 131756 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 1950   | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 445    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2408   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 660    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1791   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 26     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 79     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 77     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 605    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 819    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 63     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 125    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6605   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7741   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 163    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 829834 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 967530 | 0       |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 660    | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 1      | 25     | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 895    | 132653 | 2549    |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 70     | 1761   | 120     |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 105    | 2122   | 187     |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 1485   | 132062 | 1398    |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 580    | 131176 | 1634    |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 2      | 17     | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 32     | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 10     | 650    | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 933    | 143739 | 137474  |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 934    | 143756 | 137473  |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 28     | 800    | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 3      | 23     | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 1485   | 132063 | 2436    |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 22      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 40     | 1791   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 72     | 2155   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 3977    |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 112    | 3977   | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 74     | 260    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 329    | 127004 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 515    | 131241 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 112    | 1838   | 1       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 2      | 443    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 113    | 2295   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 10     | 650    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 10     | 1781   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 1      | 25     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 4      | 75     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 4      | 73     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 12     | 593    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 21     | 798    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 1      | 62     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 2      | 123    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 174    | 6431   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 177    | 7564   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 2      | 161    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 2048    |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 829834 | 838     |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 967530 | 2884    |
| Character Classes - Common        | Digit                 | `[\d]`                        | 10     | 650    | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 3      | 23     | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 1485   | 132063 | 2436    |
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

### Compare with [Python](../python)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1805   | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2201   | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 133485 | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 131704 | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 17     | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 32     | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 650    | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 144578 | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 144595 | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 796    | 32     | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 20     | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 133485 | 63     | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2227   | 6       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 4089   | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 334    | 63      |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 127333 | 4279    |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 131756 | 4348    |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 1950   | 35      |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 445    | 7       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2408   | 42      |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 660    | 20      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 20      |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1791   | 40      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 26     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 79     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 77     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 605    | 23      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 819    | 23      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 63     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 125    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6605   | 29      |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7741   | 29      |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 163    | 7       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 829834 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 829827 | 137703 | 0       |
| Character Classes - Common        | Digit                 | `[\d]`                        | 650    | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 21     | 5      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 133485 | 63     | 0       |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 43     | 1788   | 120     |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 76     | 2151   | 189     |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 7038   | 126509 | 1377    |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 6113   | 125643 | 1613    |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 1      | 18     | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 65     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 30     | 630    | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 6768   | 137904 | 137474  |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 6768   | 137922 | 137473  |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 27     | 801    | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 1      | 25     | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 7038   | 126510 | 2407    |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 43     | 1788   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 76     | 2151   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 3970    |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 4089   | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 75     | 259    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 5919   | 121414 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 6113   | 125643 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 125    | 1825   | 1       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 16     | 429    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 140    | 2268   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 30     | 630    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 7      | 888    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 37     | 1754   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 2      | 24     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 4      | 75     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 4      | 73     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 17     | 588    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 27     | 792    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 1      | 62     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 4      | 121    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 444    | 6161   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 449    | 7292   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 2      | 161    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 829834 | 6768    |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 967530 | 6766    |
| Character Classes - Common        | Digit                 | `[\d]`                        | 650    | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 20     | 6      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 133485 | 63     | 0       |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1805   | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2201   | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 133485 | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 131704 | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 17     | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 32     | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 650    | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 144578 | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 144595 | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 796    | 32     | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 20     | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 133485 | 63     | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2227   | 6       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 4095    |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 4089   | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 334    | 63      |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 127333 | 4279    |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 131756 | 4348    |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 1950   | 35      |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 445    | 7       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2408   | 42      |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 660    | 20      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 20      |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1791   | 40      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 26     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 79     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 77     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 605    | 23      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 819    | 23      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 63     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 125    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6605   | 29      |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7741   | 29      |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 163    | 7       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 4489   | 825345 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 4482   | 963048 | 0       |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 660    | 20      |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 1      | 25     | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 895    | 132653 | 6959    |
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
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1831   | 0      | 5       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2222   | 5      | 1       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 133542 | 5      | 1       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 131752 | 4      | 1       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 123    | 5      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 19     | 0      | 6       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 65     | 0      | 6       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 660    | 0      | 5       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 144666 | 6      | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 144684 | 6      | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 827    | 1      | 5       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 26     | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 133544 | 4      | 1       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 21     | 1      | 5       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 40     | 1791   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 72     | 2155   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 0      | 3977    |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 4089   | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 74     | 260    | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 329    | 127004 | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 515    | 131241 | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 112    | 1838   | 1       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 2      | 443    | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 113    | 2295   | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 10     | 650    | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 895    | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 10     | 1781   | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 1      | 25     | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 4      | 75     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 4      | 73     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 12     | 593    | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 21     | 798    | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 1      | 62     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 2      | 123    | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 174    | 6431   | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 177    | 7564   | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 2      | 161    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 2048    |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 0      | 829834 | 838     |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 0      | 967530 | 2884    |
| Character Classes - Common        | Digit                 | `[\d]`                        | 650    | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 20     | 6      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 133485 | 63     | 0       |
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

