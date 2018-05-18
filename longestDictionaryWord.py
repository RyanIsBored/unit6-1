#Ryan Jones
#5/10/18

file = open('engmix.txt')

longest = ''
for words in file:
    word = words.split(' ')
    if len(words)>len(longest):
        longest = words
print(longest)