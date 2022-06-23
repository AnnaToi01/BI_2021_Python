# HW13 - SQL

This is homework about library `sqlite3`. Following exercises have been given and their description is provided below. Each exercise has its corresponding .py file. Also Jupyter Notebok with all of the exercises is provided.

## Table of Contents
1. [Task Descriptions](#exercises)
    1. [Task 1](#ex1)
    2. [Task 2](#ex2)
2. [Installation and Usage](#instus)
3. [Software Requirements](#Software)

<a name="exercises"></a>
## Exercise Descriptions

<a name="ex1"></a>
### Task 1
Here I work/train with [data available on google drive](https://drive.google.com/file/d/1NWIT8Yn-GdgpBUfFO87dnIDQgmE5nj-j/view?usp=sharing). 
Please download the file and place it into the working directory. Then proceed to first unzip the file:
```
$ unzip genotyping_data.zip
```
Making the directory for two created `.csv` files and placing them there:
```
$ mkdir genotyping_data
$ mv *.csv ./genotyping_data
```
Here functions were created in order to convert the `csv` files to SQL database files. Also, some SQL queries were executed. Please see the files [training.ipynb](https://github.com/AnnaToi01/BI_2021_Python/blob/hw13/hw13/training.ipynb) and [training.py](https://github.com/AnnaToi01/BI_2021_Python/blob/hw13/hw13/training.py) for further details.
<a name="ex2"></a>
### Task 2 

Here I tried to work with the [worldometer coronavirus](https://www.worldometers.info/coronavirus/) webpage table with the statistics for each country. I tried to convert the table into an SQL database and write some functions to modify the database, e.g. to insert a new country or remove an existing one.
Please see [worldometer_coronavirus.ipynb](https://github.com/AnnaToi01/BI_2021_Python/blob/hw13/hw13/worldometer_coronavirus.ipynb)
and [worldometer_coronavirus.py](https://github.com/AnnaToi01/BI_2021_Python/blob/hw13/hw13/worldometer_coronavirus.py)

<a name="instus"></a>
## Installation and Usage
1. You can download the current directory with all the script by typing in https://github.com/AnnaToi01/BI_2021_Python/tree/hw13/hw13 into the search field https://download-directory.github.io/. Move the zip file to your working directory.
2. Unpack the directory:
```
$ unzip AnnaToi01\ BI_2021_Python\ hw13\ hw13.zip 
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
