import sys

from command_runner import run_commands


def main():
    if len(sys.argv) != 2:
        print("USAGE: <program> <commands_file>")
        return 1

    commands_file = sys.argv[1]
    try:
        run_commands(commands_file)
    except Exception:
        print("USAGE: <program> <commands_file>")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())