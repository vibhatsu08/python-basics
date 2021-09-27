#python program to check if a given number is a prime number or not.
number = int(input())
print(type(number))
flag = False

for i in range(2, number):
    if number%i == 0:
        flag = True
        break
    
if flag:
    print("not prime number")
else:
    print("prime number")