import random
from typing import Any, Callable, Iterable, List


# Exercise 1
def fasta_reader(path_to_file: str, include_gt_sign: bool = True):
    """
    Generator
    Read FASTA file, return sequence id and sequence as tuple.

    @param path_to_file: str, path to FASTA file
    @param include_gt_sign: bool, true to return id with > and false to return id without >
    @return: id_, seq tuple
    """
    with open(path_to_file) as fasta_file:
        sequence = ""
        id_ = ""
        for line in fasta_file:
            # ID line
            if line.startswith(">"):
                # If FASTA sequence is not empty - get id and sequence
                if sequence:
                    yield id_, sequence
                    # Sequence reset
                    sequence = ""

                # ID definition - include >?
                if include_gt_sign:
                    id_ = line.strip()
                else:
                    id_ = line.strip().lstrip(">")

                continue
            # Sequence line
            else:
                sequence += line.strip()
                continue
        else:
            yield id_, sequence


# Exercise 2
class FaultyAASeqReader:
    """A class that iterates over sequences in a FASTA file and randomly changes them."""

    # List of all amino acids (one-letter-code)
    AA_list = ['C', 'D', 'S', 'Q', 'K', 'I', 'P', 'T', 'F', 'N', 'G', 'H', 'L', 'R', 'W', 'A', 'V', 'E', 'Y', 'M']

    def __init__(self, path_to_file: str, random_change_probability: float = 0.9):
        """
        FaultyAASeqReader class constructor.

        @param path_to_file: str, path to FASTA file
        @param random_change_probability: float, probability of how often random FASTA sequence is changed
        """
        self.path_to_file = path_to_file
        self.seq_index = 0
        self.sequences = self.get_sequences()
        self.random_change_probability = random_change_probability

    def __iter__(self):
        """
        Return an iterator for the self object.

        @return: self
        """
        return self

    def __next__(self) -> str:
        """
        Return the next item, here sequence, from the iterator (indefinitely).

        @return: sequence, str, modified/not modified sequence
        """
        try:
            sequence = self.sequences[self.seq_index]
        except IndexError:
            self.seq_index = 0
            sequence = self.sequences[self.seq_index]
        self.seq_index += 1
        return self.random_change(sequence)

    def get_sequences(self) -> List[str]:
        """
        Read the FASTA file and return all the sequences in it as a list.
        @return: sequences, list of str of sequences in FASTA file
        """
        sequences = []
        with open(self.path_to_file) as fasta_file:
            sequence = ""
            for line in fasta_file:
                # Sequence reset
                if line.startswith(">"):
                    sequences.append(sequence)
                    sequence = ""
                # Sequence line
                else:
                    sequence += line.strip()
        return sequences[1:]

    def random_change(self, sequence: str, max_num_of_changes: int = 10) -> str:
        """
        Randomly change the sequence, if random number between 0 and 1 is less than self.random_change_probability.
        Choose a random number of functions (with replacement) to modify the sequence and return it.

        @param sequence: str, sequence to be modified
        @param max_num_of_changes: int, maximum number of functions to be chosen to modify the sequence
        @return: sequence, str, modified/not modified sequence
        """
        # Possible changing function
        functions: List[Callable] = [
            self.deletion,
            self.insertion,
            self.substitution,
            self.inversion
        ]
        # Decision to change or not - if random number less than self.random_change_probability, then change
        if random.random() < self.random_change_probability:
            # Sequence of functions to apply to sequence
            func_seq = random.choices(functions, k=random.randint(1, max_num_of_changes))
            for func in func_seq:
                sequence = func(sequence=sequence)
            return sequence
        else:
            return sequence

    def deletion(self, sequence: str) -> str:
        """
        Delete a random segment from a sequence.

        @param sequence: str, sequence of letters
        @return: sequence, str, modified string
        """
        # Length of the sequence
        seq_len = len(sequence)

        # Position of deletion start
        del_start = random.randint(0, seq_len - 1)

        # Position of deletion end
        del_end = random.randint(del_start, seq_len - 1)

        # Results of deletion - sequence with deletion
        del_seq = sequence[:del_start] + sequence[del_end:]

        return del_seq

    def insertion(self, sequence: str, max_length: int = 1000) -> str:
        """
        Insert a random amino acid sequence of random length into the provided amino acid sequence.
        Maximal possible length of insertion can be changed by max_length variable.

        @param sequence: str, sequence of letters
        @param max_length: int, maximal possible length of insertion
        @return: sequence, str, modified string
        """
        # Length of the sequence
        seq_len = len(sequence)

        # Position of insertion start
        ins_start = random.randint(0, seq_len - 1)

        # Length of insertion
        ins_len = random.randint(0, max_length)

        # Choose random sequence to insert
        rand_seq = "".join(random.choices(self.AA_list, k=ins_len))

        # Results of insertion - sequence with the insertion
        ins_seq = sequence[:ins_start] + rand_seq + sequence[ins_start + 1:]

        return ins_seq

    def substitution(self, sequence: str, max_length: int = 10) -> str:
        """
        Substitute a random amino acid sequence of random length in the provided amino acid sequence.
        Maximal possible length of substitution can be changed by max_length variable.

        @param sequence: str, sequence of letters
        @param max_length: int, maximal possible length of substitution
        @return: sequence, str, modified string
        """
        # Length of the sequence
        seq_len = len(sequence)

        # Position of substitution start
        sub_start = random.randint(0, seq_len - 1)

        # Length of insertion
        sub_len = random.randint(0, max_length)

        # Choose random sequence to insert
        rand_seq = "".join(random.choices(self.AA_list, k=sub_len))

        # Results of insertion - sequence with the insertion
        sub_seq = sequence[:sub_start] + rand_seq + sequence[sub_start + sub_len:]

        return sub_seq

    def inversion(self, sequence: str, max_length: int = 100) -> str:
        """
        Inverts a random amino acid sequence of random length of the provided amino acid sequence.
        Maximal possible length of inversion can be changed by max_length variable.

        @param sequence: str, sequence of letters
        @param max_length: int, maximal possible length of substitution
        @return: sequence, str, modified string
        """

        # Length of the sequence
        seq_len = len(sequence)

        # Position of inversion start
        inv_start = random.randint(0, seq_len - 1)

        # Length of inversion
        inv_len = random.randint(0, max_length)

        # Results of insertion - sequence with the insertion
        inv_seq = sequence[:inv_start] + sequence[inv_start:inv_start + inv_len][::-1] + sequence[inv_start + inv_len:]

        return inv_seq


# Exercise 3
def iter_append(iterable: Iterable, item: Any):
    """
    Generator - append an item to an iterable.

    @param iterable: iterable
    @param item: anything
    @return: makes a generator
    """
    yield from iterable
    yield item


# Exercise 4
def nested_list_unpacker(iterable: Iterable) -> List:
    """
    Completely flatten a nested list (or tuple).
    If just a string is passed - returns list of letters.

    @param iterable: iterable
    @return: list, a flattened list
    """

    def flattener(iterable: Iterable[Any]):
        """
        Generator - yields objects from a flattened iterable.

        @param iterable: iterable
        @return: objects from the list
        """
        for obj in iterable:

            # Check if iterable and not string (otherwise - str breaks into letters)
            if isinstance(obj, Iterable) and not isinstance(obj, (str, bytes)):
                yield from nested_list_unpacker(obj)
            else:
                yield obj

    return list(flattener(iterable))


if __name__ == "__main__":
    # Exercise 1
    print("#"*50 + "\nExercise 1\n" + "#"*50)
    reader = fasta_reader("sequences.fasta")
    print(type(reader))
    for id_, seq in reader:
        print(id_, seq[:50])

    # Exercise 2
    print("#"*50 + "\nExercise 2\n" + "#"*50)
    ins = FaultyAASeqReader("sequences.fasta")

    print(next(ins))
    print(next(ins))
    print(next(ins))
    print(next(ins))

    # Exercise 3
    print("#"*50 + "\nExercise 3\n" + "#"*50)
    generator = iter_append([1, 2, 3, 4], "ABCD")
    print(type(generator))

    for i in generator:
        print(i)

    filt = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
    generator = iter_append(filt, [5, 6, 7, 8])
    print(type(generator))

    for i in generator:
        print(i)

    # Exercise 4
    print("#"*50 + "\nExercise 4\n" + "#"*50)
    generator = nested_list_unpacker([1, 2, 3, [1, 2, [3, 4, []], [1], [], 12, 3], [1, [5, 6]], "abc"])
    print(type(generator))
    print(generator)
    for i in generator:
        print(i)

    generator = nested_list_unpacker("abc")
    print(type(generator))
    print(generator)
    for i in generator:
        print(i)
