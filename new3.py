number = input("Enter your phone number :")
if len(number) == 10:
    for i in number:
        if i.isnumeric():
            print("valid")
        else:
            print("not valid")
else:
    print("try to add more digits")