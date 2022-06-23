# HW14 - Iterators and Generators

This is homework about iterators and generators. Following exercises have been given and their description is provided below. No external libraries were allowed. All of the solutions are provided in the [`iter_gen.py`](https://github.com/AnnaToi01/BI_2021_Python/blob/hw14/hw14/iter_gen.py).

## Table of Contents
1. [Task Descriptions](#exercises)
    1. [Task 1](#ex1)
    2. [Task 2](#ex2)
    3. [Task 3](#ex3)
    4. [Task 4](#ex4)
2. [Installation and Usage](#instus)
3. [Software Requirements](#Software)

<a name="exercises"></a>
## Exercise Descriptions

<a name="ex1"></a>
### Task 1 - function `fasta_reader`
Create a generator that takes the path to the FASTA file (here, as an example provided as [`sequences.fasta`](https://github.com/AnnaToi01/BI_2021_Python/blob/hw14/hw14/sequences.fasta)) and yields tuple od id and sequence. 

<a name="ex2"></a>
### Task 2 - class `FaultyAASeqReader`
A class that iterates over sequences in a FASTA file and randomly changes them.

Attributes and methods:
  * `path_to_file` - attribute, path to the FASTA file
  * `random_change_probability` - attribute, probability of how often random FASTA sequence is changed
  * `__init__` - class constructor
  * `__iter__` - returns an iterator
  * `__next__` - returns the next item, here sequence, from the iterator (indefinitely)
  * `get_sequences` - reads the FASTA file (path to file stored in `path_to_file` attribute) and returns all the sequences in it as a list
  * `random_change` - randomly changes the sequence or leaves it as it is (see `random_change_probability`), possible modifications are deletions, insertions, substitutions, inversions
  * `deletion` - delete a random segment from a sequence
  * `insertion` - inserts a random amino acid sequence of random length into the provided amino acid sequence
  * `substitution` - substitutes a random amino acid sequence of random length in the provided amino acid sequence
  * `inversion` - inverts a random amino acid sequence of random length of the provided amino acid sequence

<a name="ex3"></a>
### Task 3 - function `iter_append`
Create a generator that appends an item to an iterable.

<a name="ex4"></a>
### Task 4 - function `nested_list_unpacker`
Create a function that completely flattens a nested list/tuple.


<a name="instus"></a>
## Installation and Usage
1. You can download the current directory with all the script by typing in https://github.com/AnnaToi01/BI_2021_Python/tree/hw14/hw14 into the search field https://download-directory.github.io/. Move the zip file to your working directory.
2. Unpack the directory:
```
$ unzip AnnaToi01\ BI_2021_Python\ hw14\ hw14.zip 
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
         $ virtualenv venv --python=3.8
         ```
       * Activate it
         ```
         $ source ./venv/bin/activate
         ```
    * Via `conda`
        * [Install Anaconda](https://docs.anaconda.com/anaconda/install/index.html)
        * Create virtual environment
           ```
           $ conda create --name <env_name> python=3.8
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
   ```
   $ python ./<file_name>.py
   ```

<a name="Software"></a>
## Software Requirements

* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/python.svg height=20> Python 3.8
