# Standard libraries
import argparse
from collections import Counter
import concurrent.futures

# Third party imports
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


def fasta_reader(path_to_file: str, threads: int) -> None:
    """
    Reads a FASTA file and counts the number of symbols in each record
    @param path_to_file: str, path to FASTA file
    @param threads: str, number of threads
    @return: None, prints the results
    """
    # Opens the FASTA file and the processes
    with open(path_to_file) as handle, concurrent.futures.ProcessPoolExecutor(max_workers=threads) as executor:
        executor.map(rec_symbol_counter, SeqIO.parse(handle, "fasta"))


def rec_symbol_counter(rec: SeqRecord):
    """
    Counts the number of symbols of a nucleotide FASTA sequence record
    @param rec: Bio.SeqRecord.SeqRecord, FASTA record
    @return: None, prints the results
    """
    # Counts the symbols
    symbol_count = dict(Counter(rec.seq))

    # Generates output string
    symbol_str = ", ".join(f"{key}={value}" for key, value in symbol_count.items())
    print(f"Contig {rec.id + ':':<20}{symbol_str}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Counts the number of symbols in a FASTA file")

    # Input file
    parser.add_argument("-f", "--fasta", help="Path to input FASTA file")

    # Number of threads
    parser.add_argument("-t", "--threads", type=int, default=1, help="Number of threads")

    # Parsing all the arguments
    args = parser.parse_args()

    # Print results
    fasta_reader(args.fasta, args.threads)
