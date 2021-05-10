import argparse
import pathlib
import sys

from . import __version__
from .rptree import DirectoryTree


def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)

    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()

    tree = DirectoryTree(root_dir)
    tree.generate()


def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="tree",
        description="Cherry Tree, a directory tree generator",
        epilog="Thanks for using Cherry Tree!",
    )
    parser.version = f"Cherry Tree v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        # number of aruments we can take, ? means One argument will be consumed from the command line if possible, and produced as a single item. If no command-line argument is present, the value from default will be produced.
        nargs="?",
        default=".",  # default value if one is not provided, a single . represents the current directory
        help="Generate a full directory tree starting at ROOT_DIR",
    )

    return parser.parse_args()
