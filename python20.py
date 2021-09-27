#python program to find the LCM of two natural numbers
def LCM(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2
        
        while(True):
            if ((greater%num1 == 0) and (greater%num2 == 0)):
                lcm = greater
                break
            greater += 1
        return lcm
number1 = int(input())
number2 = int(input())
print(LCM(number1, number2))