'''There are two arrays of numbers. the numbers are sorted in ascending order. 
Find the numbers that are common in both arrays. 
Eg - array 1 = [1,3,7,9,13,14], array2 [1,2,7,13,15]. answer - [1,7,13]'''

array1 =  [1,3,7,9,13,14]
array2 = [1,2,7,13,15]
answer = []
for i in array1:
    if i in array2:
        answer.append(i)
print(answer)
