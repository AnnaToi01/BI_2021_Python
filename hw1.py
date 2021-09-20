state = True
DNA_comp = {"T": "A", "G": "C", "C": "G", "A": "T",
            "t": "a", "g": "c", "c": "g", "a": "t"}

RNA_comp = {"U": "A", "G": "C", "C": "G", "A": "U",
            "u": "a", "g": "c", "c": "g", "a": "u"}


def reverse(s):
    return s[::-1]


def transcribe(s):
    return s.replace('T', 'U').replace('t', 'u')


def complement(s):
    if "T" in s.upper():
        return ''.join([DNA_comp[i] for i in s])
    else:
        return ''.join([RNA_comp[i] for i in s])


def rev_complement(s):
    return reverse(complement(s))


def valid_command(command):
    global com
    com = command
    if command not in dic_command.keys():
        print(
            "Invalid command. Available commands: \ntranscribe\ncomplement\nreverse\nAnd their combinations!\nTry again!")
        com = input("Enter command: ")
        valid_command(com)
    return


def valid_seq(sequence, command):
    global seq
    seq = sequence
    legal = ['A', 'G', 'C', 'T', 'U']
    if "T" in sequence.upper() and "U" in sequence.upper():
        print('Invalid alphabet. Try again')
        seq = input("Enter sequence: ")
        valid_seq(seq, command)
    elif ("U" in sequence.upper()) and (command == 'transcribe'):
        print("RNA sequence cannot be transcribed. Try again!")
        seq = input("Enter sequence: ")
        valid_seq(seq, command)
    elif all((c in legal) for c in sequence.upper()):
        return
    else:
        print("Invalid alphabet. Try again!")
        seq = input("Enter sequence: ")
        valid_seq(seq, command)


dic_command = {'transcribe': transcribe,
               'complement': complement,
               'reverse': reverse}

while state:

    commands = input("Enter command: ").replace(",", "").split(" ")
    if commands[0].lower().startswith('exit'):
        print('Good luck')
        break
    whole_commands = ""
    len_commands = len(commands)
    for i, command in enumerate(commands):
        whole_commands = f"{commands[len_commands - 1 - i]}({whole_commands}"

        valid_command(command)

    nuc_seq = input("Enter sequence: ")
    valid_seq(nuc_seq, command)
    nuc_seq = seq

    print(eval(f"{whole_commands}'{nuc_seq}'{len_commands * ')'}"))

