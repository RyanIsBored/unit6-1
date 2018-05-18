#Ryan Jones
#5/10/18

file = open('engmix.txt')

longest = ''
for line in file:
    words = line.split()
    if len(words)>len(longest):
        longest = words
print(longest)