#python program to print the fibonacci series
end = int(input())
num1 = 0
num2 = 1
print(num1)
print(num2)
for i in range(0, end):
    temp = num1 + num2
    num1 = num2
    num2 = temp
    print(temp)