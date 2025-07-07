# Greatest Common Divisor of Strings
str1 = input()
str2 = input()

quotient = []
div = ''

# Set N(Numerator) and D(denominator) based on size of each string 
if len(str1) <= len(str2):
    N, D = str2, str1
else:
    N, D = str1, str2

# Using each pattern formed in div to remove the elements from each strings
for i in range(len(D)):
    # Create pattern
    div += D[i]
    
    # Replace each pattern in the string with empty value
    remainder1 = N.replace(div, '')
    remainder2 = D.replace(div, '')

    # If both strings are empty then, store the pattern formed to empty the strings
    if remainder1 == '' and remainder2 == '':
        quotient.append(div)

# Print the longest pattern as the answer (last item in the list)
if quotient:
    print(quotient[-1])
# Print empty string if no pattern
else:
    print('')