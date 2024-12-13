def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped

def read_fasta(filepath):
    from util import read_input
    sequences = {}
    current_id = ""
    for line in read_input(filepath):
        if line[0] == ">":
            header = line
            current_id = header[1:]
            sequences[current_id] = ""
        else:
            sequence = line
            sequences[current_id] += sequence
    return sequences