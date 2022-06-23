# HW16 - Parallel programming

This is homework about parallel programming. Following exercises have been given and their description is provided below. All of the solutions are provided in the [`nuc_counter.py`](https://github.com/AnnaToi01/BI_2021_Python/blob/hw16/hw16/nuc_counter.py), [`run_time_proc.py`](https://github.com/AnnaToi01/BI_2021_Python/blob/hw16/hw16/runtime_proc.py) and summarized in Jupyter Notebook [`parallel_programming.ipynb`](https://github.com/AnnaToi01/BI_2021_Python/blob/hw16/hw16/parallel_programming.ipynb).
## Table of Contents
1. [Task Descriptions](#exercises)
    1. [Task 1](#ex1)
    2. [Additional Task 1](#ex2)
2. [Installation and Usage](#instus)
3. [Software Requirements](#Software)

<a name="exercises"></a>
## Exercise Descriptions

<a name="ex1"></a>
### Task 1 - file `nuc_counter.py`
Write a command line program (using argparse) that will accept a large FASTA file (500MB+) (e.g. with the [human genome](https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_genomic.fna.gz)), as well as the number of threads in which this program will be executed. The program should count the characters for each sequence in the fast file and output this information. Consider any characters: masked and regular nucleotides and non-standard nucleotide designations, etc.

Run times (another batch of run times are also in the Jupyter Notebook):
![runtimes](https://user-images.githubusercontent.com/58418063/164983639-e6790d9f-7c7a-4f5a-b797-82b85f34c251.png)

<a name="ex2"></a>
### Additional Task 1 - file `run_time_proc.py`
Reproduce a graph of function runtime dependency on the number of processes.

<a name="instus"></a>
## Installation and Usage
1. You can download the current directory with all the script by typing in https://github.com/AnnaToi01/BI_2021_Python/tree/hw16/hw16 into the search field https://download-directory.github.io/. Move the zip file to your working directory.
2. Unpack the directory:
```
$ unzip AnnaToi01\BI_2021_Python\hw16\hw16.zip 
```
All the files will be in the current directory.

3. Create virtual environment
    * Via `virtualenv`

       * Install virtualenv if it is not installed.
         ```
         $ pip install virtualenv
         ```
       * Create virtual environment
         ```
         $ virtualenv venv --python=3.10
         ```
       * Activate it
         ```
         $ source ./venv/bin/activate
         ```
    * Via `conda`
        * [Install Anaconda](https://docs.anaconda.com/anaconda/install/index.html)
        * Create virtual environment
           ```
           $ conda create --name <env_name> python=3.10
           ```
        * Activate it
           ```
           $ conda activate <env_name>
           ```
4. Install necessary libraries
 ```
$ pip install -r requirements.txt
 ```
 5. Making the files executable
   * Via `chmod +x`
   ```
   $ chmod +x *.py
   ```
   Then you can run the files from the working directory as follows:
   * for `nuc_counter.py`:
   ```
   $ time python nuc_counter.py --fasta FASTA-FILE --threads NUM-THREADS
   ```
   * for `run_time_proc`:
   ```
   $ python ./<file_name>.py
   ```

<a name="Software"></a>
## Software Requirements

* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/python.svg height=20> Python 3.10
