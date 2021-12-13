#!/usr/bin/env python
import argparse
import sys
import re


def sort_alphabetical(path_to_file):
    """
    Sort lines of text files in alphanumeric order
    @param path_to_file: path to file
    @return: sorted lines
    """
    all_lines = [line for file in path_to_file for line in file]
    sd_ls = sorted(all_lines, key=lambda x: re.sub('[^A-Za-z0-9]*', '', x).lower())
    for ls in sd_ls:
        sys.stdout.write(ls)
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort lines of text files in alphanumeric order")
    if sys.stdin.isatty():
        parser.add_argument('path_to_file', help="path to file", nargs="+",
                            type=argparse.FileType('r', encoding='UTF-8'), default=sys.stdin)
        args = parser.parse_args()
        sort_alphabetical(path_to_file=args.path_to_file)
    else:
        parser.add_argument('--path_to_file', help="path to file",
                            type=argparse.FileType('r', encoding='UTF-8'), default=sys.stdin)
        args = parser.parse_args()
        sort_alphabetical(path_to_file=[args.path_to_file])
