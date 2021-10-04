#python program to iterate over a dictionary using a for loop
stuff = {1:"one", 2:"two", 3:"three", 4:"four"}
#iterate over a dictionary using the items() method
for key, value in stuff.items():
    print(key, value)
    
#iterate over a dictionary without using the items() method
for key in stuff:
    print(key, stuff[key])