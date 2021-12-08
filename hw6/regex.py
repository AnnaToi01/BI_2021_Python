import re
import matplotlib.pyplot as plt
import numpy as np
import urllib.request as url
from pathlib import Path
import matplotlib.ticker as mticker


def download_files_from_http(link, output_dir):
    """
    Downloads files from the link, placing them into directory
    @param link: str, https link to file
    @param output_dir: str, output directory
    @return: Saves file and returns its path
    """
    path_to_file = Path(output_dir, link.split("/")[-1])
    url.urlretrieve(link, filename=path_to_file)
    return path_to_file


def exercise_1(path_to_file, file_out, output_dir):
    """
    Parses file and replaces all ftp links with ftps generating file_out
    @param path_to_file: str, path to file
    @param file_out: str, name of generated file
    @param output_dir: str, output directory
    @return: None, generates ouput_dir/file_out
    """
    with open(path_to_file, 'r') as reference, open(Path(output_dir, file_out), 'w') as after:
        content = reference.read()
        pattern = re.compile(r'\bftp[.\w/]+\b')
        matches = pattern.findall(content)
        after.write("\n".join(matches))


def exercise_2_digits(path_to_file, file_out, output_dir):
    """
    Extracts all numbers written in digits from the path_to_file
    @param path_to_file: str, path to file
    @param file_out: str, name of generated file
    @param output_dir: str, output directory
    @return: None, generates ouput_dir/file_out
    """
    pattern = re.compile(r'\d+[.]?\d*')
    with open(path_to_file, "r") as f, open(Path(output_dir, file_out), 'w') as after:
        contents = f.read()
        matches = pattern.findall(contents)
        for match in matches:
            after.write(match + "\n")
    return

def exercise_2_digits_words(path_to_file, file_out, output_dir):
    """
    Extracts all numbers written in digits and words (English) from the path_to_file
    @param path_to_file: str, path to file
    @param file_out: str, name of generated file
    @param output_dir: str, output directory
    @return: None, generates ouput_dir/file_out
    """
    numbers = (r"(?x)          # Turn on Verbose" "\n"
               r"                (" "\n"
               r"                  \b\d+[.]?\d*|        # digits" "\n"
               r"                  \b                           " "\n"
               r"                  (?:" "\n"
               r"                      one|two|three|four|five|six|seven|eight|nine|ten| " "\n"
               r"                      eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|" "\n"
               r"                      nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|" "\n"
               r"                      hundred|thousand" "\n"
               r"                  )             # numbers as words" "\n"
               r"                  -?" "\n"
               r"                  (?:" "\n"
               r"                      one|two|three|four|five|six|seven|eight|nine|ten| " "\n"
               r"                      eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|" "\n"
               r"                      nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|" "\n"
               r"                      hundred|thousand" "\n"
               r"                  )*           # Specifying, that they might be separated by hyphen" "\n"
               r"                  \b            " "\n"
               r"    )")
    pattern = re.compile(numbers, re.I)
    with open(path_to_file, "r") as f, open(Path(output_dir, file_out), 'w') as after:
        contents = f.read()
        matches = pattern.findall(contents)
        for match in matches:
            after.write(match + "\n")
    return


def exercise_3(path_to_file, file_out, output_dir):
    """
    Extracts words containing a (irrespective of case) from path_to_file
    @param path_to_file: str, path to file
    @param file_out: str, name of generated file
    @param output_dir: str, output directory
    @return: None, generates ouput_dir/file_out
    """
    pattern = re.compile(r"\b[\w.']*a[\w.']*\b", re.I)
    with open(path_to_file, "r") as f, open(Path(output_dir, file_out), 'w') as after:
        contents = f.read()
        matches = pattern.findall(contents)
        for match in matches:
            after.write(match + "\n")
    return


def exercise_4(path_to_file, file_out, output_dir):
    """
    Extracts exclamatory sentences into a file from path_to_file
    @param path_to_file: str, path to file
    @param file_out: str, name of generated file
    @param output_dir: str, output directory
    @return: None, generates ouput_dir/file_out
    """
    pattern = re.compile(r'([A-Z][^.!?]*[!])', re.I)
    with open(path_to_file, "r") as f, open(Path(output_dir, file_out), 'w') as after:
        contents = f.read()
        matches = pattern.findall(contents)
        for match in matches:
            after.write(match + "\n")
    return


def exercise_5(path_to_file, file_out, figure_out, output_dir):
    """
    Extracts all words from path_to_file and writes them into file_out
    Generate a histogram of distribution of unique words in path_to_file
    @param path_to_file: str, path to file
    @param file_out: str, name of generated file
    @param figure_out: str, name of generated figure
    @param output_dir: str, output directory
    @return: None, generates ouput_dir/file_out and ouput_dir/figure_out
    """
    pattern = re.compile(r"\b\w+([.']?\w*)*\b", re.I)
    with open(path_to_file, "r") as f, open(Path(output_dir, file_out), 'w') as after:
        contents = f.read()
        matches = pattern.finditer(contents)
        for match in matches:
            after.write(match.group(0) + "\n")

    with open(Path(output_dir, file_out), 'r') as f:
        txt = f.read().lower()
        words = txt.split()
        uniq = set(words)
        length_ls = []
        for word in uniq:
            length_ls.append(len(word))
        plt.hist(length_ls, histtype='bar', color="purple", edgecolor="white",
                 alpha=0.3, bins=range(min(length_ls), max(length_ls)),
                 weights=np.ones(len(length_ls)) / len(length_ls))
        plt.gca().yaxis.set_major_formatter(mticker.PercentFormatter(1))
        plt.grid(axis="y")
        plt.xticks(np.arange(max(length_ls) + 1))
        plt.xlabel("Length of word")
        plt.ylabel("Frequency in percentage")
        plt.title("Distribution of length of words in text 2340AD")
        plt.savefig(Path(output_dir, figure_out))
        plt.show()
    return


if __name__ == "__main__":
    output_dir = "./"
    # Exercise 1
    link1 = "https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references"
    path_to_file1 = download_files_from_http(link=link1, output_dir=output_dir)
    exercise_1(path_to_file=path_to_file1, file_out="fttps", output_dir=output_dir)
    # Exercise 2
    link2 = "https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD"
    path_to_file2 = download_files_from_http(link=link2, output_dir=output_dir)
    # Numbers as digits
    exercise_2_digits(path_to_file=path_to_file2, file_out="numbers_digits.txt", output_dir=output_dir)
    # Numbers as words
    exercise_2_digits_words(path_to_file=path_to_file2, file_out="numbers_digits_words.txt", output_dir=output_dir)
    # Exercise 3
    # Words separated by hyphen count as two, see line 145 in 2430AD
    exercise_3(path_to_file=path_to_file2, file_out="words_with_a.txt", output_dir=output_dir)
    # Exercise 4
    exercise_4(path_to_file=path_to_file2, file_out="exclamatory_sentences.txt", output_dir=output_dir)
    # Exercise 5
    exercise_5(path_to_file=path_to_file2, file_out="all_words.txt", figure_out="histogram_length_distribution.png",
               output_dir=output_dir)
