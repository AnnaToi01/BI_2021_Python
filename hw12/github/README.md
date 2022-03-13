# HW12 - API

This is homework about working with API, using libraries `request` and `beautifulsoup4`. Here the task of the program was to access the GitHub and get some user information using the username.

## Table of Contents
1. [File Descriptions](#files)  
    1. [github.py](#tblastn)
    2. [requirements.txt](#requirements)
3. [Installation and Usage](#instus)
4. [Software Requirements](#Software)

<a name="files"></a>
## File Descriptions

<a name="tblastn"></a>
### [tblastn.py](https://github.com/AnnaToi01/BI_2021_Python/blob/hw12/hw12/tblastn/tblastn.py)

The main python API file interacting with tblastn that is supposed to be used from the command line. It includes:
* Class Github which contains following functions:
  * function get_user_info
    * Returns a dictionary containing user information (name of the users, followers, information like organization, number of public repositories)
  * function get_user_repositories
    * Returns a list of repositories in the form of a list of dictionaries, each dictionary has keys describing username, name of repository, description, language
  * function list_repository_contents
    * Returns a list of files and directories in the repository of the user with path repository_path
  * function download_file
    * Downloads a file which has remote path in a repository and saves it locally (local_file_path)

<a name="requirements"></a>
### [requirements.txt](https://github.com/AnnaToi01/BI_2021_Python/blob/hw12/hw12/tblastn/requirements.txt)

Requirements for the program to run.

<a name="instus"></a>
## Installation and Usage
1. You can download the current directory with all the script by typing in https://github.com/AnnaToi01/BI_2021_Python/tree/hw12/hw12/github into the search field https://download-directory.github.io/. Move the zip file to your working directory.
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

The username as well as other parameters can be changed inside of the file.

<a name="Software"></a>
## Software Requirements

* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/python.svg height=20> Python 3.8
