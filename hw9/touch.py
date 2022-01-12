#!/usr/bin/env python
import argparse
import sys
from pathlib import Path


def touch(path_to_files):
    """
    Changes the timestamps of the files
    @param path_to_files: list, path to files
    @return: None
    """
    for file in path_to_files:
        Path(file).touch()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="change file timestamps")
    parser.add_argument('path_to_files', help="path to files", nargs="+", default=sys.stdin)
    args = parser.parse_args()
    touch(path_to_files=args.path_to_files)
