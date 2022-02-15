# HW10 - Classes

This is homework about classes. Following exercises have been given and their description is provided below. Each exercise has its corresponding .py file. Also Jupyter Notebok with all of the exercises is provided.

## Table of Contents
1. [Exercise Descriptions](#exercises)
    1. [Exercise 1](#ex1)
    2. [Exercise 2](#ex2)
    3. [Exercise 3](#ex3)
    4. [Exercise 4](#ex4)
2. [Installation and Usage](#instus)
3. [Software Requirements](#Software)

<a name="exercises"></a>
## Exercise Descriptions

<a name="ex1"></a>
### Exercise 1 - `classes Card and CardDeck`

Create a class that describes something.

I programmed a deck of cards and some simple operations connected with it. First, I prepared a `Card` which describes single cards. hen I wrote a class for a deck of cards (`CardDeck`), which can hold a list of `Card` instances. The class `Card` only contain the cards' suit and rank, the `CardDeck` class contains:
* a list to store the cards in the deck
* a list to store the cards that were drawn from the deck, in the order they were drawn
* a method `create_deck` to create a regular 52 card deck, that is called when the CardDeck is initialized
* a method `shuffle` to shuffle the list of cards of the deck
* a method `get_number_of_cards_remaining` to retrieve the number of cards remaining in the deck
* a method `get_value_of_cards_remaining` to retrieve the total value of all cards remaining in the deck
* a method `get_cards_drawn` to retrieve the drawn cards
* a method `draw` to draw the topmost card from the deck (this function has to remove the drawn card from the deck)
* a method `peek` to peek the next three cards that will be drawn from the deck 
 
<a name="ex2"></a>
### Exercise 2 - `class RNA`

Write a class that describes RNA sequences. We need:

* Constructor that takes the RNA sequene and creates an object with it
* Method `translation` - translates the RNA sequence according to the standard genetic code table
* Method `back transcription` - reverse transcribes the RNA sequence

<a name="ex3"></a>
### Exercise 3 - `class PositiveSet`

Write a class that is inhereted from set and which will only contain positive numbers (>0) when created and won't allow adding any negative numbers.

<a name="ex4"></a>
### Exercise 4 - `class FASTAStats`

Create a class for statistic analysis of FASTA files.

Input parameters:

* Path to the FASTA file

Methods:
* `__init__` - initiate the class with all the attributes
* `__str__` - redefine method for information generation when printing
* `check_type` - checks the molecule type (DNA, RNA, protein)
* `count_seq` - number of sequences in FASTA file
* `hist_len_distribution` - build a histogram for length distribution of the sequences
* `min_max_seq_len` - returns minimal and maximal sequence length
* `gc_calc` - GC content
* `n_calc` - N content
* `count_kmers` - histogram of 4-mers (x-axis - all possible 4-mers, y-axis - their frequency
* `statistics` - run the whole statistical analysis

Addition:
* `check_if_None` - decorator, checks if some attributes are already calculated to save the computational resources

<a name="instus"></a>
## Installation and Usage
1. You can download the current directory with all the script by typing in https://github.com/AnnaToi01/BI_2021_Python/tree/hw10/hw10 into the search field https://download-directory.github.io/. Move the zip file to your working directory.
2. Unpack the directory:
```
$ unzip AnnaToi01\ BI_2021_Python\ hw10\ hw10.zip 
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
* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/ubuntu.svg height = 20> Ubuntu 21.04
* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/gnubash.svg height=20> Bash
