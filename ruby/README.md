# Ruby

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
  - [Compare with PHP](#compare-with-php)
  - [Compare with Python](#compare-with-python)
  - [Compare with Rust](#compare-with-rust)
  - [Compare with Scala](#compare-with-scala)

## Usage

### Run

Run the application with the following command:

```bash
ruby main.rb <pattern> <file_path>
```

## Match Statistics

| Category                          | Name                  | Value                         | Total  | Percentile (%)<br>(include zero) | Percentile (%)<br>(exclude 0) |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -------------: | -------------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1908   | 91.67          | 90.91          |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2340   | 91.67          | 90.91          |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 127886 | 75.00          | 72.73          |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 127256 | 75.00          | 72.73          |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 128    | 100.00         | 100.00         |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 18     | 91.67          | 90.91          |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 65     | 100.00         | 100.00         |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 630    | 75.00          | 72.73          |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 275378 | 83.33          | 81.82          |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 275395 | 83.33          | 81.82          |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 801    | 83.33          | 81.82          |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 25     | 91.67          | 90.91          |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 128917 | 75.00          | 70.00          |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 22     | 83.33          | 81.82          |
| Character Classes - Common        | Digit                 | `[\d]`                        | 10     | 66.67          | 66.67          |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 6      | 58.33          | 58.33          |
| Character Classes - Common        | Word Character        | `[\w]`                        | 63     | 66.67          | 66.67          |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1788   | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2151   | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 3970   | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 259    | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 121414 | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 125643 | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1826   | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 429    | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2268   | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 630    | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 888    | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1754   | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 24     | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 75     | 75.00          | 40.00          |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 73     | 75.00          | 40.00          |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 588    | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 792    | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 62     | 75.00          | 40.00          |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 121    | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6161   | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7292   | 66.67          | 20.00          |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 161    | 75.00          | 40.00          |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 83.33          | —              |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 836602 | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 974296 | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 1788   | 16.67          | 9.09           |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 2151   | 16.67          | 9.09           |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 31     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 3970   | 50.00          | 14.29          |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 75.00          | —              |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 259    | 25.00          | 10.00          |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 121414 | 25.00          | 18.18          |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 125643 | 16.67          | 9.09           |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1826   | 25.00          | 10.00          |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 429    | 25.00          | 10.00          |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 13     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 2268   | 25.00          | 10.00          |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 630    | 25.00          | 18.18          |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 236    | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 888    | 16.67          | 9.09           |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 1754   | 16.67          | 9.09           |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 10     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 24     | 25.00          | 18.18          |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 75     | 50.00          | 45.45          |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 73     | 50.00          | 45.45          |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 12     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 10     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 588    | 16.67          | 9.09           |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 792    | 16.67          | 9.09           |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 948    | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 62     | 41.67          | 36.36          |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 121    | 16.67          | 9.09           |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 6161   | 16.67          | 9.09           |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 7292   | 16.67          | 9.09           |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 17     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 1      | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 1      | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 19     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 65     | 91.67          | 90.91          |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 161    | 41.67          | 36.36          |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 66.67          | —              |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 137468 | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 836602 | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 974296 | 91.67          | 90.91          |

## Cardinalities

### Compare with [C++](../c++)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1882   | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2314   | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 127824 | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 127204 | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 128    | 0      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 16     | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 32     | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 620    | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 275284 | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 275300 | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 769    | 32     | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 19     | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 128917 | 0      | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 1788   | 0      | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 2151   | 0      | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 31     | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 3970   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 259    | 0      | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 121414 | 0      | 0       |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 125643 | 0      | 0       |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1826   | 0      | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 429    | 0      | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 13     | 0      | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 2268   | 0      | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 630    | 0      | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 236    | 0      | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 888    | 0      | 0       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 1754   | 0      | 0       |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 10     | 0      | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 24     | 0      | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 75     | 0      | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 73     | 0      | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 12     | 0      | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 10     | 0      | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 588    | 0      | 0       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 792    | 0      | 0       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 948    | 0      | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 62     | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 121    | 0      | 0       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 6161   | 0      | 0       |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 7292   | 0      | 0       |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 17     | 0      | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 19     | 0      | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 65     | 0      | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 161    | 0      | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 137468 | 0      | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 836602 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 974296 | 0      | 0       |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1788   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2151   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 3970   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 259    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 121414 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 125643 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1826   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 429    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2268   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 630    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 888    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1754   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 24     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 75     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 73     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 588    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 792    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 62     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 121    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6161   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7292   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 161    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 836602 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 974296 | 0      | 0       |

### Compare with [Go](../go)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1882   | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2314   | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 127824 | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 127204 | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 16     | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 32     | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 620    | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 275284 | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 275300 | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 769    | 32     | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 19     | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 128854 | 63     | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1788   | 43      |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2151   | 82      |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 3970   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 259    | 138     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 121414 | 10198   |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 125643 | 10461   |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1      | 1825   | 160     |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 429    | 23      |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2268   | 182     |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 630    | 50      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 888    | 27      |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1754   | 77      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 24     | 2       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 4       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 4       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 588    | 40      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 792    | 50      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 1       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 121    | 4       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6161   | 2521    |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7292   | 2526    |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 9       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 836602 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 836593 | 137703 | 0       |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 1      | 5      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1788   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2151   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 3970   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 259    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 121414 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 125643 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1826   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 429    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2268   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 630    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 888    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1754   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 24     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 75     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 73     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 588    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 792    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 62     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 121    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6161   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7292   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 161    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 836602 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 974296 | 0      | 0       |

### Compare with [Haskell](../haskell)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1882   | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2314   | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 127824 | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 127204 | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 1      | 127    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 16     | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 33     | 32     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 620    | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 275284 | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 275300 | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 769    | 32     | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 19     | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 128854 | 63     | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 1320   | 468    | 1350    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 531    | 1620   | 1110563 |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 31     | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 3970   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 1113973 |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 259    | 0      | 0       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 110349 | 11065  | 88039   |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 30     | 125613 | 988362  |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1826   | 0      | 0       |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 429    | 0      | 0       |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 13     | 0      | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 2268   | 0      | 0       |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 620    | 10     | 0       |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 236    | 0      | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 683    | 205    | 281131  |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 1447   | 307    | 281039  |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 9      | 1      | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 23     | 1      | 0       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 72     | 3      | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 70     | 3      | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 11     | 1      | 50322   |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 9      | 1      | 50322   |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 499    | 89     | 238409  |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 641    | 151    | 322639  |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 894    | 54     | 99118   |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 52     | 10     | 192127  |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 106    | 15     | 192123  |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 5541   | 620    | 191516  |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 4648   | 2644   | 570351  |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 15     | 2      | 50322   |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 1      | 0      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 17     | 2      | 50322   |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 1      | 64     | 964512  |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 156    | 5      | 50318   |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 137468 | 0      | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 836602 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 107744 | 866552 | 110907  |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1788   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2151   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 3970   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 259    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 121414 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 125643 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1826   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 429    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2268   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 630    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 888    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1754   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 24     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 75     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 73     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 588    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 792    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 62     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 121    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6161   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7292   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 161    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 836602 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 974296 | 0      | 0       |

### Compare with [Java](../java)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1908   | 0      | 5       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2335   | 5      | 1       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 127881 | 5      | 1       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 127252 | 4      | 1       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 123    | 5      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 18     | 0      | 6       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 65     | 0      | 6       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 630    | 0      | 5       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 275372 | 6      | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 275389 | 6      | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 800    | 1      | 5       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 25     | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 128913 | 4      | 1       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 21     | 1      | 5       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1788   | 3       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2151   | 4       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 3970   | 7       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 259    | 1       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 121414 | 5590    |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 125643 | 5598    |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 1826   | 13      |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 429    | 14      |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2268   | 27      |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 630    | 20      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 888    | 7       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1754   | 27      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 24     | 1       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 588    | 5       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 792    | 6       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 121    | 2       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6161   | 270     |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7292   | 272     |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 2048    |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 5930   | 830672 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 5930   | 968366 | 2048    |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1788   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2151   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 3970   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 259    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 121414 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 125643 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1826   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 429    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2268   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 630    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 888    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1754   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 24     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 75     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 73     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 588    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 792    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 62     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 121    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6161   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7292   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 161    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 836602 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 974296 | 0      | 0       |

### Compare with [Javascript](../javascript)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1908   | 0      | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2340   | 0      | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 127886 | 0      | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 127256 | 0      | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 128    | 0      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 18     | 0      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 65     | 0      | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 630    | 0      | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 275378 | 0      | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 275395 | 0      | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 801    | 0      | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 25     | 0      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 128917 | 0      | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 22     | 0      | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1788   | 43      |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2151   | 82      |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 3970   | 125     |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 259    | 138     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 121414 | 10198   |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 125643 | 10461   |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1      | 1825   | 160     |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 429    | 23      |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2268   | 182     |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 630    | 50      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 888    | 27      |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1754   | 77      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 24     | 2       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 4       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 4       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 588    | 40      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 792    | 50      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 1       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 121    | 4       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6161   | 473     |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7292   | 478     |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 9       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 2048    |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 11257  | 825345 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 11248  | 963048 | 2048    |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 19      |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 1788   | 43      |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 2151   | 82      |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 31     | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 3970   | 125     |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 259    | 138     |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 121414 | 10198   |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 125643 | 10461   |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1      | 1825   | 160     |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 429    | 23      |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 13     | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 2268   | 182     |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 630    | 50      |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 236    | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 888    | 27      |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 1754   | 77      |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 24     | 2       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 75     | 4       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 73     | 4       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 12     | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 588    | 40      |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 792    | 50      |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 948    | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 62     | 1       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 121    | 4       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 6161   | 473     |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 7292   | 478     |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 17     | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 19     | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 65     | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 161    | 9       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 2048    |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 137468 | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 11257  | 825345 | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 11248  | 963048 | 2048    |

### Compare with [Obj-C](../objc)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 0      | 1908   | 43      |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 0      | 2340   | 131     |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 0      | 127886 | 6170    |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 0      | 127256 | 6140    |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 18     | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 65     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 630    | 30      |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 0      | 275378 | 6768    |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 0      | 275395 | 6768    |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 9      | 792    | 27      |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 25     | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 0      | 128917 | 6285    |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 662     |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1788   | 43      |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2151   | 76      |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 3970   | 119     |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 259    | 75      |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 121414 | 5919    |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 125643 | 6113    |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1      | 1825   | 125     |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 429    | 16      |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2268   | 140     |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 630    | 30      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 888    | 7       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1754   | 37      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 24     | 2       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 4       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 4       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 588    | 17      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 792    | 27      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 1       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 121    | 4       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6161   | 444     |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7292   | 449     |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 2       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 6768   | 829834 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 6766   | 967530 | 0       |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 650     |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 19      |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 135139  |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 1788   | 43      |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 2151   | 76      |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 31     | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 3970   | 119     |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 259    | 75      |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 121414 | 5919    |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 125643 | 6113    |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1      | 1825   | 125     |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 429    | 16      |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 13     | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 2268   | 140     |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 630    | 30      |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 236    | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 888    | 7       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 1754   | 37      |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 24     | 2       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 75     | 4       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 73     | 4       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 12     | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 588    | 17      |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 792    | 27      |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 948    | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 62     | 1       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 121    | 4       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 6161   | 444     |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 7292   | 449     |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 17     | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 19     | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 65     | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 161    | 2       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 137468 | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 6768   | 829834 | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 6766   | 967530 | 0       |

### Compare with [Perl](../perl)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 30     | 1878   | 3       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 35     | 2305   | 4       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 65     | 127821 | 5639    |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 65     | 127191 | 5619    |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 1      | 17     | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 32     | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 630    | 20      |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 95     | 275283 | 5930    |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 96     | 275299 | 5930    |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 7      | 794    | 6       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 2      | 23     | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 65     | 128852 | 5647    |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 22      |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1788   | 3       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2151   | 4       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 3970   | 7       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 3977    |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 259    | 1       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 121414 | 5590    |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 125643 | 5598    |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 1826   | 13      |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 429    | 14      |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2268   | 27      |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 630    | 20      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 888    | 7       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1754   | 27      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 24     | 1       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 588    | 5       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 792    | 6       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 121    | 2       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6161   | 270     |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7292   | 272     |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 2048    |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 5930   | 830672 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 5930   | 968366 | 2048    |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 640     |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 17      |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 134436  |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 1788   | 3       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 2151   | 4       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 31     | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 3970   | 7       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 259    | 1       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 121414 | 5590    |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 125643 | 5598    |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 1826   | 13      |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 429    | 14      |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 13     | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 2268   | 27      |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 630    | 20      |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 236    | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 888    | 7       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 1754   | 27      |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 24     | 1       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 75     | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 73     | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 12     | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 588    | 5       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 792    | 6       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 948    | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 62     | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 121    | 2       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 6161   | 270     |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 7292   | 272     |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 17     | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 19     | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 65     | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 161    | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 2048    |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 137468 | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 5930   | 830672 | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 5930   | 968366 | 2048    |

### Compare with [PHP](../php)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 120    | 1788   | 43      |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 189    | 2151   | 76      |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 1377   | 126509 | 7038    |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 1613   | 125643 | 6113    |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 18     | 1       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 65     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 630    | 30      |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 137474 | 137904 | 6768    |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 137473 | 137922 | 6768    |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 801    | 27      |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 25     | 1       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 2407   | 126510 | 7038    |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1788   | 43      |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2151   | 76      |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 3970   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 4089    |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 259    | 75      |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 121414 | 5919    |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 125643 | 6113    |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1      | 1825   | 125     |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 429    | 16      |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2268   | 140     |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 630    | 30      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 888    | 7       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1754   | 37      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 24     | 2       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 4       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 4       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 588    | 17      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 792    | 27      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 1       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 121    | 4       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6161   | 444     |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7292   | 449     |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 2       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 6768   | 829834 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 6766   | 967530 | 0       |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 650     |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 20      |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 133485  |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1788   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2151   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 3970   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 259    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 121414 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 125643 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1826   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 429    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2268   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 630    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 888    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1754   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 24     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 75     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 73     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 588    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 792    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 62     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 121    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6161   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7292   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 161    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 836602 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 974296 | 0      | 0       |

### Compare with [Python](../python)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1882   | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2314   | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 127824 | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 127204 | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 16     | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 32     | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 620    | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 275284 | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 275300 | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 769    | 32     | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 19     | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 128854 | 63     | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1788   | 43      |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2151   | 82      |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 3970   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 259    | 138     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 121414 | 10198   |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 125643 | 10461   |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1      | 1825   | 160     |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 429    | 23      |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2268   | 182     |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 630    | 50      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 888    | 27      |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1754   | 77      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 24     | 2       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 4       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 4       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 588    | 40      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 792    | 50      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 1       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 121    | 4       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6161   | 473     |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7292   | 478     |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 9       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 836602 | 0      | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 836593 | 137703 | 0       |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 1      | 5      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1788   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2151   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 3970   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 259    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 121414 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 125643 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1826   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 429    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2268   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 630    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 888    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1754   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 24     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 75     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 73     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 588    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 792    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 62     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 121    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6161   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7292   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 161    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 836602 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 974296 | 0      | 0       |

### Compare with [Rust](../rust)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1882   | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2314   | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 127824 | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 127204 | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 16     | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 32     | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 620    | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 275284 | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 275300 | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 769    | 32     | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 19     | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 128854 | 63     | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 0      | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1788   | 43      |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2151   | 82      |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 3970   | 125     |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 259    | 138     |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 121414 | 10198   |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 125643 | 10461   |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 1      | 1825   | 160     |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 429    | 23      |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2268   | 182     |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 630    | 50      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 888    | 27      |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1754   | 77      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 24     | 2       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 4       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 4       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 588    | 40      |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 792    | 50      |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 1       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 121    | 4       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6161   | 473     |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7292   | 478     |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 9       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 11257  | 825345 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 11248  | 963048 | 0       |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 670     |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 19      |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 139549  |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 1788   | 43      |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 2151   | 82      |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 31     | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 3970   | 125     |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 259    | 138     |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 121414 | 10198   |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 125643 | 10461   |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1      | 1825   | 160     |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 429    | 23      |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 13     | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 2268   | 182     |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 630    | 50      |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 236    | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 888    | 27      |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 1754   | 77      |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 24     | 2       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 75     | 4       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 73     | 4       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 12     | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 588    | 40      |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 792    | 50      |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 948    | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 62     | 1       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 121    | 4       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 6161   | 473     |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 7292   | 478     |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 17     | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 19     | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 65     | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 161    | 9       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 137468 | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 11257  | 825345 | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 11248  | 963048 | 0       |

### Compare with [Scala](../scala)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1908   | 0      | 5       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2335   | 5      | 1       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 127881 | 5      | 1       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 127252 | 4      | 1       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 123    | 5      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 18     | 0      | 6       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 65     | 0      | 6       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 630    | 0      | 5       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 275372 | 6      | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 275389 | 6      | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 800    | 1      | 5       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 25     | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 128913 | 4      | 1       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 21     | 1      | 5       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1788   | 3       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2151   | 4       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 3970   | 7       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
| Character Classes - POSIX - Short | Modifier Letter       | `[\p{Lm}]`                    | 0      | 259    | 1       |
| Character Classes - POSIX - Short | Other Letter          | `[\p{Lo}]`                    | 0      | 121414 | 5590    |
| Character Classes - POSIX - Short | Letter                | `[\p{L}]`                     | 0      | 125643 | 5598    |
| Character Classes - POSIX - Short | Nonspacing Mark       | `[\p{Mn}]`                    | 0      | 1826   | 13      |
| Character Classes - POSIX - Short | Spacing Mark          | `[\p{Mc}]`                    | 0      | 429    | 14      |
| Character Classes - POSIX - Short | Enclosing Mark        | `[\p{Me}]`                    | 0      | 13     | 0       |
| Character Classes - POSIX - Short | Mark                  | `[\p{M}]`                     | 0      | 2268   | 27      |
| Character Classes - POSIX - Short | Decimal Number        | `[\p{Nd}]`                    | 0      | 630    | 20      |
| Character Classes - POSIX - Short | Letter Number         | `[\p{Nl}]`                    | 0      | 236    | 0       |
| Character Classes - POSIX - Short | Other Number          | `[\p{No}]`                    | 0      | 888    | 7       |
| Character Classes - POSIX - Short | Number                | `[\p{N}]`                     | 0      | 1754   | 27      |
| Character Classes - POSIX - Short | Connector Punctuation | `[\p{Pc}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Dash Punctuation      | `[\p{Pd}]`                    | 0      | 24     | 1       |
| Character Classes - POSIX - Short | Open Punctuation      | `[\p{Ps}]`                    | 0      | 75     | 0       |
| Character Classes - POSIX - Short | Close Punctuation     | `[\p{Pe}]`                    | 0      | 73     | 0       |
| Character Classes - POSIX - Short | Initial Punctuation   | `[\p{Pi}]`                    | 0      | 12     | 0       |
| Character Classes - POSIX - Short | Final Punctuation     | `[\p{Pf}]`                    | 0      | 10     | 0       |
| Character Classes - POSIX - Short | Other Punctuation     | `[\p{Po}]`                    | 0      | 588    | 5       |
| Character Classes - POSIX - Short | Punctuation           | `[\p{P}]`                     | 0      | 792    | 6       |
| Character Classes - POSIX - Short | Math Symbol           | `[\p{Sm}]`                    | 0      | 948    | 0       |
| Character Classes - POSIX - Short | Currency Symbol       | `[\p{Sc}]`                    | 0      | 62     | 0       |
| Character Classes - POSIX - Short | Modifier Symbol       | `[\p{Sk}]`                    | 0      | 121    | 2       |
| Character Classes - POSIX - Short | Other Symbol          | `[\p{So}]`                    | 0      | 6161   | 270     |
| Character Classes - POSIX - Short | Symbol                | `[\p{S}]`                     | 0      | 7292   | 272     |
| Character Classes - POSIX - Short | Space Separator       | `[\p{Zs}]`                    | 0      | 17     | 0       |
| Character Classes - POSIX - Short | Line Separator        | `[\p{Zl}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Paragraph Separator   | `[\p{Zp}]`                    | 0      | 1      | 0       |
| Character Classes - POSIX - Short | Separator             | `[\p{Z}]`                     | 0      | 19     | 0       |
| Character Classes - POSIX - Short | Control               | `[\p{Cc}]`                    | 0      | 65     | 0       |
| Character Classes - POSIX - Short | Format                | `[\p{Cf}]`                    | 0      | 161    | 0       |
| Character Classes - POSIX - Short | Surrogate             | `[\p{Cs}]`                    | 0      | 0      | 2048    |
| Character Classes - POSIX - Short | Private Use           | `[\p{Co}]`                    | 0      | 137468 | 0       |
| Character Classes - POSIX - Short | Unassigned            | `[\p{Cn}]`                    | 5930   | 830672 | 0       |
| Character Classes - POSIX - Short | Other                 | `[\p{C}]`                     | 5930   | 968366 | 2048    |
| Character Classes - Common        | Digit                 | `[\d]`                        | 0      | 10     | 0       |
| Character Classes - Common        | Whitespace            | `[\s]`                        | 0      | 6      | 0       |
| Character Classes - Common        | Word Character        | `[\w]`                        | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1788   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2151   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 3970   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 259    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 121414 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 125643 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1826   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 429    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2268   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 630    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 888    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1754   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 24     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 75     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 73     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 588    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 792    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 62     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 121    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6161   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7292   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 161    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 836602 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 974296 | 0      | 0       |

