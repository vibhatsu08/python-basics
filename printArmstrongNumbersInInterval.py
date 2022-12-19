# Python program to print Armstrong numbers in an interval.
def printArmstrongNumbers (lower, upper) :
    for num in range (lower, upper+1) :
        # need to check if the number is an armstrong number or not for every number in the range.
        length = len(str(num))
        newNumber = 0
        temp = num
        while (temp > 0) :
            remainder = temp%10
            newNumber += remainder**length
            temp //= 10
            
        if num == newNumber:
            print(num)
        # print(i)
        
printArmstrongNumbers(100, 600)