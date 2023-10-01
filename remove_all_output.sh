#!/bin/bash

declare -a language_names
while IFS="=" read -r key value; do
  language_names+=("$key")
done < <(jq -r '.base | keys[]' commands.json)

for language_name in "${language_names[@]}"; do
  if [[ -z "$language_name" ]]; then
    echo "Skipping '$language_name' because it is empty"
    continue
  fi
  if [[ ! -d "$language_name" ]]; then
    echo "Skipping '$language_name' because it is not a directory"
    continue
  fi

  output_dir="$language_name/output"
  if [[ ! -d "$output_dir" ]]; then
    echo "Skipping '$language_name' because '$output_dir' is not a directory"
    continue
  fi

  echo "Removing all *.txt files in '$output_dir'"
  rm -f "$output_dir/"*'.txt'
done
