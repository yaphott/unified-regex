#!/bin/bash

CURRENT_DIR="$( pwd )"
CURRENT_FILENAME="$( basename "$0" )"

function exit_with_failure () {
    local failure_msg="$1"
    echo "===================================================================="
    if [[ ! -z "$failure_msg" ]]; then
      echo "Test failed: $failure_msg"
    else
      echo "Test failed"
    fi
    exit 1
}

function find_project_dir () {
    local project_dir=''
    if [[ -f "$CURRENT_DIR"'/'"$CURRENT_FILENAME" ]]; then
        # Current: root_dir/"$project_dir"'/result_validator/tests
        project_dir="$( dirname "$( dirname "$CURRENT_DIR" )" )"
    elif [[ -f "$CURRENT_DIR"'/validate.py' ]]; then
        # Current: root_dir/result_validator )"
        project_dir="$( dirname "$CURRENT_DIR" )"
    elif [[ -d "$CURRENT_DIR"'/result_validator' ]]; then
        # Current: root_dir
        project_dir="$CURRENT_DIR"
    else
        return 1
    fi
    echo "$project_dir"
    return 0
}

function run_check () {
    local project_dir="$1"
    local test_expects="$2"
    local pattern="$3"
    local filename="$4"
    local output="$( python3 "$project_dir"'/result_validator/validate.py' "$pattern" "$project_dir"'/result_validator/tests/sample_data/'"$filename" )"
    local exit_code="$?"
    if [[ "$exit_code" -ne 0 ]]; then
        exit_with_failure 'Failed to run validate.py'
    fi
    if [[ "$output" != "$test_expects" ]]; then
        return 1
    fi
    return 0
}

test_pattern='[\p{M}]'
project_dir="$( find_project_dir )" \
    || exit_with_failure 'Could not find project directory'
echo 'Project directory: '"$project_dir"

test_description='Valid if file has a result matching other than the pattern characters'
run_check "$project_dir" \
    valid \
    "$test_pattern" \
    mark.txt \
    || exit_with_failure "$test_description"
echo 'Test passed: '"$test_description"

test_description='Empty if file has no content'
run_check "$project_dir" \
    empty \
    "$test_pattern" \
    empty_one_line.txt \
    || exit_with_failure "$test_description"
echo 'Test passed: '"$test_description"

test_description='Empty if file has only whitespace'
run_check "$project_dir" \
    empty \
    "$test_pattern" \
    empty_two_line.txt \
    || exit_with_failure "$test_description"
echo 'Test passed: '"$test_description"

test_description='Invalid if file has a result matching the pattern characters'
run_check "$project_dir" \
    invalid \
    "$test_pattern" \
    mark_pattern_chars.txt \
    || exit_with_failure "$test_description"
echo 'Test passed: '"$test_description"

test_description='Invalid if file has a result matching the pattern characters (without backslash)'
run_check "$project_dir" \
    invalid \
    "$test_pattern" \
    mark_pattern_chars_without_backslash.txt \
    || exit_with_failure "$test_description"
echo 'Test passed: '"$test_description"

test_description='Invalid if file has a result matching the pattern characters (zero-filled)'
run_check "$project_dir" \
    invalid \
    "$test_pattern" \
    mark_pattern_chars_zero_filled.txt \
    || exit_with_failure "$test_description"
echo 'Test passed: '"$test_description"

test_description='Missing if file does not exist'
run_check "$project_dir" \
    missing \
    "$test_pattern" \
    mark_nonexistent.txt \
    || exit_with_failure "$test_description"
echo 'Test passed: '"$test_description"

echo "===================================================================="
echo 'All tests passed'
echo "===================================================================="
exit 0
