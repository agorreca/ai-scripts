#!/bin/bash

# Absolute path to the directory where the scripts are located
SCRIPT_DIR="${WORKSPACE_PATH}/tc-ai/src/commits"

# Check and run Ollama if necessary
$SCRIPT_DIR/check_and_run_ollama.sh

# Get the git diff
diff=$(git diff --staged)

# Check if there are changes
if [ -z "$diff" ]; then
    echo "No changes to commit."
    exit 1
fi

# Run the Python script and pass the diff
commit_message=$(python $SCRIPT_DIR/generate_commit_message.py "$diff")

# Show the commit message
echo "Suggested commit message: $commit_message"
