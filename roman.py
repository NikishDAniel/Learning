'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.'''
'''plan
    -- take input from the user
    -- create a dictionary to hold these values
    -- define a functions to split the string'''
 
 # roman letters dictionary   
roman = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000   
}

# a function to count the total splited
def count(splited):
    result = roman[splited[0]]
    if len(splited) == 2:
        if result < roman[splited[1]]:
            result -= roman[splited[1]]
            result=abs(result)
        else:
            result += roman[splited[1]]
    else:
        for i in range(1,len(splited)-1):
            if splited[i] > splited[i+1] or splited[i] == splited[i+1]:
                result += (roman[splited[i]])
            elif splited[i] < splited[i+1]:
                result += roman[splited[i+1]] - roman[splited[i]]
        if len(splited) % 2 ==0:
            result-=1
    return result    

# input function
def inputSplit(romanInput):
    splited = romanInput.split()
    li = count(splited)
    return li
def takeInput(romanInput):
    #romanInput = input("Enter the roman integer : ").upper()
    romanInput = romanInput.upper()
    input = romanInput.replace(""," ")
    output = inputSplit(input)
    print(f'The number equivalent to     {romanInput}    is ',output)
for i in range(10):
    romanInput = input("enter the roman letter  : ")
    takeInput(romanInput)