'''Given an array of integers and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''


'''plan
    -- first loop through the list and find the sum that equals to the target value
    -- we can define the functions to find these'''

def main(list,target):
    for i in list:
        for j in range(1,len(list)):
            foundElement = i + list[j]
            if foundElement == target:
                return list.index(i), j
k = main(list = [2,6,8,9],target=int(input("Enter the target sum element :")))
if k is not None:
    print(f"the target sum pair is found in pair of index {k}")
else:
    print("target is not found")