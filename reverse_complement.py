file = open('rosalind_revc.txt', 'r')
string = file.read()
#convert string into list of individual characters
my_list = list(string)
#flip list
my_list.reverse()
#Replace list strings with lower case to prevent unwanted transitions
my_list = [w.replace('T', 'a') for w in my_list]
my_list = [w.replace('A', 't') for w in my_list]
my_list = [w.replace('C', 'g') for w in my_list]
my_list = [w.replace('G', 'c') for w in my_list]
#convert list to string
lisp = ''.join(map(str , my_list))
#return to uppercase and print
print lisp.upper()