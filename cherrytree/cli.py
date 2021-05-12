import argparse
import pathlib
import sys

from . import __version__
from .cherrytree import DirectoryTree


def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)

    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()

    tree = DirectoryTree(root_dir, dir_only=args.dir_only,
                         output_file=args.output_file)
    tree.generate()


def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="tree",
        description="Cherry Tree, a directory tree generator",
        epilog="Thanks for using Cherry Tree!",
    )
    parser.version = f"Cherry Tree v{__version__}"

    parser.add_argument(
        "-d",
        "--dir-only",
        action="store_true",
        help="Generate a directory-only tree",
    )
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        # number of aruments we can take, ? means One argument will be consumed from the command line if possible, and produced as a single item. If no command-line argument is present, the value from default will be produced.
        nargs="?",
        default=".",  # default value if one is not provided, a single . represents the current directory
        help="Generate a full directory tree starting at ROOT_DIR",
    )
    parser.add_argument(
        "-o",
        "--output-file",
        metavar="OUTPUT_FILE",
        nargs="?",
        default=sys.stdout,
        help="Generate a full directory tree and save it to a file"
    )

    return parser.parse_args()
