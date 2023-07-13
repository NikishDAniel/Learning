'''checking whether the number is prime or not'''
def checkPrime(number):
    for i in range(2,number+1):
        if number%i == 0:
            break
        else:
            return True
    
number = int(input('Enter'))