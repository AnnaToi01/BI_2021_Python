#!/usr/bin/env python
import argparse
import sys


def count_lines(txt):
    """
    Count lines of text
    @param txt: str, text
    @return: count_of_lines: int, count of lines
    """
    return txt.count("\n")


def count_words(txt):
    """
    Count words of text
    Definition of word in wc - w:
    A word is defined to be a string of alphanumerics,
    ignoring any backspaces, underlines, apostrophes, dashes, or pluses.
    @param txt: str, text
    @return: count_of_words: int, count of words
    """
    return sum([1 for line in txt.split("\n") for word in line.split()])


def count_bytes(txt):
    """
    Count bytes in txt
    @param txt: str, text
    @return: count_of_bytes: int, count of bytes
    """
    return len(txt.encode('utf-8'))


def output(txt, func_dic, no_param_end=" ", param_end=" "):
    """
    Print newline, word, and byte counts for a text
    @param txt: str, text
    @param args: arguments from argparse
    @param no_param_end: str, separator of output for input without parameters
    @param param_end: str, separator of output for input with parameters
    @return: None, print the output
    """
    if all(func_dic.values()):
        for key in func_dic.keys():
            sys.stdout.write(no_param_end + str(key(txt)))
    else:
        for key, value in func_dic.items():
            if not value:
                sys.stdout.write(str(key(txt)) + param_end)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="print newline, word, and byte counts for a file")
    parser.add_argument('-l', '--lines', action='store_false', help='print the newline counts')
    parser.add_argument('-w', '--words', action='store_false', help='print the word counts')
    parser.add_argument('-c', '--bytes', action='store_false', help='print the byte counts')

    if sys.stdin.isatty():
        parser.add_argument('path_to_file', help="path to file",
                            type=argparse.FileType('r', encoding='UTF-8'), default=sys.stdin)
        args = parser.parse_args()
        file = args.path_to_file.read()
        func_dic = {
            count_lines: args.lines,
            count_words: args.words,
            count_bytes: args.bytes
        }
        output(file, func_dic)
        sys.stdout.write(" " + args.path_to_file.name + "\n")
    else:
        parser.add_argument('--path_to_file', help="path to file", default=sys.stdin)
        args = parser.parse_args()
        file = args.path_to_file.read()
        func_dic = {
            count_lines: args.lines,
            count_words: args.words,
            count_bytes: args.bytes
        }
        output(file, func_dic, no_param_end="\t", param_end="\t")
        sys.stdout.write("\n")
