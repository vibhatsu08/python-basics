#python program to print the pyramid patterns
#half pyramid
rows = 5

for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    print("\n")
    
#half pyramid with numbers 1
for i in range(rows):
    for j in range(i+1):
        print(i+1, end="")
    print("\n")
    
#half pyramid with numbers 2
for i in range(rows):
    for j in range(i+1):
        print(j+1, end="")
    print("\n")  
    
#inverted half pyramid
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print("\n")  
    
#half pyramid with numbers 1
for i in range(rows, 0, -1):
    for j in range(i):
        print(i, end="")
    print("\n")
    
#half pyramid with numbers 2
for i in range(rows, 0, -1):
    for j in range(i):
        print(j+1, end="")
    print("\n")
    
        
