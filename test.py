######## Problem  4  ###############

#print a multiplication table like below.
#get user intput for start and end numbers. 
#the following example uses 1 to 5.

'''   1  2  3  4  5
  ********************
1 |  1  2  3  4  5
2 |  2  4  6  8 10
3 |  3  6  9 12 15
4 |  4  8 12 16 20
5 |  5 10 15 20 25'''
def printX():
  for i in range(startNumber,endNumber+1):
    if i == startNumber:
      print(f'  {i}',end=" ")
    else:
      print( i,end = "  ")
  print()
  print(f" ********************")

startNumber = int(input("Enter the starting number : "))
endNumber = int(input("Enter the ending number : "))
for i in range(2):
  if i == 0:
    printX()
  else:
    for i in range(startNumber,endNumber+1):
        for j in range(startNumber,endNumber+1):
            mul = i*j
            if j== startNumber:
                print(f'{i} | {mul}',end = ' ')
            else:
                print(f'{mul}',end = ' ')
        print()
