from maze_solver import MazeSolver
from tokenizer import parse_tokens


def run_commands(commands_file):
    app = MazeSolver()
    with open(commands_file, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if line == "" or line.startswith("#"):
                continue

            tokens = parse_tokens(line)
            should_quit = app.process_command(tokens)
            if should_quit:
                break
