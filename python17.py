#python program to reverse a number using while loop
number = int(input())
reverseNumber = 0

while number > 0:
    lastDigit = number%10
    reverseNumber = reverseNumber*10 + lastDigit
    number //= 10
    
print(reverseNumber)
    