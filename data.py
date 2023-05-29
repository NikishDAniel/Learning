'''Given an array of integers and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''


'''plan
    -- first loop through the list and find the sum that equals to the target value
    -- we can define the functions to find these'''
    
digits = [9]
length = len(digits)-1
old = digits[length]
new = digits[length] + 1
digits.remove(old)
if new > 9:
    stry = str(new)
    stry = stry.replace(""," ").split()
    for i in stry:
        i = int(i)
        digits.append(i)
else:
    digits.append(new)
print(digits)