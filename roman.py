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
    
roman = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000   
}
def sumNumber(a,b):
    output = a+b
    return output
def diff(a,b):
    output = abs(a-b)
    return output   
def checkPos(list1):
    result = 0
    for pos in range(len(list1)-1):
        if list1[pos]>list1[pos+1]:
            result += sumNumber(list1[pos],list1[pos+1])
        elif list1[pos]<list1[pos+1]:
            result += diff(list1[pos],list1[pos+1])
        elif list1[pos]==list1[pos+1]:
            result = sumNumber(result,list1[pos])
    return result
def count(splited):
    list1 = []
    for str in splited:
        list1.append(roman[str])      
    result = checkPos(list1)
    return result
def inputSplit(romanInput):
    splited = romanInput.split()
    li = count(splited)
    return li
romanInput = input("Enter the roman integer : ").upper().replace(""," ")
print(inputSplit(romanInput))