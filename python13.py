#python program to check if a given number is an armstrong number or not.
number = int(input())
order = len(str(number))

temp = number
sum = 0

while temp > 0:
    lastDigit = temp % 10
    sum += lastDigit ** order
    temp //= 10
    
print(sum)

if number == sum:
    print("given number is an armstrong number")
else:
    print("given number is not an armstrong number")
