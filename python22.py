#python program for the implementation of lists
#program to enter the values of all the avengers in a list using a loop
avengers = []
while True:
    name = input()
    
    if name == '':
        break
    else:
        avengers = avengers + [name] #string concatenation
        
print(avengers)
