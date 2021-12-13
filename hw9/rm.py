#!/usr/bin/env python

import argparse
import sys
import os
import shutil


def remove(path_to_file, recursive):
    """
    Removes the file/directory at the path_to_file
    @param path_to_file:
    @return:
    """
    if os.path.isfile(path_to_file):
        os.remove(path_to_file)
    elif os.path.isdir(path_to_file):
        if recursive:
            shutil.rmtree(path_to_file)
        else:
            os.rmdir(path_to_file)
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="remove a file or directory")
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='remove directories and their contents recursively')
    parser.add_argument('path_to_file', help="path to file", type=str, default=sys.stdin)
    args = parser.parse_args()
    remove(path_to_file=args.path_to_file, recursive=args.recursive)
