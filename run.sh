#!/bin/bash

function exit_with_failure () {
  local failure_msg="$1"
  [[ -z "$failure_msg" ]] && failure_msg="Failed to run"
  echo "ERROR: $failure_msg"
  exit 1
}

declare -A build_commands
while IFS="=" read -r key value; do
  build_commands["$key"]="$value"
done < <(jq -r '.build | to_entries[] | "\(.key)=\(.value)"' commands.json)

declare -A base_commands
declare -a keys_with_preserved_order
while IFS="=" read -r key value; do
  keys_with_preserved_order+=("$key")
  base_commands["$key"]="$value"
done < <(jq -r '.base | to_entries[] | "\(.key)=\(.value)"' commands.json)

declare -A clean_commands
while IFS="=" read -r key value; do
  clean_commands["$key"]="$value"
done < <(jq -r '.clean | to_entries[] | "\(.key)=\(.value)"' commands.json)

function build () {
  local lang_name="$1"
  local build_cmd="${build_commands[$lang_name]}"
  if [[ -n "$build_cmd" ]]; then
    echo "Building $lang_name with ${build_cmd}"
    cd "$lang_name"
    eval "${build_cmd}" || exit_with_failure "Failed to build $lang_name"
    cd ..
  else
    echo "No build command for $lang_name"
  fi
}

function run () {
  local lang_name="$1"
  local base_cmd="${base_commands[$lang_name]}"
  if [[ -z "$base_cmd" ]]; then
    exit_with_failure "No base command for $lang_name"
  fi
  echo "Running $lang_name with ${base_cmd}"
  bash runner.sh "$lang_name" "${base_cmd}" || exit_with_failure "Failed to run $lang_name"
}

function clean () {
  local lang_name="$1"
  local clean_cmd="${clean_commands[$lang_name]}"
  if [[ -n "$clean_cmd" ]]; then
    echo "Cleaning up $lang_name with ${clean_cmd}"
    cd "$lang_name"
    eval "${clean_cmd}" || exit_with_failure "Failed to clean up $lang_name"
    cd ..
  else
    echo "No clean up command for $lang_name"
  fi
}

for lang_name in "${keys_with_preserved_order[@]}"; do
  clean "$lang_name"
  build "$lang_name"
  run "$lang_name"
  clean "$lang_name"
done

echo ""
echo "===================================================================="
echo "Done"
echo "===================================================================="

exit 0
