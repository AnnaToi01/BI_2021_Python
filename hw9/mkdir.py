#!/usr/bin/env python
import sys
import os
import argparse
import shutil

def add_to_path(path_to_directory_with_scripts, path_directory):
    for file in os.listdir(path_to_directory_with_scripts):
        if file.endswith(".py"):
            path_to_script = os.path.join(os.path.abspath(path_to_directory_with_scripts), file)
            shutil.copy(path_to_script, path_directory)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Appends all the scripts in the given directory to the PATH")
    parser.add_argument('path_to_directory_with_scripts', help="path to directory with scripts",
                        type=str, default=sys.stdin)
    parser.add_argument('-P', '--PATH_directory', help="PATH directory to place the scripts, "
                                                       "default is the first directory in the PATH",
                        type=str, default=f"{os.environ['PATH'].split(os.pathsep)[0]}")
    args = parser.parse_args()
    add_to_path(args.path_to_directory_with_scripts, path_directory=args.PATH_directory)
