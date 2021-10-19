import os


def gc_mean(reads, dic_ind, up = 100, low = 0):
    for i, read in enumerate(reads):
        mean = (read[1].count("G") + read[1].count("C"))/len(read[1])
        if mean > up or mean < low:
            dic_ind[i] += 1


def gc_filter(reads, dic_ind, gc_bounds = (0, 100)):
    if isinstance(gc_bounds, float) or isinstance(gc_bounds, int):
        up = gc_bounds
        gc_mean(reads, dic_ind, up/100)
    else:
        low, up = gc_bounds
        gc_mean(reads, dic_ind, up/100, low/100)


def length_filter(reads, dic_ind, length_bounds = (0, 2**32)):
    if isinstance(length_bounds, int):
        up = length_bounds
        for i, read in enumerate(reads):
            if len(read[1]) > up:
                dic_ind[i] += 1
    else:
        low, up = length_bounds
        for i, read in enumerate(reads):
            if len(read[1]) > up or len(read[1]) < low:
                dic_ind[i] += 1



def quality_threshold(reads, dic_ind, qs_threshold = 0):
    """
    reads
    dic_ind
    qs_threshold- > quality score mean for a read
    """
    for i, read in enumerate(reads):
        qs_sum = 0
        for character in read[3]:
            qs_sum += ord(character) - 33
        qs_mean = qs_sum/len(read[3])
        if qs_mean < qs_threshold:
            dic_ind[i] += 1


def main(input_fastq, output_file_prefix, gc_bounds = (0, 100), length_bounds = (0, 2**32), qs_threshold = 0, save_filtered = False):
    passed_reads = output_file_prefix + "_passed.fastq"
    failed_reads = output_file_prefix + "_failed.fastq"
    with open(input_fastq, 'r') as file, open(passed_reads, "w") as passed, open(failed_reads, "w") as failed:
        fastq = file.read().splitlines()
        reads = []
        for index in range(0, len(fastq), 4):
            reads.append(fastq[index:index + 4])
        dic_ind = {i: 0 for i in range(len(reads))}
        gc_filter(reads, dic_ind, gc_bounds)
        length_filter(reads, dic_ind, length_bounds)
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

path = "./test.fastq"
print(main(path, "new_file", length_bounds=150, qs_threshold=35))
