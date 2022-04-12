# HW15 - Decorators

This is homework about decorators. Following exercises have been given and their description is provided below. All of the solutions are provided in the [`decorators.py`](https://github.com/AnnaToi01/BI_2021_Python/blob/hw15/hw15/decorators.py).

## Table of Contents
1. [Task Descriptions](#exercises)
    1. [Task 1](#ex1)
    2. [Task 2](#ex2)
    3. [Task 3](#ex3)
    4. [Additional Task 1](#ex4)
    5. [Additional Task 2](#ex5)
2. [Installation and Usage](#instus)
3. [Software Requirements](#Software)

<a name="exercises"></a>
## Exercise Descriptions

<a name="ex1"></a>
### Task 1 - function `measure_time`
Create a decorator that measures runtime of a function.

<a name="ex2"></a>
### Task 2 - function `function_logging`
Print the positional and keyword arguments of the decorated function.

<a name="ex3"></a>
### Task 3 - function `russian_roulette_decorator`
Russian roulette function - makes the decorated function return the input value (return_value) with given probability.

<a name="ex4"></a>
### Additional Task 1 - function `staticmethod_alt`
Returns a static method for a function passed as the parameter. Alternative to staticmethod.

<a name="ex5"></a>
### Additional Task 2 - function `dataclass_alt`
Adds generated special methods to the class. Alternative to dataclass.

<a name="instus"></a>
## Installation and Usage
1. You can download the current directory with all the script by typing in https://github.com/AnnaToi01/BI_2021_Python/tree/hw15/hw15 into the search field https://download-directory.github.io/. Move the zip file to your working directory.
2. Unpack the directory:
```
$ unzip AnnaToi01\ BI_2021_Python\ hw15\ hw15.zip 
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

* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/python.svg height=20> Python 3.10
