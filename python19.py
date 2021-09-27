#python program to find the HCF/GCD of two given numbers.
def HCF(num1, num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
        
    for i in range(1, smaller+1):
        if ((num1%i == 0) and (num2%i == 0)):
            hcf = i
    return hcf
    
number1 = int(input())
number2 = int(input())
print(HCF(number1, number2))