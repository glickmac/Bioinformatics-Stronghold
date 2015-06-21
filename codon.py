with open("rosalind_prot.txt", "r") as myfile:
    data = myfile.read()
    mRNA = data
map = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
       "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
       "UAU": "Y", "UAC": "Y", "UAA": "XX", "UAG": "XX",
       "UGU": "C", "UGC": "C", "UGA": "XX", "UGG": "W",
       "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
       "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
       "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
       "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
       "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
       "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
       "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
       "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
       "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
       "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
       "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
       "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }

start = mRNA.find('AUG')
newseq = ""
if start!= -1:
    while start+2 < len(mRNA):
        codon = mRNA[start:start+3]
        if codon == "UAG": break;
        if codon == "UAA": break;
        if codon == "UGA": break;
        newseq = newseq + map[codon]
        start+=3
    print newseq
