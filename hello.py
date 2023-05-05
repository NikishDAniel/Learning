print("hello world")
#printing hello world
'''
Given two arrays a[] and b[] of size n and m respectively. 
The task is to find the number of elements in the union between these two arrays.
Union of the two arrays can be defined as the set containing distinct elements from both the arrays. 
If there are repetitions, then only one occurrence of element should be printed in the union.
Note : Elements are not necessarily distinct
'''

list1 = [5,3]
list2 = [1,2,3,4,5]
list3 = [1,2,3]
union = []
u = list1+list2+list3
print(sorted(u,reverse=True))


