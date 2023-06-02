'''list '''

def replace(list,value1,value2):
    index1 = list.index(value1)
    index2 = list.index(value2)
    list.remove(value2)
    list.insert(index1,value2)
    list.remove(value1)
    list.insert(index2,value1)
    return list
'''output = replace(list = input(),value1=input(),value2=input())'''

