#python program to print the sum of n natural numbers
number = int(input())
sum = 0

for i in range(number+1):
    sum += i
    
print(sum)