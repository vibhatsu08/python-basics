#lists and loops
#program to print the inner characters of a list
names = ["steve", "scott", "tony", "clint"]
for name in names:
    print(name, end = " ")
print("\n")
#program to print all the uppercase characters from a string
string = "thIs is a sUfficientLy lonG strinG to fit in the Screen, baZinGa!"
for char in string:
    if char.isupper():
        print(char, end = "")
print("\n")       
#list comprehension
squares = [n**2 for n in range(10)]
print(squares)

planets = ["earth", "mars", "venus"]
short_planets = [planet for planet in planets]
print(short_planets)
caps_planets = [planet.upper()+'!' for planet in planets]
print(caps_planets)
    