# UNIX utilities simulator

These Python 3.8 scripts simulate the well-known UNIX command utilities using only built-in libraries, not including subprocess. 

## Table of Contents
1. [List of Utilities](#utilities)
2. [Installation and Usage](#instaus)
    * Pipeline structure
    * Preliminary settings
    * Console interface
    * Running utility
3. [Software Requirements](#Software)

<a name="utilities"></a>
## List of utilities
In alphabetical order. For each utility additionaly `-h`, `--help` option can be used to take a look at the help page:

1. `cat.py`
    * Concatenate files and print on the standard output
    * *OPTIONS*:
        * Can take multiple files as STDIN
2. `cp.py`
    * Copy files and directories
    * *OPTIONS in this order*:
        * `-r`, `--recursive` - copy directories and their contents recursively
        * Can take multiple files/directories as STDIN (can copy directories only with `-r`)
3. `grep.py`
    * grep searches for a pattern in each file. Typically grep prints each line that matches a pattern. Typically, patterns should be quoted with single quotes when grep is used.
    * *OPTIONS in this order*:
        * pythonic regex pattern
        * `-v`, `--invert_match` - invert the sense of matching, to select non-matching lines
        * `-i`, `--ignore_case` - ignore  case  distinctions  in  patterns and input data, so that characters that differ only in case match each other
        * `-c`, `--count` - print a count of matching lines for each input file
        * Can take multiple files as STDIN, match for each file is shown by `<file_name>: match`
4. `head.py`
    * Output the first part of files
    * *OPTIONS in this order*:
        * `-n`, `--lines` - print the first NUM lines instead of  the  first  10;  with  the leading '-', print all but the last NUM lines of each file
        * Can take multiple files as STDIN, first n lines for each are separated by `==> path_to_file.name <==`
5. `install.py`
    * Appends all the scripts in the given directory to the PATH"
    * *OPTIONS in this order*:
        * `-P`, `--PATH_directory` - PATH directory to place the scripts, default is the first directory listed in the PATH
        * path to directory with the scripts
6. `ln.py`
    * Make links between files
    * *OPTIONS in this order*:
        * `-s`, `--symbolic` - make symbolic links instead of hard links
        * path to input file
        * path to output file (link name)
7. `ls.py`
    * List directory contents
    * *OPTIONS in this order*:
        * `-a`, `--all` - do not ignore entries starting with .
        * path to directory, if none given - lists the contents of current directory
8. `mkdir.py`
    * make directories
    * *OPTIONS in this order*:
        * `-p`, `--parents` - no error if existing, make parent directories as needed
        * `-v`, `--verbose` - print a message for each created directory
        * path to directory
9. `mv.py`
    * move (rename) files (recursively)
    * *OPTIONS in this order*:
        * path to input file
        * path to output file
10. `rm.py`
    * remove a file or directory (can remove empty directories without `-r`)
    * *OPTIONS in this order*:
        * `-r`, `--recursive` - remove directories and their contents recursively
        * path to file/directory
11. `sort.py`
    * sort lines of text files in alphanumeric order
    * *OPTIONS in this order*:
        * Can take multiple files as STDIN
12. `tail.py`
    * Output the last part of files
    * *OPTIONS in this order*:
        * `-n`, `--lines` - output the last NUM lines, instead of the last  10; or  use  -n +NUM to output starting with line NUM'
        * Can take multiple files as STDIN, last n lines for each are separated by `==> path_to_file.name <==`
13. `touch.py`
    * change file timestamps/create files
    * *OPTIONS in this order*:
        * Can take multiple files as STDIN
14. `uniq.py`
    * report or omit repeated lines
    * *OPTIONS in this order*:
        * Can take multiple files as STDIN in comparison to UNIX utility, it concatenates them and prints unique lines of n files
15. `wc.py`
    * report or omit repeated lines
    * *OPTIONS in this order*:
        * '-l', '--lines' - print the newline counts
        * '-w', '--words' - print the word counts
        * '-c', '--bytes' - print the byte counts
        * path to file

<a name="instaus"></a>
## Installation and Usage

### Pipeline structure
Pipeline is separated into several files located in `scripts` folder:

* `caclulations.py` contains functions required for calculations

* `plotting.py` contains functions for plotting graphs

* `main.py` contains main piece pf code for running all computations




### Preliminary settings
Clone repository
```
$ git clone git@github.com:ipsemenov/FastQC_simulator.git
```
Move to project directory 
```
$ cd FastQC
```
Set up virtual environment in working directory:
1. Create virtual environment
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
2. Install necessary libraries
 ```
$ pip install -r requirements.txt
 ```
3. Install package wkhtmltopdf
```
$ sudo apt-get install wkhtmltopdf
```

### Console interface
This instrument is a console utility maintaining following parameters:
```
  -i ,  --input     path to fastq file`
  -o , --output     path to output folder for storing results
  -a , --adapters   path to file with adapters. Default: ./adapters.txt
```


### Running utility
Example workflow:
```
$ python main.py -i <path_to_fastq> -o <path_to_ouptut_dir>  -a <path_to_adapters> 
```
To show brief information about parameters, execute following command:
```	
$ python main.py -h
```


<a name="Software"></a>
## Software Requirements
<img src=https://img.shields.io/badge/FastQC%20Simulator-FASTQ%20Quality%20Check-informational height = 20>

* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/python.svg height=20> Python 3.8
* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/ubuntu.svg height = 20> Ubuntu 20.04 and 21.04
* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/git.svg height = 20> Git 2.30.2
* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/markdown.svg height=20> Markdown
* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/html5.svg height=20> HTML
* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/github.svg height=20> GitHub
* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/gnubash.svg height=20> Bash
* Rest of the requirements are in requirements.txt.

