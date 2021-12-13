#!/usr/bin/env python
import argparse
import sys


def print_last_lines(path_to_file, lines):
    """
    Print last lines of the file
    @param path_to_file: str, path to file
    @param lines: int, number of lines
    @return: sys.stdout writes last lines
    """
    all_lines = path_to_file.readlines()
    n_lines = len(all_lines)
    last_lines = all_lines[n_lines - lines:]
    for line in last_lines:
        sys.stdout.write(line)


def print_from_line(path_to_file, lines):
    """
    Print file from a specific line
    @param path_to_file: str, path to file
    @param lines: int, number of line
    @return: sys.stdout writes the lines
    """
    all_lines = path_to_file.readlines()
    last_lines = all_lines[lines-1:]
    for line in last_lines:
        sys.stdout.write(line)


def print_file_name(path_to_file):
    """
    Prints the file name
    @param path_to_file: str, path_to_file
    @return: sys.stdout ==> path_to_file <==\n
    """
    sys.stdout.write("==> " + path_to_file.name + "<==\n")


def tail(path_to_files, lines):
    """
    Outputs the last part of files, as tail in UNIX
    @param path_to_files: list, path to files
    @param lines: str, number of lines
    @return: sys.stdout - writes the contents of files
    """
    if lines.count("+") == 1:
        lines = int(lines[1:])
        for file in path_to_files:
            if len(path_to_files) > 1:
                print_file_name(path_to_file=file)
            print_from_line(file, lines)
    else:
        lines = int(lines)
        for file in path_to_files:
            if len(path_to_files) > 1:
                print_file_name(path_to_file=file)
            print_last_lines(file, lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="output the last part of files")
    parser.add_argument('-n', '--lines',  nargs='?', type=str, const="10", default="10",
                        help='output the last NUM lines, instead of the last  10;  '
                             'or  use  -n +NUM to output starting with line NUM')
    if sys.stdin.isatty():
        parser.add_argument('path_to_files', help="path to files", nargs="+",
                            type=argparse.FileType('r', encoding='UTF-8'), default=sys.stdin)
        args = parser.parse_args()
        tail(path_to_files=args.path_to_files, lines=args.lines)
    else:
        parser.add_argument('--path_to_files', help="path to files", nargs="+", default=sys.stdin)
        args = parser.parse_args()
        tail(path_to_files=[args.path_to_files], lines=args.lines)
