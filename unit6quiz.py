#Ryan Jones
#5/21/18

file = open('engmix.txt')


#program #1
'''
letter = input('enter a letter: ')

for word in file:
    if word.count(letter)==4:
        print(word.strip())
'''


#program #3
'''
number = int(input('enter a number: '))
letter = input('enter a letter: ')
for word in file:
    if word.strip()[0]==letter and len(word.strip())==number:
        print(word.strip())
'''        

wcount = 0
for word in file:
    if len(word.strip())>=10:
        wcount+=1
    if wcount==8000:
        print(word.strip())