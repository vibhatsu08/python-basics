#python program to sort a string alphabetically
string = input()
words = [word.lower() for word in string.split()]
words.sort()

for word in words:
    print(word)