#Ryan Jones
#5/10/18

file = open('engmix.txt')

for line in file:
    words = line.split()
    mostchar = words.count(2)
print(mostchar)