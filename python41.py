#program to find the factors of a given number
number = int(input())
flag = False
for i in range(1, number+1):
    if number%i == 0:
        print(i)
        
    