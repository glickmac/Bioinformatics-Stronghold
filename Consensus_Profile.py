import numpy as np

files = "rosalind_cons.txt"


def rosalind_parser(files):
    """This function takes a fasta file format and parsers it into
    a dictionary with the sequence and ID.
    :param files: a fasta file format with a header designated by > and corresponding sequence
     Output: a dictionary with headers as keys and sequences as values
    """
    with open(files, 'r') as file_f:  # Open file as read only
        my_string = file_f.read()
        my_list = my_string.split('\n')
    return my_list

def count_matrix(list):
    a = len(list[0])
    score = np.mat([[0]*a for x in range(4)])
    for i in range(4):
        for j in range(a):
            if i == 'A':
                score[i][1] = score[i][1] + 1
            elif i == 'C':
                score[i][2] = score[i][2] + 1
    print score

test = ['ACGTTT', 'AGCTTT', 'ACCTTT', 'AGGTTT','TGAGTT']

count_matrix(test)