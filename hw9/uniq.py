#!/usr/bin/env python
import argparse
import sys


def unique(path_to_file, ignore_case):
    """
    Report or omit repeated lines
    @param path_to_file: list, path to file
    @return: None, sys.stdout write unique lines
    """
    # use dict.fromkeys to preserve the order
    if ignore_case:
        all_lines = list(dict.fromkeys([line.strip().lower() for file in path_to_file for line in file]))
    else:
        all_lines = list(dict.fromkeys([line.strip() for file in path_to_file for line in file]))
    for ls in all_lines:
        sys.stdout.write(ls + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="report or omit repeated lines")
    parser.add_argument('-i', '--ignore_case', action='store_true',
                        help="ignore differences in case when comparing")
    if sys.stdin.isatty():
        parser.add_argument('path_to_file', help="path to file", nargs="+",
                            type=argparse.FileType('r', encoding='UTF-8'), default=sys.stdin)
        args = parser.parse_args()
        unique(path_to_file=args.path_to_file, ignore_case=args.ignore_case)
    else:
        parser.add_argument('--path_to_file', help="path to file",
                            type=argparse.FileType('r', encoding='UTF-8'), default=sys.stdin)
        args = parser.parse_args()
        unique(path_to_file=[args.path_to_file], ignore_case=args.ignore_case)
