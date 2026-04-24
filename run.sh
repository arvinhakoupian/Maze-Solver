#!/usr/bin/env bash

set -e

# Activate virtual environment and run the app.
if [ -f ".venv/Scripts/activate" ]; then
    # Git Bash on Windows
    source .venv/Scripts/activate
elif [ -f ".venv/bin/activate" ]; then
    # Linux/macOS
    source .venv/bin/activate
else
    echo "ERROR: .venv not found. Create it first with: python3 -m venv .venv"
    exit 1
fi

if [ -n "$1" ]; then
    COMMAND_FILES=("$1")
    if [ ! -f "$1" ]; then
        echo "ERROR: Commands file not found: $1"
        exit 1
    fi
else
    shopt -s nullglob
    COMMAND_FILES=(commands_*.txt command_*.txt)
    shopt -u nullglob

    if [ ${#COMMAND_FILES[@]} -eq 0 ]; then
        echo "ERROR: No command files found matching commands_*.txt or command_*.txt"
        exit 1
    fi
fi

if command -v python >/dev/null 2>&1; then
    PYTHON_CMD="python"
elif command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
elif [ -x ".venv/bin/python" ]; then
    PYTHON_CMD=".venv/bin/python"
else
    echo "ERROR: No Python interpreter found in shell or .venv"
    exit 1
fi

OVERALL_STATUS=0
for COMMANDS_FILE in "${COMMAND_FILES[@]}"; do
    echo "Running with $COMMANDS_FILE"
    if [[ "$PYTHON_CMD" == *.exe ]]; then
        "$PYTHON_CMD" main.py "$COMMANDS_FILE" || OVERALL_STATUS=1
    else
        # Convert Windows path separators in command files for POSIX Python runtimes.
        TMP_COMMANDS_FILE=$(mktemp)
        sed -e 's#\.\\#./#g' -e 's#\\#/#g' "$COMMANDS_FILE" > "$TMP_COMMANDS_FILE"
        "$PYTHON_CMD" main.py "$TMP_COMMANDS_FILE" || OVERALL_STATUS=1
        rm -f "$TMP_COMMANDS_FILE"
    fi
done

exit $OVERALL_STATUS


