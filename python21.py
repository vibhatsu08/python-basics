#python program to print the factors of a given number
def factors(num):
    for i in range(1, num+1):
        if num%i == 0:
            print(i)
number = int(input())
factors(number)