'''looping: 1. for loop 2. while loop'''
'''1/2 '''
'''print("daniel")
print("daniel")
print("daniel")
print("daniel")
print("daniel")'''
'''formatting strings - f'''
# 1 2 3 4 

'''for i in range(1,5):
    k = i%2
    if k!=0:
        print(f"{i}*daniel")'''
# daniel -- 1,daniel ,2, daniel

'''1 - 50 even numbers '''
'''sum = 0 
for i in range(1,51):
    if i%2 == 0:#even
        sum += i
print(sum)
'''
'''
string1 = "Barath"
for i in range(len(string1)):
    print(string1[i])'''

'''print(string1[1])
print(string1[2])
print(string1[3])
for i in string1:
    print(i)'''
string1 = "1221"
store = list(reversed(string1))
print(store)
output = "".join(store)
print(output)