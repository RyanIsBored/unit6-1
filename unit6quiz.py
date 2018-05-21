#Ryan Jones
#5/21/18

file = open('engmix.txt')
letter = input('enter a letter: ')

for word in file:
    if word.count(letter)==4:
        print(word.strip())