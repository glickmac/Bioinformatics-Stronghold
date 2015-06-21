import re
with open("rosalind_subs.txt") as file:
    my_string, sub = file.readlines()
    my_string = my_string.rstrip()
    sub = sub.rstrip()



locations = []

#Start & end of a query sequence
for i in range(0, len(my_string)-len(sub)+1):
    if my_string[i:i+len(sub)] == sub:
        locations.append(str(i+1))
        locations.append(str((i+1)+len(sub)))

print ' '.join(locations)

