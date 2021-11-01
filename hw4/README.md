OS: Ubuntu 21.04
Python: 3.9.7

Get the code from the GitHub repository https://github.com/krglkvrmn/Virtual_environment_research by clicking on "Code" and option "Download ZIP". Place it in the working directory and unzip it by running:

unzip Virtual_environment_research-master.zip

Alternatively, the unzipped version is already present in the current directory under the folder name Virtual_environment_research-master. Download the requirements.txt on your computer.

Anaconda has been used to manage virtual environments. If you do not have it installed, please see the instructions https://docs.anaconda.com/anaconda/install/linux/. 

1. Create the virtual environment with the help of conda. Please keep in mind that any python version older than 3.9 will not work with the code.
conda create --name yourenv python=3.9.7

2. Activate the virtual environment.

conda activate yourenv

(yourenv) should pop up in the beginning of the line. Alternatively, you can check that you are in the virtual environment by 

which python

This should point to the directory of the environment.

3. Download all the required packages.

pip install -r requirements.txt

4. Now you can run the code:

python Virtual_environment_research-master/pain.py

5. You can leave the environment by:

conda deactivate

6. Delete the environment:

conda env remove -n yourenv

