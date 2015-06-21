import re

def gc_content(x):
    """This function takes a text file with multiple fasta and returns the gc content of each sequence"""
    content = 0
    count = 0

    for line in x:
        line = line.strip("\n")

        if not line.startswith(">"):
            content += len(re.findall("[GC]", line))
            count += len(re.findall("[ACGT]", line))
    content = (content/float(count))*100
    return content

with open("rosalind_gc.txt") as file:
#Split string into list by >
    my_list = list(file.read().split('>')[1:])
#Find the list with highest GC
highgc = 0
for x in my_list:
    if gc_content(x) > highgc:
#Print list value with highest gc
        print x
#May print out more than one value, use last value printed
        highgc = gc_content(x)

print highgc