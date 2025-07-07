# Merge Strings Alternatively
word1 = input()
word2 = input()
merge = ''
length = 0
longer = ''

# Check for lenght of each word to set the loop range to the lowest word size
if len(word1) <= len(word2):
    length = len(word1)
    longer = word2
else:
    length = len(word2)
    longer = word1

# Loop through each index in range length and merge the value at that index
for i in range(length):
    merge += word1[i] + word2[i]

# Adds the remaining values of the word that is longer than the other
merge += longer[length:]

print(merge)