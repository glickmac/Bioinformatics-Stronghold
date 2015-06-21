import re
import urllib2
from Bio import SeqIO

def fasta_reader(fasta):
    my_list = fasta.split('\n')
    new_list = my_list[1:]
    return ''.join(new_list)


def location_finder(file):
    """
    This Function finds the N-glycosolation motif in protein fasta files"""
    with open(file) as ascencion:
        my_string = ascencion.read()

    #Create and format list of ascension numbers
    my_list = my_string.split('\n')
    my_list = my_list[:-1]

    #Loop through ascension list to pull fasta records from uniprot
    for item in my_list:
        url = 'http://www.uniprot.org/uniprot/'+ item +'.fasta'
        request = urllib2.urlopen(url)  # Open records from Uniport
        protein_url = request.read()   # Open reads for reading into python
        protein_seq = fasta_reader(protein_url)  # Return fasta sequence as string

        matches = [x.start() for x in re.finditer('(?=N[^P][ST][^P])', protein_seq)]  # Search for match positions in string
        new_match = []

        # Add 1 to position in string to get actual position rather than python position
        for y in matches:
            val = y + 1
            new_match.append(str(val))

        # Print formatted item followed by string of integer positions
        if len(new_match) != 0:
            print item
            print ' '.join(new_match)
        else:
            continue


location_finder('rosalind_mprt.txt')

