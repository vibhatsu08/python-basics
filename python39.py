#python program to check armstrong number
number = int(input())
temp = number
sum = 0

while(temp > 0):
    remainder = temp%10
    sum += remainder ** len(str(number))
    temp //= 10
    
print(sum)
if sum == number:
    print("armstrong number")
else:
    print("not armstrong number")