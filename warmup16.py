#Ryan Jones
#5/11/18

file = open('engmix.txt')

numWords = 0
for line in file:
    line=line.strip()
    if len(line)>0 and line[0]=='r' and line[-1]=='j':
        print(line)