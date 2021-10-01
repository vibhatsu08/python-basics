#python program to check if a given number is a prime number or not
number = int(input())
flag = False
for i in range(2, number):
    if number%i == 0:
        flag = True
        break

if flag == False:
    print("prime number")
elif flag == True:
    print("not prime number")