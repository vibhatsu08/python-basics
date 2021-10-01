#program to print the factorial of a number
number = int(input())
fact = 1
for i in range(1, number+1):
    fact *= i

print(fact)