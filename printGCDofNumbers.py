# Python program to print the HCF or the GCD of two numbers
def printGCD (num1, num2) :
    if num1 > num2 :
        num1, num2 = num2, num1
    print(num1, num2)
    GCD = 0
    for i in range (2, num1+1) :
        if ((num1%i == 0) and (num2%i == 0)) :
            GCD = i
    return GCD
        
print(printGCD(10, 20))