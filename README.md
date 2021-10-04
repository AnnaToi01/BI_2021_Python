This is repository for a python course in the bioinformatics institute (2021). hw1.py corresponds to the program, that modifies the given nucleotide sequences.

"Enter command" prompts the user to enter a command, consisting of three possible functions: reverse, complement, transcribe as well as their combinations and an exit function to exit the loop (cases do not matter). There are infinite possibilities of the functions, separated by space or comma followed by space. Possible combinations would be:
"transcribe, reverse, reverse, complement, transcribe" and so on.
When invalid commands are entered, a prompt with "Enter a command to substitute the invalid command" shows up. The invalid command has to be substituted with one or infinite amound of functions. In case when multiple commands are given, the correct commands are kept. For example: if the command "INVALID1 reverse INVALID2", two prompts would show up, asking to substitute both of the invalid statements. INVALID1 could be substituted by e.g. "reverse complement", and INVALID2 just by "transcribe".

DNA and RNA Sequences can be given when prompted by "Enter sequence: ". When complementing and it is not evident, whether the given sequence is RNA or DNA sequence (e.g. ACAC), it is assumed to be DNA sequence. Furthermore, as RNA sequences cannot be transcribed, they are not changed if transcribed.
