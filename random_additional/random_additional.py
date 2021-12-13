import random
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import math
import matplotlib.ticker as mticker
import itertools


# When the jump is 1/3 and the point can also jump towards the midpoints
# of the four sides, the chaos game generates the Sierpinski carpet:
def random_sierpinski_square(cycles, color, output_dir):
    """
    Draws Sierpinski's carpet by random method
    @param cycles: int, number of cycles
    @param color: str, color of the graph
    @param output_dir: output directory path
    @return: plot, saved as random_sierpinski_carpet.jpg
    """

    vertices = np.array([
        [0, 0],
        [0, 1],
        [1, 1],
        [1, 0],
    ])

    coordinates = np.zeros((cycles, 2))
    coordinates[0, :] = (random.random(), random.random())
    for i in range(cycles):
        v_or_m = random.randint(0, 1)
        vertex_index = random.randint(0, 3)
        if v_or_m == 0:
            coordinates[i, :] = 1 / 3 * (coordinates[i - 1, :] + vertices[vertex_index])
        else:
            midpoint = (vertices[vertex_index] + vertices[(vertex_index + 1) % 4]) / 2
            coordinates[i, :] = 1 / 3 * (coordinates[i - 1, :] + midpoint)

    plt.scatter(coordinates[:, 0], coordinates[:, 1], c=color, s=0.5)
    plt.title("Sierpinski's carpet")
    plt.savefig(Path(output_dir, "random_sierpinski_square.jpg"))
    plt.show()


def change_read(read, subs, indels):
    """
    Generates potential sequenced read
    @param read: str, perfect read sequence
    @param subs: list, 0s and 1s, 0 - no substitution, 1 - substitution
    @param indels: list, 0s and 1s, 0 - no indel, 1 - insertion, 2 - deletion
    @return: final_read: str, sequenced read
    """
    nucleotides = ["A", "C", "G", "T"]
    # Construct read from scratch
    final_read = ""
    for i, nc in enumerate(read):
        if indels[i] == 2:  # we delete element in any case if there's 2
            continue
        if subs[i] == 1:  # Substitution - take any other nucleotide than we have, equal probability
            final_read += random.choice([i for i in nucleotides if i != nc])[0]
        else:  # No substitution -> add the same nucleotide
            final_read += nc
        if indels[i] == 1:  # if we have insertion - add any random nucleotide
            final_read += random.choice([nucleotides])[0]
    return final_read


def sequencing_simulator(sequence, coverage, read_length):
    sequence_length = len(sequence)
    # Take all possible reads (I guess something like k-mers)
    possible_reads = [sequence[i:(i + read_length)] for i in range(sequence_length - read_length + 1)]
    # Randomly select the reads according to the coverage
    reads = random.choices(possible_reads, k=sequence_length * coverage)
    substitution_rates = {
        "A": 0.004,
        "C": 0.004,
        "G": 0.004,
        "T": 0.008
    }
    # Error per base for indel
    indel_rates = 2.8 * 10 ** (-6)
    final_reads = []
    for i, read in enumerate(reads):
        # Create a list of substitutions for each nucleotide, 0 - no subst., 1 - subst.
        subs = list(itertools.chain(*[random.choices([0, 1],
                                                     weights=[1 - substitution_rates[nc], substitution_rates[nc]])
                                      for nc in read]))
        # Create a list of indel for each nucleotide, 0 - no indel, 1 - insertion, 2 - deletion
        indels = list(itertools.chain(*[random.choices([0, 1, 2],
                                                       weights=[1 - 2 * indel_rates, indel_rates, indel_rates])
                                        for nc in read]))
        final_reads.append(change_read(read, subs, indels))
    return final_reads


# Modified from FASTQC project
def calculate_read_length(reads):
    """
    Calculate read length distribution
    :param path_to_file: str, path to fastq file
    :return:
            length_dic: dic, read_length:count
            max_length: int, maximum read length
            min_length: int, minimum read length
            total_reads: int, total count of reads
            gc_content_list: list, GC content per read (%)
            mean_gc_content: float, average GC content
            nucleotide_per_position_dic: dic, Position in read (bp): Nucleotide in this position per read
    """
    length_distribution_dic = {}
    for sequence in reads:
        length = len(sequence)
        length_distribution_dic[length] = length_distribution_dic.get(length, 0) + 1
    return length_distribution_dic


def plot_length_distribution(length_distribution_dic, output_dir):
    """
    Plot Sequence length distribution
    :param length_distribution_dic: dictionary, read_length:count
    :param output_dir: directory where picture will be stored
    :return: plot
    """
    x = [int(key) for key in length_distribution_dic.keys()]
    min_x = min(x) - 1
    max_x = max(x) + 1
    x.append(min_x)
    x.append(max_x)
    y = [int(value) for value in length_distribution_dic.values()]
    y.append(0)
    y.append(0)
    max_y = max(y)
    x, y = zip(*sorted(zip(x, y)))
    _, ax = plt.subplots(figsize=(14, 10))
    plt.plot(x, y, label="Sequence length", color='r')
    plt.grid(axis="x")
    if max_x - min_x < 20:
        step = 1
    else:
        step = math.ceil((max_x - min_x) / 10)
    xticks = np.arange(min_x, max_x + step, step=step)
    for x0, x1 in zip(xticks[::2], xticks[1::2]):
        plt.axvspan(x0 + step / 2, x1 + step / 2, color='black', alpha=0.1, zorder=0)
    plt.xticks(xticks)
    difference_yticks = max_y // 10
    digits_zero = 1
    while difference_yticks // 10 > 1:
        difference_yticks = difference_yticks // 10
        digits_zero *= 10
    step_y = math.floor(max_y / difference_yticks / digits_zero) * digits_zero
    plt.yticks(np.arange(0, math.ceil(max(y) / 1000) * 1000 + step_y, step=step_y))
    ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())

    ax.ticklabel_format(style='plain', axis='y')
    leg = plt.legend(handlelength=0, loc="upper right", borderaxespad=0, prop={'size': 14})
    for line, text in zip(leg.get_lines(), leg.get_texts()):
        text.set_color(line.get_color())
    plt.title("Distribution of sequence lengths over all sequences", fontsize=14)
    plt.xlabel("Sequence length", fontsize=14)
    plt.savefig(Path(output_dir, 'sequence_length_distribution.png'))
    plt.show()


if __name__ == "__main__":
    output_dir = "./"
    cycles = 10000
    random_sierpinski_square(cycles=cycles, color="red", output_dir=output_dir)
    sequence = "ACGTAGCTGATGCTGATGTGTGATCGTAGTCGTGATGTAGTGCTGGATGTGACTGTAGTCGTAGTGCTAGCTGATCGTAGCTGACT"
    reads = sequencing_simulator(sequence=sequence, coverage=30, read_length=20)
    length_distribution_dic = calculate_read_length(reads)
    plot_length_distribution(length_distribution_dic, output_dir="./")
