#Ryan Jones
#5/17/18

file = open('engmix.txt')

for line in file:
    if 'jones' in line:
        print(line.strip())
    