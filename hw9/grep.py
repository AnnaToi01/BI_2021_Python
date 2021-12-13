#!/usr/bin/env python
import argparse
import sys
import re


def find_pattern(path_to_file, pattern, multiple_files=False,
                 ignore_case=False, invert_match=False, count=False):
    """
    Find patterns in the line
    @param path_to_file: str, path_to_file
    @param pattern: str, pattern
    @param multiple_files: bool, were multiple files given or not
    @param ignore_case: bool, ignore case or not, default=False
    @param invert_match: bool, invert match or not, default=False
    @param count: bool, only count the matches, default=False
    @return: sys.stdout writes the match
    """
    if invert_match:
        pattern = "^(?!.*?"+pattern + ").*"
    n = 0
    for line in path_to_file:
        if ignore_case:
            if re.search(pattern, line, re.I):
                if count:
                    n += 1
                else:
                    if multiple_files:
                        sys.stdout.write(path_to_file.name + ":")
                    sys.stdout.write(line)
        else:
            if re.search(pattern, line):
                if count:
                    n += 1
                else:
                    if multiple_files:
                        sys.stdout.write(path_to_file.name + ":")
                    sys.stdout.write(line)
    return n


def grep(path_to_files, pattern,
         ignore_case=False, invert_match=False, count=False):
    """
    Finds the patterns in multiple files and writes them to stdout
    @param path_to_files: list, path to the files
    @param pattern: str, python regex pattern
    @param ignore_case: bool, ignore case or not, default=False
    @param invert_match: bool, invert match or not, default=False
    @param count: bool, only count the matches, default=False
    @return: writes the matches to stdout
    """
    if len(path_to_files) == 1:
        n = find_pattern(path_to_files[0], pattern=pattern, ignore_case=ignore_case,
                         invert_match=invert_match, count=count)
        if count:
            sys.stdout.write(str(n)+"\n")
    else:
        for file in path_to_files:
            n = find_pattern(file, pattern=pattern, multiple_files=True, ignore_case=ignore_case,
                             invert_match=invert_match, count=count)
            if count:
                sys.stdout.write(file.name + ":")
                sys.stdout.write(str(n)+"\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="grep  searches  for  a pattern  in  each  FILE.  "
                                                 "grep  prints  each  line "
                                                 "that  matches a pattern.  Typically PATTERNS "
                                                 "should be quoted  with single quotes when grep "
                                                 "is used.")
    parser.add_argument('pattern', type=str,
                        help="python regex pattern")
    parser.add_argument('-v', '--invert_match', action='store_true',
                        help="Invert the sense of matching, to select non-matching lines.")
    parser.add_argument('-i', '--ignore_case', action='store_true',
                        help="Ignore  case  distinctions  in  patterns and input data, so that "
                             "characters that differ only in case match each other.")
    parser.add_argument('-c', '--count', action='store_true',
                        help="print a count of matching lines for each input file.")

    if sys.stdin.isatty():
        parser.add_argument('path_to_files', help="path to files", nargs="+",
                            type=argparse.FileType('r', encoding='UTF-8'), default=sys.stdin)
        args = parser.parse_args()
        grep(path_to_files=args.path_to_files, pattern=args.pattern, ignore_case=args.ignore_case,
             invert_match=args.invert_match, count=args.count)
    else:
        parser.add_argument('--path_to_files', help="path to files", nargs="+", default=sys.stdin)
        args = parser.parse_args()
        grep(path_to_files=[args.path_to_files], pattern=args.pattern, ignore_case=args.ignore_case,
             invert_match=args.invert_match, count=args.count)
