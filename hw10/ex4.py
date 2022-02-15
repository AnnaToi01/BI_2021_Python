from pathlib import Path
import pandas as pd
from Bio import SeqIO
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from Bio.SeqUtils import GC
import itertools


def check_if_None(attribute):
    """
    Checks whether the attribute is already calculated and returns it directly if it is, calculates it in case it is not
    @param attribute: attribute of the class
    @return: attribute
    """

    def decorator_None(func):
        def wrapper_None(self, *args):
            if getattr(self, attribute) is None:
                func(self)
                return getattr(self, attribute)
            else:
                return getattr(self, attribute)

        return wrapper_None

    return decorator_None


class FASTAStats:
    """
    Class for generating statistics about FASTA files
    """

    def __init__(self, path_to_file, save_files=True, output_dir="./"):
        # Path to file
        self.path_to_file = path_to_file
        # Type of the molecule determined after check_type
        self.type = None
        # Total number of sequences, determined after self.count_seq()
        self.num_seq = None
        # Minimal sequence length, determined after self.hist_len_distribution()
        self.min_seq_len = None
        # Maximal sequence length, determined after self.hist_len_distribution()
        self.max_seq_len = None
        # GC content, determined after self.gc_calc()
        self.gc_content = None
        # N (unknown nucleotide) content, determined after self.n_calc()
        self.n_content = None
        # Saves files or not
        self.save_files = save_files
        # Output directory
        self.output_dir = output_dir

    def __str__(self):
        """
        Dunder method to return a human-readable string, e.g. in the print function
        @return: str
        """
        return f"Path to the file: {self.path_to_file}"

    @check_if_None("type")
    def check_type(self):
        """
        Returns the molecule type in the FASTA file: DNA, RNA or protein
        It is assumed, that in unresolved cases (e.g. when no thymine/uracil is present in the nucleotide sequences)
        it is directly classified as DNA.
        @return: self.type - str, denoting the type
        """
        dna_type = {"A", "C", "G", "T", "N"}
        rna_type = {"A", "C", "G", "U", "N"}
        set_unique_elements = set()
        with open(self.path_to_file) as f:
            for nuc_seq in SeqIO.parse(f, "fasta"):
                set_unique_elements.update([element.upper() for element in nuc_seq.seq])
        if set_unique_elements.issubset(dna_type):
            self.type = "DNA"
        elif set_unique_elements.issubset(rna_type):
            self.type = "RNA"
        else:
            self.type = "protein"
        return self.type

    @check_if_None("num_seq")
    def count_seq(self):
        """
        Count the total number of sequences in the FASTA file
        @return: self.num_seq - int
        """
        self.num_seq = 0
        with open(self.path_to_file) as f:
            for nuc_seq in SeqIO.parse(f, "fasta"):
                self.num_seq += 1
        return self.num_seq

    def hist_len_distribution(self, stat="count"):
        """
        Builds a histogram for length distribution of the sequences in the FASTA file
        @param stat: str, "count", "frequency", "probability", "percent" - default "count"
        @return: None,
                 Histogram is saved as .jpg file, if self.save_files = True,
                 and shown directly if self.save_files = False
        """
        seq_len = []
        with open(self.path_to_file) as f:
            for nuc_seq in SeqIO.parse(f, "fasta"):
                seq_len.append(len(nuc_seq.seq))

        self.max_seq_len = max(seq_len)
        self.min_seq_len = min(seq_len)
        plt.figure(figsize=(30, 20), dpi=100)
        sns.set(style='whitegrid')
        sns.histplot(seq_len, stat=stat, binwidth=(self.max_seq_len - self.min_seq_len) / 100,
                     color='purple')
        plt.xlabel("Length of the sequence [bp]")
        plt.suptitle("Histogram of sequence length distribution", y=0.95, x=0.51, fontsize=25)
        plt.title(f"for file {self.path_to_file}", fontsize=20)
        if self.save_files:
            plt.savefig(Path(self.output_dir, Path(self.path_to_file).stem + "_hist_len.jpg"))
            plt.close()
        else:
            plt.show()

    def min_max_seq_len(self):
        """
        Returns minimal and maximal sequence lengths in FASTA file
        @return: self.min_seq_len, self.max_seq_len - tuple of int
        """
        if isinstance(self.min_seq_len, type(None)):
            self.hist_len_distribution()
            return self.min_seq_len, self.max_seq_len
        else:
            return self.min_seq_len, self.max_seq_len

    @check_if_None("gc_content")
    def gc_calc(self):
        """
        Calculates the GC content as percent (makes sense for RNA and DNA sequences)
        @return: self.gc_content - float
        """
        gc_content_list = []
        with open(self.path_to_file) as f:
            for nuc_seq in SeqIO.parse(f, "fasta"):
                gc_content_list.append(GC(nuc_seq.seq))

        self.gc_content = np.round(np.mean(gc_content_list), 2)
        return self.gc_content

    @check_if_None("n_content")
    def n_calc(self):
        """
        Calculates the N content as percent (makes sense for RNA and DNA sequences)
        @return: self.n_content - float
        """
        n_content_list = []
        with open(self.path_to_file) as f:
            for nuc_seq in SeqIO.parse(f, "fasta"):
                n_content_list.append((nuc_seq.seq).count('N') / len(nuc_seq.seq))
        self.n_content = np.round(np.mean(n_content_list), 2)
        return self.n_content

    def count_kmers(self):
        """
        Builds a histogram of percents of 4-mers for RNA and DNA sequences
        @return: None,
                 Histogram is saved as .jpg file, if self.save_files = True,
                 and shown directly if self.save_files = False
        """
        pos_kmers = {}
        types = {"DNA": "ACGT", "RNA": "ACGU"}
        for kmer in itertools.product(types[self.type], types[self.type], repeat=2):
            pos_kmers["".join(kmer)] = 0

        with open(self.path_to_file) as f:
            for nuc_seq in SeqIO.parse(f, "fasta"):
                for i in range(len(nuc_seq.seq) - 3):
                    kmer = str(nuc_seq.seq[i:i + 4]).upper()
                    if "N" not in kmer:  # We don't take N into account, because the histogram gets too large
                        pos_kmers[kmer] += 1
        sns.reset_orig()
        plt.figure(figsize=(30, 20), dpi=100)
        values = np.array(list(pos_kmers.values()))
        sum_values = np.sum(values)
        per_values = values / sum_values * 100
        plt.bar(pos_kmers.keys(), per_values, align='center', color=plt.get_cmap("magma").colors)
        plt.xticks(rotation=90, fontsize=4)
        plt.suptitle("4-mer Distribution", y=0.95, x=0.51, fontsize=25)
        plt.title(f"for file {self.path_to_file}", fontsize=20)
        if self.save_files:
            plt.savefig(Path(self.output_dir, Path(self.path_to_file).stem + "_4mers.jpg"))
            plt.close()
        else:
            plt.show()

    def statistics(self):
        """
        Runs the whole statistical analysis for the FASTA file
        @return: self.type, self.num_seq, self.min_seq_len, self.max_seq_len, self.gc_content, self.n_content
                 - str, int, int, int, float, float
        """
        self.check_type()
        self.count_seq()
        self.hist_len_distribution()
        self.gc_calc()
        self.n_calc()
        self.count_kmers()

        if self.save_files:
            data = {
                "Type": self.type,
                "Count of the sequences": self.num_seq,
                "Minimal sequence length:": self.min_seq_len,
                "Maximal sequence length": self.max_seq_len,
                "GC content": self.gc_content,
                "N content": self.n_content
            }
            pd.DataFrame.from_dict(data, orient='index').to_csv(Path(self.output_dir,
                                                                     Path(self.path_to_file).stem + "_statistics.csv"),
                                                                header=False)
        else:
            print(self)
            print(f"Type of the file: {self.type}")
            print(f"Count of the sequences: {self.num_seq}")
            print(f"Minimal sequence length: {self.min_seq_len} and maximal: {self.max_seq_len}")
            print(f"GC content: {self.gc_content}")
            print(f"N content: {self.n_content}")

        return self.type, self.num_seq, self.min_seq_len, self.max_seq_len, self.gc_content, self.n_content


fa = FASTAStats("./example_data/Daucus_carota.ASM162521v1.cdna.all.fa", save_files=True)
print(fa)
print(fa.check_type())
print(fa.count_seq())
fa.hist_len_distribution(stat="percent")
print(fa.min_max_seq_len())
print(fa.gc_calc())
print(fa.n_calc())
fa.count_kmers()


dm6 = FASTAStats("./example_data/dm6.rRNA.fa", output_dir="./example_data")
print(dm6.check_type())
dm6.statistics()

peptides = FASTAStats('./example_data/peptides.fa', output_dir="./example_data")
print(peptides.check_type())
