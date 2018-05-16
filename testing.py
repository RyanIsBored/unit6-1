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
    
  
-----    

file = open('engmix.txt')
num = int(input('enter a number: ')

L = []

for line in file:
    line = line.strip()
    L.append(line)
    
print(L[num-1])



-----



file = open('lastWordDemo.py')

for line in file:
    print(line.strip()+ ('!')


-----



file = open('engmix.txt')
letter = input('Enter a letter: ')

mostchar = ''
for line in file:
    line = line.strip()
    if line.count(letter) > mostchar.count(letter):
        mostchar = line

print(mostchar)



