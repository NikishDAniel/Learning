# a complete program to finding the same letter that occurs in two or three or more lists
'''plan
    -- need a function to take how many lists we need to compare , we can take it from the user
    -- '''
def takeInput(listNumber,list):
    list = []
    numberOfElements = int(input(f"Enter the number of items in your list {listNumber} : "))   
    for i in range(numberOfElements):
        inputFromUser = int(input())
        list.append(inputFromUser)
    return list
    
        
def createList(numberOfList):
    parentList = []
    for listNumber in range(1,numberOfList+1):
        valuedList = takeInput(listNumber,list)
        parentList.append(valuedList)
    return parentList   
parentList = createList(int(input("Enter number of list you need to make : ")))
print(parentList)