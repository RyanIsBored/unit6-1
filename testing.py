file = open('engmix.txt')

word = input('enter a word: ')

inD = False
for line in file:
    line = line.strip()
    if word == line:
        print('in dictionary')
        inD = True
        break

if not inD:
    print('no')
