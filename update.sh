#!/bin/bash
# update-gitattributes.sh
# Auto-generate .gitattributes for all submodules to ignore merge conflicts on GitHub

GITATTRIBUTES_FILE=".gitattributes"

echo "# GitHub-only: ignore merge conflicts for submodules" > "$GITATTRIBUTES_FILE"

# Loop through submodule paths in .gitmodules
git config --file .gitmodules --get-regexp path | awk '{print $2}' | while read sub; do
    echo "$sub merge=ours" >> "$GITATTRIBUTES_FILE"
done

echo ".gitattributes updated:"
cat "$GITATTRIBUTES_FILE"
