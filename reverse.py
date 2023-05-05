'''message = "My Name is Sam"
print(''.join(reversed(message)))'''

def rreverse(message):
    reversedString = message[::-1]
    return reversedString
reverseString = rreverse(input("Enter the string to be reversed : "))
print(reverseString)