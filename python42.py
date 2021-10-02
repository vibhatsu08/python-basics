#python program to display fibonacci series using recursion
def display_fib(num):
    if num<=1:
        return num
    else:
        return display_fib(num-1) + display_fib(num-2)

number = int(input())

for i in range(number):
    print(display_fib(i))