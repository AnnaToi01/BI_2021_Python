state = True
legal = {'A', 'G', 'C', 'T', 'U'}


class ExitError(Exception):
    pass


def flatten(lis, out=[]):
    for ele in lis:
        if isinstance(ele, list):
            flatten(ele, out)
        else:
            out.append(ele)

    return out


def reverse(s):
    """Reverses the nucleotide sequence"""
    return s[::-1]


def transcribe(s):
    """Transcribes the DNA sequence"""
    return s.replace('T', 'U').replace('t', 'u')


def complement(s):
    """Complements the nucleotide sequences"""
    if "T" in s.upper():
        return s.translate(str.maketrans("ATGCatgc", "TACGtacg"))  # alternatively, ''.join([DNA_comp[i] for i in s])
    else:
        return s.translate(str.maketrans("AUGCaugc", "UACGuacg"))  # alternatively, ''.join([RNA_comp[i] for i in s])


dic_command = {'transcribe': transcribe,
               'complement': complement,
               'reverse': reverse}


def valid_command(command):
    """Validates the command, takes it as a string and gives out a list of all commands"""
    com = command.replace(",", "").split(" ")
    n = 0
    if com[0] == 'exit':
        raise ExitError
    for i, c in enumerate(com):
        if c.lower() not in dic_command.keys():
            if n == 0:  # only printed once after the first input of the invalid command in each recursive cycle
                print(
                    f"Invalid command '{c}'. Available commands: \n"
                    f"transcribe\n"
                    f"complement\n"
                    f"reverse\n"
                    f"And their combinations, as well as exit for exiting the function. "
                    f"See README.md for further information.\nTry again!")
            n += 1
            com[i] = input(f"Enter a command to substitute the invalid command '{c}' from previous entry: ")
            com[i] = valid_command(com[i])  # the input is checked every time recursively
    return com


def valid_seq(sequence):
    """Validates the nucleotide sequence"""
    if "T" in sequence.upper() and "U" in sequence.upper():
        print('Invalid alphabet. Try again')
        sequence = input("Enter sequence: ")
        return valid_seq(sequence)
    elif all((c in legal) for c in sequence.upper()):
        return sequence
    else:
        print("Invalid alphabet. Try again!")
        sequence = input("Enter sequence: ")
        return valid_seq(sequence)


try:
    while state:
        commands = input("Enter command: ")
        whole_commands = valid_command(commands)
        whole_commands = flatten(whole_commands, [])
        nuc_seq = input("Enter sequence: ")

        nuc_seq = valid_seq(nuc_seq)

        for i, command in enumerate(reversed(whole_commands)):
            # reversed sequence of the commands based on the example of reverse complement
            nuc_seq = dic_command[command.lower()](nuc_seq)
        print(nuc_seq)


except ExitError:
    print("Good luck!")
