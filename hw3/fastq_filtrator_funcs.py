import os


def gc_mean(reads, dic_ind, up=100, low=0):
    """
    Calculates the mean GC-contents of reads
    """
    for i, read in enumerate(reads):
        mean = (read[1].count("G") + read[1].count("C")) / len(read[1])
        if mean > up/100 or mean < low/100:
            dic_ind[i] += 1


def gc_filter(reads, dic_ind, gc_bounds=(0, 100)):
    """"
    Filters reads according based on their mean GC-content
    gc_bounds - tuple of lowest and highest threshold, or just one-element tuple of highest threshold
    """
    if len(gc_bounds) == 1:
        up = gc_bounds[0]
        gc_mean(reads, dic_ind, up)
    else:
        low, up = gc_bounds
        gc_mean(reads, dic_ind, up, low)


def length_filter(reads, dic_ind, length_bounds=(0, 2 ** 32)):
    """"
    Filters reads based on their length
    length_bounds - tuple of lowest and highest threshold, or just one-element tuple of highest threshold
    """
    if len(length_bounds) == 1:
        up = length_bounds[0]
        for i, read in enumerate(reads):
            if len(read[1]) > up:
                dic_ind[i] += 1
    else:
        low, up = length_bounds
        for i, read in enumerate(reads):
            if len(read[1]) > up or len(read[1]) < low:
                dic_ind[i] += 1


def quality_threshold(reads, dic_ind, qs_threshold=0):
    """
    Filters reads according to their quality score (phred33)
    qs_threshold - lowest mean quality score for the read
    """
    for i, read in enumerate(reads):
        qs_sum = 0
        for character in read[3]:
            qs_sum += ord(character) - 33
        qs_mean = qs_sum / len(read[3])
        if qs_mean < qs_threshold:
            dic_ind[i] += 1


def main(input_fastq, output_file_prefix, gc_bounds=(0, 100), length_bounds=(0, 2 ** 32), qs_threshold=0,
         save_filtered=False):
    passed_reads = output_file_prefix + "_passed.fastq"
    failed_reads = output_file_prefix + "_failed.fastq"
    with open(input_fastq, 'r') as file, open(passed_reads, "w") as passed, open(failed_reads, "w") as failed:
        fastq = file.read().splitlines()
        reads = []
        for index in range(0, len(fastq), 4):
            reads.append(fastq[index:index + 4])
        dic_ind = {i: 0 for i in range(len(reads))}
        if gc_bounds != (0, 100):
            gc_filter(reads, dic_ind, gc_bounds)
        if length_bounds != (0, 2 ** 32):
            length_filter(reads, dic_ind, length_bounds)
        if qs_threshold != 0:
            quality_threshold(reads, dic_ind, qs_threshold)
        for key, value in dic_ind.items():
            if value > 0:
                if save_filtered:
                    failed.write("\n".join(reads[key]))
                    failed.write("\n")
            else:
                passed.write("\n".join(reads[key]))
                passed.write("\n")
        if not save_filtered:
            os.remove(failed_reads)


if __name__ == "__main__":
    print(
        "This program filters the reads based on their GC-content, length and mean quality score: \n"
        "GC content (in %) and length minimal and maximal thresholds should be given with space as separator,"
        "if just one threshold is given - it is taken as maximal possible value \n"
        "For the output file its prefix: the path and the name of the file should be specified - "
        "the reads that passed the filter are saved as prefix_passed.fastq and "
        "the ones that failed as prefix_failed.fastq"
    )
    input_path = input("Enter path to the input file: ")
    output_path = input("Enter the prefix of the output file: ")
    gc_bounds_in = tuple(int(i) for i in input("Enter the bounds for GC: ").split())
    length_bounds_in = tuple(int(i) for i in input("Enter the bounds for length of the read: ").split())
    qs_threshold_in = input("Enter the minimal mean quality of the read: ")
    try:
        qs_threshold_in = float(qs_threshold_in)
    except ValueError:
        pass
    save_filtered_in = bool(int(input("Should reads that failed be saved? Yes - 1, No - 0 \n")))
    # Example for input format:
    # input_path = "test.fastq"
    # output_path = "test"
    # gc_bounds_in = tuple(float(i) for i in "40 60".split())
    # length_bounds_in = tuple(float(i) for i in "20 110".split())
    # qs_threshold_in = float("30")
    # save_filtered_in = bool(int("0"))
    kwargs = dict(gc_bounds=gc_bounds_in, length_bounds=length_bounds_in,
                  qs_threshold=qs_threshold_in, save_filtered=save_filtered_in)

    main(input_path, output_path,
         **{k: v for k, v in kwargs.items() if isinstance(v, (bool, int, float)) or len(v) != 0})
