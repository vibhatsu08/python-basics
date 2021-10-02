#python program to convert a decimal number to binary
def decimal_to_binary(num):
    if num > 1:
        decimal_to_binary(num//2)
    print(num%2, end="")

number = int(input())
decimal_to_binary(number)

    
    
    
