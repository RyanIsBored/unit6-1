#Ryan Jones
#5/17/18

file = open('engmix.txt')

for line in file:
    if 'j' in line and 'o' in line and 'n' in line and 'e' in line and 's' in line:
        print(line.strip())
    