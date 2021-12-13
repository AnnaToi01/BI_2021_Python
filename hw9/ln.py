#!/usr/bin/env python
import argparse
import sys
import shutil
import os


def link(path_to_input_file, path_to_output_file, symbolic):
    """
    Copies the file/directory at the path_to_file (directories only with -r option)
    @param path_to_input_file: str, path to input file/directory
    @param path_to_output_file: str, path to output file/directory
    @param symbolic: bool, create symbolic links instead of hard links
    @return: None, copies file/directory
    """
    if symbolic:
        os.symlink(path_to_input_file, path_to_output_file)  # symbolic link
    else:
        os.link(path_to_input_file, path_to_output_file)  # hard link
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="make links between files")
    parser.add_argument('-s', '--symbolic', action='store_true',
                        help="make symbolic links instead of hard links")
    parser.add_argument('path_to_input_file', help="path to input file", type=str, default=sys.stdin)
    parser.add_argument('path_to_output_file', help="path to output file", type=str, default=sys.stdin)
    args = parser.parse_args()
    link(path_to_input_file=args.path_to_input_file, path_to_output_file=args.path_to_output_file,
         symbolic=args.symbolic)

