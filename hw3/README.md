This is repository for a python course in the bioinformatics institute (2021). This branch contains homework 3 - fastq files filtrator, which filters based on the GC mean content of the reads, their length and their mean quality score (phred33). There are two programs - one of them is fastq_filtrator.py - this is file that runs more efficiently. In fastq_filtrator_funcs each function is separate, so that it is possible to use/import them separately.

There are input prompts for the path of the input file, the output file, and the threshholds for GC mean content, length and quality score. Also there is prompt asking, whether the reads that failed filtering, should be saved.

Input file should be a classical fastq file, without headers.

One or two output files are generated, based on whether the failed reads should be saved. For output file its prefix, consisting of path and the name of the file, should be given. E.g. "/home/user/test", two files will be generated: test_passed.fastq and test_failed.fastq, which contained reads that passed and failed the filtering, respectively.

For GC mean content, one or two bounds (in %) can be given. When one bound is given, it is assumed that it's the maximal possible GC-content. Same goes for length. Quality score should be given as phred score integer. 
