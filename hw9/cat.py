#!/usr/bin/env python

import argparse
import sys


def print_concat_files(path_to_files):
    """
    Concatenate files and print on the standard output
    @param path_to_files: list, path to files
    @return: stdout concatenated file, str
    """
    for file in path_to_files:
        with open(file) as f:
            sys.stdout.write(f.read())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="concatenate files and print on the standard output")
    parser.add_argument('path_to_files', help="path to files", nargs="+", default=sys.stdin)
    args = parser.parse_args()
    print_concat_files(path_to_files=args.path_to_files)
