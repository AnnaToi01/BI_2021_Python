#!/usr/bin/env python

import argparse
import sys
import os


def create_directory(path_to_directory, parents, verbose):
    """
    Makes directories
    @param path_to_directory: list, path to directory
    @param parents: bool, True - can create directory trees, False - only one directory at a time
    @param verbose: bool, print a message for each created directory
    @return:
    """
    if parents:
        printed = []
        for dir in path_to_directory:
            os.makedirs(dir, exist_ok=True)  # mkdir -p raises no Error when the directory exists
            if verbose:
                for i in range(len(dir.split(sep=os.sep))):
                    created = os.sep.join(dir.split(sep=os.sep)[:i + 1])
                    if created not in printed:
                        sys.stdout.write(f"mkdir: created directory '{created}'\n")
                    printed.append(created)
    else:
        for dir in path_to_directory:
            os.mkdir(dir)
            if verbose:
                sys.stdout.write(f"mkdir: created directory '{dir}'\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="make directories")
    parser.add_argument('-p', '--parents', action='store_true',
                        help='no error if existing, make parent directories as needed')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='print a message for each created directory')
    parser.add_argument('path_to_directory', help="path to directory", nargs='+', type=str, default=sys.stdin)
    args = parser.parse_args()
    create_directory(path_to_directory=args.path_to_directory, parents=args.parents, verbose=args.verbose)
