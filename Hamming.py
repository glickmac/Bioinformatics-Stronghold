with open('rosalind_hamm.txt') as file:
    my_list = file.read().splitlines()
def Hamm(x):
    """This function takes two lines of text and returns the hamming distance between them"""
    string_1 = x[0]
    string_2 = x[1]
    count = 0
    list_1 = list(string_1)
    list_2 = list(string_2)
    for x, y in zip(list_1, list_2):
        if x != y:
            count += 1
    return count
print Hamm(my_list)