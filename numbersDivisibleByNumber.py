# Python program to find numbers divisible by another number
def checkDivisiblity (numbers, number) :
    for num in numbers :
        if num%number == 0 :
            return num
        
print(checkDivisiblity(numbers=[12, 65, 54, 39, 102, 339, 221,], number=12))