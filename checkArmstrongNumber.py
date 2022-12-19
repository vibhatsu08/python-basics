# Python program to check if a given number is an armstrong number or not.
def checkArmstrong (armstrongNumber) :
    tempNumber = armstrongNumber
    length = len(str(armstrongNumber))
    newNumber = 0
    while tempNumber > 0 :
        remainder = tempNumber%10
        newNumber += remainder**length
        tempNumber //= 10
    print(newNumber)
    if armstrongNumber == newNumber :
        return "armstrong number"
    else :
        return "not armstrong number"
    
print(checkArmstrong(407))