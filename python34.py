#python program to check if a number is even or odd
number = int(input())
if number > 0:
    if number%2 == 0:
        print("even")
    elif number%2 != 0:
        print("odd")