#!/usr/bin/env python
import sys
import argparse
import os
import shutil


def copy(path_to_input_file, path_to_output_file, recursive):
    """
    Copies the files/directories at the path_to_file (directories only with -r option)
    @param path_to_input_file: list, path to input file/directory
    @param path_to_output_file: str, path to output file/directory
    @param recursive: bool, recursively or not
    @return: None, copies file/directory
    """
    for input_file in path_to_input_file:
        if os.path.isfile(input_file):
            shutil.copy2(input_file, path_to_output_file)
        elif os.path.isdir(input_file):
            if recursive and os.path.exists(path_to_output_file):
                # Copies it with the same name into existing output directory
                shutil.copytree(input_file, path_to_output_file+os.path.sep+os.path.basename(input_file))
            elif recursive and not os.path.exists(path_to_output_file):
                # Copies it with the given name into the directory
                shutil.copytree(input_file, path_to_output_file)
            else:
                sys.stdout.write(f"cp: -r not specified; omitting directory '{input_file}'\n")
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="copy files and directories")
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='copy directories and their contents recursively')
    parser.add_argument('path_to_input_file', help="path to input file", nargs='+', default=sys.stdin)
    parser.add_argument('path_to_output_file', help="path to output file", type=str, default=sys.stdin)
    args = parser.parse_args()
    copy(path_to_input_file=args.path_to_input_file, path_to_output_file=args.path_to_output_file,
         recursive=args.recursive)
