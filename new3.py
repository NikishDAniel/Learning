number = input("Enter your phone number :").replace("",' ').split()
'''result = list(x for x in number if x.isnumeric())
if len(result) == 10:
    print('true')
else:
    print('false')
    
    '''
'''result = [1,2,3,4,5,6,7]
print(list(filter(lambda x:x%2 == 0,result)))'''
result = list(filter(lambda x : x.isnumeric(),number))
if len(result) == 10:
    print('true')
else:
    print('false')