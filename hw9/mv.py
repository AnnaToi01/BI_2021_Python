#!/usr/bin/env python
import sys
import argparse
import shutil


def move(path_to_input_file, path_to_output_file):
    """
    Copies the file/directory at the path_to_file (directories only with -r option)
    @param path_to_input_file: path to input file/directory
    @param path_to_output_file: path to output file/directory
    @return: None, copies file/directory
    """
    for input_file in path_to_input_file:
        shutil.move(input_file, path_to_output_file)
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="move (rename) files")
    parser.add_argument('path_to_input_file', help="path to input file", nargs='+', default=sys.stdin)
    parser.add_argument('path_to_output_file', help="path to output file", type=str, default=sys.stdin)
    args = parser.parse_args()
    move(path_to_input_file=args.path_to_input_file, path_to_output_file=args.path_to_output_file)
