#python program to check if a number is positive, negative or zero
number = input()
number = int(number)

if number < 0:
    print("negative number")
elif number > 0:
    print("positive number")
elif number == 0:
    print("zero")