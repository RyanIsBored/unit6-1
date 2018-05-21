
file = open('engmix.txt')

#
'''
for word in file:
    if word.strip()[0]=='z' and word.strip()[-1]=='n':
        print(word.strip())
        break
'''

for word in file:
    if word.count('q')==2:
        print(word.strip())