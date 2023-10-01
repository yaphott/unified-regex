# Obj-C

## Tables of Contents

[Go back to the overall results](../)

- [Usage](#usage)
  - [Build](#build)
  - [Run](#run)
  - [Clean up](#clean-up)
- [Match Statistics](#match-statistics)
- [Cardinalities](#cardinalities)
  - [Compare with C++](#compare-with-c)
  - [Compare with Go](#compare-with-go)
  - [Compare with Haskell](#compare-with-haskell)
  - [Compare with Java](#compare-with-java)
  - [Compare with Javascript](#compare-with-javascript)
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
. /usr/share/GNUstep/Makefiles/GNUstep.sh
clang $(gnustep-config --objc-flags) -I /usr/lib/gcc/x86_64-linux-gnu/12/include -o main main.m $(gnustep-config --base-libs)
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
rm -rf main.d
```

## Match Statistics

| Category                          | Name                  | Value                         | Total  | Percentile (%)<br>(include zero) | Percentile (%)<br>(exclude 0) |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -------------: | -------------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1951   | 100.00         | 100.00         |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2471   | 100.00         | 100.00         |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 134056 | 100.00         | 100.00         |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 133396 | 100.00         | 100.00         |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 128    | 100.00         | 100.00         |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 18     | 91.67          | 90.91          |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 65     | 100.00         | 100.00         |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 660    | 100.00         | 100.00         |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 282146 | 100.00         | 100.00         |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 282163 | 100.00         | 100.00         |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 819    | 91.67          | 90.91          |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 25     | 91.67          | 90.91          |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 135202 | 100.00         | 100.00         |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 684    | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 1831   | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 2227   | 58.33          | 54.55          |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 31     | 100.00         | 100.00         |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 4089   | 83.33          | 71.43          |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 75.00          | —              |
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
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2227   | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4089   | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 334    | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 127333 | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 131756 | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1950   | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 445    | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2408   | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 660    | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 895    | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1791   | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 605    | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 819    | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6605   | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7741   | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 163    | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 83.33          | —              |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 100.00         | 100.00         |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 829834 | 83.33          | 60.00          |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 967530 | 83.33          | 60.00          |

## Cardinalities

### Compare with [C++](../c++)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1925   | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2445   | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 133994 | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 133344 | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 128    | 0      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 16     | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 32     | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 650    | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 282052 | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 282068 | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 796    | 23     | 9       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 19     | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 135202 | 0      | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 662    | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 1831   | 0      | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 2227   | 0      | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 31     | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 4089   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
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
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2227   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4089   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 334    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 127333 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 131756 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1950   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 445    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2408   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 660    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 895    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1791   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 605    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 819    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6605   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7741   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 163    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 829834 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 967530 | 0      | 0       |

### Compare with [Go](../go)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1925   | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2445   | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 133994 | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 133344 | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 16     | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 32     | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 650    | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 282052 | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 282068 | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 796    | 23     | 9       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 19     | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 135139 | 63     | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 662    | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2227   | 6       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 4089   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
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
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2227   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4089   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 334    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 127333 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 131756 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1950   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 445    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2408   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 660    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 895    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1791   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 605    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 819    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6605   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7741   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 163    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 829834 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 967530 | 0      | 0       |

### Compare with [Haskell](../haskell)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1925   | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2445   | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 133994 | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 133344 | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 1      | 127    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 16     | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 33     | 32     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 650    | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 282052 | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 282068 | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 796    | 23     | 9       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 19     | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 135139 | 63     | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 662    | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 1363   | 468    | 1350    |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 531    | 1696   | 1110487 |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 31     | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 4089   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 1113973 |
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
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2227   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4089   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 334    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 127333 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 131756 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1950   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 445    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2408   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 660    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 895    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1791   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 605    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 819    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6605   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7741   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 163    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 829834 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 967530 | 0      | 0       |

### Compare with [Java](../java)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1951   | 0      | 5       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2466   | 5      | 1       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 134051 | 5      | 1       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 133392 | 4      | 1       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 123    | 5      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 18     | 0      | 6       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 65     | 0      | 6       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 660    | 0      | 5       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 282140 | 6      | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 282157 | 6      | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 818    | 1      | 5       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 25     | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 135198 | 4      | 1       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 683    | 1      | 5       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 40     | 1791   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 72     | 2155   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 112    | 3977   | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
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
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2227   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4089   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 334    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 127333 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 131756 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1950   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 445    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2408   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 660    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 895    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1791   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 605    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 819    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6605   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7741   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 163    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 829834 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 967530 | 0      | 0       |

### Compare with [Javascript](../javascript)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1951   | 0      | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2471   | 0      | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 134056 | 0      | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 133396 | 0      | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 128    | 0      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 18     | 0      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 65     | 0      | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 660    | 0      | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 282146 | 0      | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 282163 | 0      | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 819    | 0      | 0       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 25     | 0      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 135202 | 0      | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 684    | 0      | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2227   | 6       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 4089   | 6       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
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
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 1831   | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 2227   | 6       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 31     | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 4089   | 6       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 334    | 63      |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 127333 | 4279    |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 131756 | 4348    |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 1950   | 35      |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 445    | 7       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 13     | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 2408   | 42      |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 660    | 20      |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 236    | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 895    | 20      |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 1791   | 40      |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 26     | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 79     | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 77     | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 12     | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 605    | 23      |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 819    | 23      |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 948    | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 125    | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 6605   | 29      |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 7741   | 29      |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 17     | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 19     | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 65     | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 163    | 7       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 2048    |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 137468 | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 4489   | 825345 | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 4482   | 963048 | 2048    |

### Compare with [Perl](../perl)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 70     | 1881   | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 162    | 2309   | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 596    | 133460 | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 586    | 132810 | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 1      | 17     | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 32     | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 10     | 650    | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 933    | 281213 | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 934    | 281229 | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 28     | 791    | 9       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 2      | 23     | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 703    | 134499 | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 640    | 44     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 40     | 1791   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 72     | 2155   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 112    | 3977   | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 3977    |
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
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 40     | 1791   | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 72     | 2155   | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 31     | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 112    | 3977   | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 74     | 260    | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 329    | 127004 | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 515    | 131241 | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 112    | 1838   | 1       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 2      | 443    | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 13     | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 113    | 2295   | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 10     | 650    | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 236    | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 895    | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 10     | 1781   | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 1      | 25     | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 4      | 75     | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 4      | 73     | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 12     | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 12     | 593    | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 21     | 798    | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 948    | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 1      | 62     | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 2      | 123    | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 174    | 6431   | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 177    | 7564   | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 17     | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 19     | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 65     | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 2      | 161    | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 2048    |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 137468 | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 829834 | 838     |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0      | 967530 | 2884    |

### Compare with [PHP](../php)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 120    | 1831   | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 244    | 2227   | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 1404   | 132652 | 895     |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 1640   | 131756 | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 18     | 1       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 65     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 0      | 660    | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 137474 | 144672 | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 137473 | 144690 | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 0      | 819    | 9       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 25     | 1       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 2549   | 132653 | 895     |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 662    | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2227   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 4089   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 4089    |
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
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2227   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4089   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 334    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 127333 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 131756 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1950   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 445    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2408   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 660    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 895    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1791   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 605    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 819    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6605   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7741   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 163    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 829834 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 967530 | 0      | 0       |

### Compare with [Python](../python)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1925   | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2445   | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 133994 | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 133344 | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 16     | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 32     | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 650    | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 282052 | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 282068 | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 796    | 23     | 9       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 19     | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 135139 | 63     | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 662    | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2227   | 6       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 4089   | 0      | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
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
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2227   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4089   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 334    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 127333 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 131756 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1950   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 445    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2408   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 660    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 895    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1791   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 605    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 819    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6605   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7741   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 163    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 829834 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 967530 | 0      | 0       |

### Compare with [Ruby](../ruby)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 43     | 1908   | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 131    | 2340   | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 6170   | 127886 | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 6140   | 127256 | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 0      | 18     | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 0      | 65     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 30     | 630    | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 6768   | 275378 | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 6768   | 275395 | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 27     | 792    | 9       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 0      | 25     | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 6285   | 128917 | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 662    | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 43     | 1788   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 76     | 2151   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 119    | 3970   | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
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
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 43     | 1788   | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 76     | 2151   | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 31     | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 119    | 3970   | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 75     | 259    | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 5919   | 121414 | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 6113   | 125643 | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 125    | 1825   | 1       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 16     | 429    | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 13     | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 140    | 2268   | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 30     | 630    | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 236    | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 7      | 888    | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 37     | 1754   | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 2      | 24     | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 4      | 75     | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 4      | 73     | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 12     | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 17     | 588    | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 27     | 792    | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 948    | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 1      | 62     | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 4      | 121    | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 444    | 6161   | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 449    | 7292   | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 17     | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 19     | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 65     | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 2      | 161    | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 137468 | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 0      | 829834 | 6768    |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 0      | 967530 | 6766    |

### Compare with [Rust](../rust)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1925   | 26     | 0       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2445   | 26     | 0       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 133994 | 62     | 0       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 133344 | 52     | 0       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 0      | 128    | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 16     | 2      | 0       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 32     | 33     | 0       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 650    | 10     | 0       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 282052 | 94     | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 282068 | 95     | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 796    | 23     | 9       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 19     | 6      | 0       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 135139 | 63     | 0       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 662    | 22     | 0       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 0      | 1831   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 0      | 2227   | 6       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 0      | 4089   | 6       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
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
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 0      | 1831   | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 0      | 2227   | 6       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 0      | 31     | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 0      | 4089   | 6       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 0      | 334    | 63      |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 0      | 127333 | 4279    |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 0      | 131756 | 4348    |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 0      | 1950   | 35      |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 0      | 445    | 7       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 0      | 13     | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 0      | 2408   | 42      |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 0      | 660    | 20      |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 0      | 236    | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 0      | 895    | 20      |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 0      | 1791   | 40      |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 0      | 26     | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 0      | 79     | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 0      | 77     | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 0      | 12     | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 0      | 10     | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 0      | 605    | 23      |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 0      | 819    | 23      |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 0      | 948    | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 0      | 63     | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 0      | 125    | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 0      | 6605   | 29      |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 0      | 7741   | 29      |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 0      | 17     | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 0      | 1      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 0      | 19     | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 0      | 65     | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 0      | 163    | 7       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 0      | 137468 | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 4489   | 825345 | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 4482   | 963048 | 0       |

### Compare with [Scala](../scala)

| Category                          | Name                  | Value                         | Unique | Shared | Missing |
| :-------------------------------- | :-------------------- | :---------------------------- | -----: | -----: | ------: |
| Character Classes - ASCII         | Uppercase Letter      | `[[:upper:]]`                 | 1951   | 0      | 5       |
| Character Classes - ASCII         | Lowercase Letter      | `[[:lower:]]`                 | 2466   | 5      | 1       |
| Character Classes - ASCII         | Letter And Digit      | `[[:alnum:]]`                 | 134051 | 5      | 1       |
| Character Classes - ASCII         | Letter                | `[[:alpha:]]`                 | 133392 | 4      | 1       |
| Character Classes - ASCII         | ASCII Character       | `[[:ascii:]]`                 | 123    | 5      | 0       |
| Character Classes - ASCII         | Space And Tab         | `[[:blank:]]`                 | 18     | 0      | 6       |
| Character Classes - ASCII         | Control Character     | `[[:cntrl:]]`                 | 65     | 0      | 6       |
| Character Classes - ASCII         | Digit                 | `[[:digit:]]`                 | 660    | 0      | 5       |
| Character Classes - ASCII         | Visible Character     | `[[:graph:]]`                 | 282140 | 6      | 0       |
| Character Classes - ASCII         | Printable             | `[[:print:]]`                 | 282157 | 6      | 0       |
| Character Classes - ASCII         | Punctuation           | `[[:punct:]]`                 | 818    | 1      | 5       |
| Character Classes - ASCII         | Whitespace            | `[[:space:]]`                 | 25     | 0      | 6       |
| Character Classes - ASCII         | Word Character        | `[[:word:]]`                  | 135198 | 4      | 1       |
| Character Classes - ASCII         | Hexadecimal Digit     | `[[:xdigit:]]`                | 683    | 1      | 5       |
| Character Classes - POSIX - Short | Uppercase Letter      | `[\p{Lu}]`                    | 40     | 1791   | 0       |
| Character Classes - POSIX - Short | Lowercase Letter      | `[\p{Ll}]`                    | 72     | 2155   | 0       |
| Character Classes - POSIX - Short | Titlecase Letter      | `[\p{Lt}]`                    | 0      | 31     | 0       |
| Character Classes - POSIX - Short | Cased Letter          | `[\p{LC}]`                    | 112    | 3977   | 0       |
| Character Classes - POSIX - Short | Cased Letter Amp      | `[\p{L&}]`                    | 0      | 0      | 0       |
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
| Character Classes - POSIX - Long  | Uppercase Letter      | `[\p{Uppercase_Letter}]`      | 1831   | 0      | 0       |
| Character Classes - POSIX - Long  | Lowercase Letter      | `[\p{Lowercase_Letter}]`      | 2227   | 0      | 0       |
| Character Classes - POSIX - Long  | Titlecase Letter      | `[\p{Titlecase_Letter}]`      | 31     | 0      | 0       |
| Character Classes - POSIX - Long  | Cased Letter          | `[\p{Cased_Letter}]`          | 4089   | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Letter       | `[\p{Modifier_Letter}]`       | 334    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Letter          | `[\p{Other_Letter}]`          | 127333 | 0      | 0       |
| Character Classes - POSIX - Long  | Letter                | `[\p{Letter}]`                | 131756 | 0      | 0       |
| Character Classes - POSIX - Long  | Nonspacing Mark       | `[\p{Nonspacing_Mark}]`       | 1950   | 0      | 0       |
| Character Classes - POSIX - Long  | Spacing Mark          | `[\p{Spacing_Mark}]`          | 445    | 0      | 0       |
| Character Classes - POSIX - Long  | Enclosing Mark        | `[\p{Enclosing_Mark}]`        | 13     | 0      | 0       |
| Character Classes - POSIX - Long  | Mark                  | `[\p{Mark}]`                  | 2408   | 0      | 0       |
| Character Classes - POSIX - Long  | Decimal Number        | `[\p{Decimal_Number}]`        | 660    | 0      | 0       |
| Character Classes - POSIX - Long  | Letter Number         | `[\p{Letter_Number}]`         | 236    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Number          | `[\p{Other_Number}]`          | 895    | 0      | 0       |
| Character Classes - POSIX - Long  | Number                | `[\p{Number}]`                | 1791   | 0      | 0       |
| Character Classes - POSIX - Long  | Connector Punctuation | `[\p{Connector_Punctuation}]` | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Dash Punctuation      | `[\p{Dash_Punctuation}]`      | 26     | 0      | 0       |
| Character Classes - POSIX - Long  | Open Punctuation      | `[\p{Open_Punctuation}]`      | 79     | 0      | 0       |
| Character Classes - POSIX - Long  | Close Punctuation     | `[\p{Close_Punctuation}]`     | 77     | 0      | 0       |
| Character Classes - POSIX - Long  | Initial Punctuation   | `[\p{Initial_Punctuation}]`   | 12     | 0      | 0       |
| Character Classes - POSIX - Long  | Final Punctuation     | `[\p{Final_Punctuation}]`     | 10     | 0      | 0       |
| Character Classes - POSIX - Long  | Other Punctuation     | `[\p{Other_Punctuation}]`     | 605    | 0      | 0       |
| Character Classes - POSIX - Long  | Punctuation           | `[\p{Punctuation}]`           | 819    | 0      | 0       |
| Character Classes - POSIX - Long  | Math Symbol           | `[\p{Math_Symbol}]`           | 948    | 0      | 0       |
| Character Classes - POSIX - Long  | Currency Symbol       | `[\p{Currency_Symbol}]`       | 63     | 0      | 0       |
| Character Classes - POSIX - Long  | Modifier Symbol       | `[\p{Modifier_Symbol}]`       | 125    | 0      | 0       |
| Character Classes - POSIX - Long  | Other Symbol          | `[\p{Other_Symbol}]`          | 6605   | 0      | 0       |
| Character Classes - POSIX - Long  | Symbol                | `[\p{Symbol}]`                | 7741   | 0      | 0       |
| Character Classes - POSIX - Long  | Space Separator       | `[\p{Space_Separator}]`       | 17     | 0      | 0       |
| Character Classes - POSIX - Long  | Line Separator        | `[\p{Line_Separator}]`        | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Paragraph Separator   | `[\p{Paragraph_Separator}]`   | 1      | 0      | 0       |
| Character Classes - POSIX - Long  | Separator             | `[\p{Separator}]`             | 19     | 0      | 0       |
| Character Classes - POSIX - Long  | Control               | `[\p{Control}]`               | 65     | 0      | 0       |
| Character Classes - POSIX - Long  | Format                | `[\p{Format}]`                | 163    | 0      | 0       |
| Character Classes - POSIX - Long  | Surrogate             | `[\p{Surrogate}]`             | 0      | 0      | 0       |
| Character Classes - POSIX - Long  | Private Use           | `[\p{Private_Use}]`           | 137468 | 0      | 0       |
| Character Classes - POSIX - Long  | Unassigned            | `[\p{Unassigned}]`            | 829834 | 0      | 0       |
| Character Classes - POSIX - Long  | Other                 | `[\p{Other}]`                 | 967530 | 0      | 0       |

