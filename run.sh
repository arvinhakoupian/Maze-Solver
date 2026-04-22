#!/bin/bash
# Run the application

commands_files =(
    "commands_invalid.txt"
    "commands_missing.txt"
    "commands_unsolvable.txt"
    "commands_no_maze.txt"
    "commands_test.txt"
)

venv="venv"
if [ ! -d "$venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $venv
fi

source $venv/bin/activate
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Running the application..."
for file in "${commands_files[@]}"; do
    echo "Running with $file..."
    python main.py  "$file"
done

echo "All done!"


