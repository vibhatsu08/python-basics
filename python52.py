#python program to count the number of vowels and consonants in a sentence
string = input()
vowels = "aeiou"
vowels_count = 0

for i in string:
    if i in vowels:
        vowels_count += 1

print(vowels_count)