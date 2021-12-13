#!/usr/bin/env python
import argparse
import sys
import os


def list_dir(path_to_dir, all):
    """
    Lists the content of the directory
    @param path_to_dir: str, path to directory
    @return: contents, str, separated by " "
    """
    files = sorted(os.listdir(path_to_dir), key=str.lower)
    if all:
        for f in files:
            if not f.startswith("."):
                sys.stdout.write(f + "\n")
    else:
        sys.stdout.write(".\n..\n")
        for f in files:
            sys.stdout.write(f + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="list directory contents")
    parser.add_argument("-a", "--all", action='store_false', help="do not ignore entries starting with .")
    parser.add_argument("dir", help="path to directory", nargs='?', const="./", type=str)
    args = parser.parse_args()
    list_dir(args.dir, all=args.all)
