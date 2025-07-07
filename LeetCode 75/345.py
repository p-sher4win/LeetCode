# Reverse Vowels of a String
s  = "IceCreAm"

vowels = "aeiouAEIOU"
s = list(s)
i, j = 0, len(s)-1

# for i being < j
while i<j:

    # for value at an index not vowel
    while i<j and s[i] not in vowels:
        i+=1
    while i<j and s[j] not in vowels:
        j-=1

    # swap values for corresponding index
    temp = s[i]
    s[i] = s[j]
    s[j] = temp

    # increment i and j
    i+=1
    j-=1

# print the result list using join()
print(''.join(s))