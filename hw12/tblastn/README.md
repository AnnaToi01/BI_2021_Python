# HW12 - API

This is homework about working with API, using libraries `request` and `beautifulsoup4`. Here the task of the program was to access the [tblastn](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=tblastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome) server. Given a protein sequence and the species name/taxid the BLAST alignments should have been searched in Whole-genome contigs (wgs) database.

## Table of Contents
1. [File Descriptions](#files)  
    1. [tblastn.py](#tblastn)
    2. [tblastn_API.ipynb](#tblastn_API)
    3. [example.fa](#example)
    4. [requirements.txt](#requirements)
3. [Installation and Usage](#instus)
4. [Software Requirements](#Software)

<a name="files"></a>
## File Descriptions

<a name="tblastn"></a>
### [tblastn.py](https://github.com/AnnaToi01/BI_2021_Python/blob/hw12/hw12/tblastn/tblastn.py)

The main python API file interacting with tblastn that is supposed to be used from the command line. It includes:
* Class Taxonomy 
    * works with https://www.ncbi.nlm.nih.gov/Taxonomy/TaxIdentifier/tax_identifier.cgi from NCBI, extract the taxids from the species names
* Class Alignment
    * works with tblastn (https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=tblastn) alignment output and returns an object with all the alignment details
* Function save_content 
    *  saves the content of the requests model Response into a file with the given path
* Function check_response
    * prints the URL and the status code in case the request did not function
* Function query
    *  saves first query input HTML file, and the HTML file after job was completed
    *  returns the JobID (RID) and the accession numbers
* Function get_alignment
    * saves the alignment HTML file
    * gets all alignment details from Alignment tab of the BLAST results, generating an Alignment object
    * returns a list of Alignment objects (for each alignment match)
* Funciton fasta_alig
    * reads a FASTA file and returns a dictionary of Alignments for each FASTA sequence (uses query and get_alignment functions)

<a name="tblastn_API"></a>
### [tblastn_API.ipynb](https://github.com/AnnaToi01/BI_2021_Python/blob/hw12/hw12/tblastn/tblastn_API.ipynb)

Messy jupyter notebook just describing my thoughts about how I came to the solution.

<a name="example"></a>
### [example.fa](https://github.com/AnnaToi01/BI_2021_Python/blob/hw12/hw12/tblastn/example.fa)

Example FASTA file to try the script out on.

<a name="requirements"></a>
### [requirements.txt](https://github.com/AnnaToi01/BI_2021_Python/blob/hw12/hw12/tblastn/requirements.txt)

Requirements for the program to run.

<a name="instus"></a>
## Installation and Usage
1. You can download the current directory with all the script by typing in https://github.com/AnnaToi01/BI_2021_Python/tree/hw12/hw12/tblastn into the search field https://download-directory.github.io/. Move the zip file to your working directory.
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
   $ python ./<file_name>.py [options]
   ```
6. Running the program on [example.fa](https://github.com/AnnaToi01/BI_2021_Python/blob/hw12/hw12/tblastn/example.fa)
   ```
   $ python tblastn.py -id "Populus trichocarpa" -i example.fa
   ```

If run without only with option `-id` (without `-i`), the user will be asked "Do you want to continue with the alignment? [print yes if continue]" - if anything other than yes is answered, only the taxids will be printed out. Otherwise, one can type in the protein FASTA sequence (one line) and continue with the alignment.

<a name="Software"></a>
## Software Requirements

* <img src=https://github.com/simple-icons/simple-icons/blob/develop/icons/python.svg height=20> Python 3.8
