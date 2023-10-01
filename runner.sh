#!/bin/bash

PROJECT_PATH="$(pwd)"
echo "    Project path: $PROJECT_PATH"

function exit_with_failure () {
  local failure_msg="$1"
  if [[ -z "$failure_msg" ]]; then
    failure_msg="Failed to run"
  fi
  echo "ERROR: $failure_msg"
  exit 1
}

function run_command () {
  local lang_name="$1"
  local base_cmd="$2"
  local pattern="$3"
  local file_path="$4"
  echo "Running:"
  echo "    Language name: $lang_name"
  echo "    Base Command: ${base_cmd}"
  echo "    Pattern: $pattern"
  echo "    File path: $file_path"

  if [ "$lang_name" == "scala" ]; then
    $base_cmd "run $pattern $file_path"
  else
    $base_cmd "$pattern" "$file_path"
  fi
}

function create_new_file () {
  local file_path="$1"
  if [[ -f "$file_path" ]]; then
    echo "    Removing existing file: $file_path"
    rm -f "$file_path"
  fi
  echo "    Creating new file: $file_path"
  touch "$file_path"
}

function validate_result () {
  local pattern="$1"
  local file_path="$2"
  echo "Validating:"
  echo "    Pattern: $pattern"
  echo "    File path: $file_path"

  local result_status=$(python3 "$PROJECT_PATH"'/result_validator/validate.py' "$pattern" "$file_path")
  if [[ $? -ne 0 ]]; then
    return 1
  fi
  if [[ "$result_status" == "valid" ]]; then
    echo "Valid match result"
    return 0
  elif [[ "$result_status" == "invalid" ]]; then
    echo "Invalid match result"
    create_new_file "$file_path" || exit_with_failure "Failed to create new file"
  elif [[ "$result_status" == "missing" ]]; then
    echo "Missing match result"
    create_new_file "$file_path" || exit_with_failure "Failed to create new file"
  elif [[ "$result_status" == "empty" ]]; then
    echo "Empty match result"
    create_new_file "$file_path" || exit_with_failure "Failed to create new file"
  else
    exit_with_failure "Unknown result status: $result_status"
  fi
}

function mk_outfile_path () {
  local lang_name="$1"
  local patterns_file_name="$2"
  local pattern_name="$3"
  [[ -z "$lang_name" ]] && exit_with_failure "Missing required argument: lang_name"
  [[ -z "$patterns_file_name" ]] && exit_with_failure "Missing required argument: patterns_file_name"
  [[ -z "$pattern_name" ]] && exit_with_failure "Missing required argument: pattern_name"
  echo "$PROJECT_PATH"'/'"$lang_name"'/output/'"$patterns_file_name"'-'"$pattern_name"'.txt'
}

# Validate user input
lang_name="$1"
base_cmd="$2"
[[ -z "$lang_name" ]] && exit_with_failure "Missing required argument: lang_name"
[[ -z "$base_cmd" ]] && exit_with_failure "Missing required argument: base_cmd"
echo "    Language name: $lang_name, command: ${base_cmd}"

cd $lang_name || exit_with_failure "Failed to change directory to $lang_name"

# Test that braces do not match
outfile_path=$(mk_outfile_path "$lang_name" "test" "test")
run_command "$lang_name" "${base_cmd}" '[x]' "$outfile_path" \
  || exit_with_failure 'Failed whle running '"$base_cmd"
line_count=$(wc -l "$outfile_path" | awk '{print $1}')
[[ $line_count -eq 1 ]] || exit_with_failure "Should not match straight braces"
file_contents=$(cat "$outfile_path" | python3 -c "import sys; print(sys.stdin.read().strip().lstrip('0'))")
[[ "$file_contents" == "78" ]] || exit_with_failure "Should match 'x'"
rm "$outfile_path" || exit_with_failure "Failed to remove output file"

# Test that single backslash is escaped
outfile_path="./test.txt"
run_command "$lang_name" "${base_cmd}" '[\]]' "$outfile_path" \
  || exit_with_failure 'Failed whle running '"$base_cmd"
line_count=$(wc -l "$outfile_path" | awk '{print $1}')
[[ $line_count -eq 1 ]] || exit_with_failure "Backslash should be escaped"
file_contents=$(cat "$outfile_path" | python3 -c "import sys; print(sys.stdin.read().strip().lstrip('0'))")
[[ "$file_contents" == "5D" ]] || exit_with_failure "Should match ']'"
rm "$outfile_path" || exit_with_failure "Failed to remove output file"

patterns_dir_path="$PROJECT_PATH/patterns"
echo "    Pattern dir path: $patterns_dir_path"
for patterns_file_path in "$patterns_dir_path"/*.json; do
  patterns_file_name="$(basename "$patterns_file_path" | cut -d'.' -f1)"
  echo "    Pattern file path: $patterns_file_path"
  echo "    Pattern file name: $patterns_file_name"

  declare -A patterns
  while IFS="=" read -r key value; do
    patterns["$key"]="$value"
  done < <(jq -r 'to_entries[] | "\(.key)=\(.value)"' "$patterns_file_path")

  for pattern_name in "${!patterns[@]}"; do
    [[ -z "$pattern_name" ]] && exit_with_failure "Empty pattern name"
    pattern_exp="${patterns[$pattern_name]}"
    [[ -z "$pattern_exp" ]] && exit_with_failure "Empty pattern expression"

    outfile_path=$(mk_outfile_path "$lang_name" "$patterns_file_name" "$pattern_name")
    run_command "$lang_name" "${base_cmd}" "$pattern_exp" "$outfile_path" \
      || echo "Skipping ..."
    validate_result "$pattern_exp" "$outfile_path" \
      || exit_with_failure "Failed to validate result"
  done
done

exit 0
