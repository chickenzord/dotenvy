import argparse
import os
import subprocess
import sys

import dotenvy


def main(stdout=sys.stdout):
    description = (
        "Run any shell command with environment variables loaded from DotEnv file"
    )
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--file",
        type=str,
        default=".env",
        help="dotenv file path (default: .env)",
    )
    parser.add_argument(
        "commands",
        type=str,
        nargs="+",
        help="command to run",
    )
    args = parser.parse_args()

    try:
        env = os.environ.copy()
        env.update(dotenvy.read_file(args.file))
    except OSError as e:
        sys.exit(f"Cannot load dotenv: {args.file}\n{e}")

    subprocess.call(" ".join(args.commands), env=env, shell=True, stdout=stdout)


if __name__ == "__main__":  # pragma: no cover
    main()
