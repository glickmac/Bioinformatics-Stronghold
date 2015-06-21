#import file
file = open('rosalind_rna.txt', 'r')
string = file.read()
#initialize list
my_list = list(string)
my_list = [w.replace('T', 'U') for w in my_list]

#print converted list
print ''.join(map(str , my_list))
