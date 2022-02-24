# HW10 - Pandas

This is homework about library `pandas`. Following exercises have been given and their description is provided below. Each exercise has its corresponding .py file. Also Jupyter Notebok with all of the exercises is provided.

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
### Task 1

Build histogramms for the distribution of the nucleotides for each position from the [source](https://github.com/Serfentum/bf_course/blob/master/14.pandas/train.csv). 
 
<a name="ex2"></a>
### Task 2 

For the dataframe from the previous task:
* choose rows where the `matches` column is higher than average
* choose columns pos, reads_all, mismatches, deletions, insertions
* save it as `train_part.csv`


<a name="ex3"></a>
### Task 3

Do some small EDA. I chose this [data](https://www.kaggle.com/rohitsahoo/sales-forecasting).

<a name="ex4"></a>
### Task 4 

Write `bedtools intersect` for two files `rrna_annotation.gff` and `alignmend.bed`.

<a name="instus"></a>
## Installation and Usage
1. You can download the current directory with all the script by typing in https://github.com/AnnaToi01/BI_2021_Python/tree/hw11/hw11 into the search field https://download-directory.github.io/. Move the zip file to your working directory.
2. Unpack the directory:
```
$ unzip AnnaToi01\ BI_2021_Python\ hw11\ hw11.zip 
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
