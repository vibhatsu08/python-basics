#python program to check if a given number is a fibonacci number or not
def isFibonacci(num):
    temp = num
    tempNum = num
    num1 = 0
    num2 = 1
    flag = False
    for i in range(0, temp+1):
        tempNum = num1 + num2
        num1 = num2
        num2 = tempNum
        print(tempNum)
        
        if tempNum == num:
            flag = True
            break
        else:
            flag = False
    
    if flag == True:
        print("yes")
    elif flag == False:
        print("no")

number = int(input())
isFibonacci(number)