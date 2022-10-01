# Write a python program to find out GCD of two numbers.
# function to find the GCD of the two input numbers
def findGCD (num1, num2) :
    # make a variable and set the smaller number as the value
    if (num1 < num2) :
        smaller = num1
    else :
        smaller = num2
        
    # since its a GCD, the GCD for any two given numbers wouldn't be larger than the smallest number of the two input numbers
    for i in range (2, smaller+1) :
        if (num1%i == 0) and (num2%i == 0) :
            gcd = i
            
    return gcd

# input for both the numbers
num1 = int(input())
num2 = int(input())

# prints the GCD for the two numbers
print(findGCD(num1, num2))