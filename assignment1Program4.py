# Write a python program to replace all the occurrences of 'e' by "7" in the given string.
# with using the built in replace() method in python
# string input
sent1 = input()
# replace method replaces all the occurrences of the mentioned first parameter with the second parameter.
sent2 = sent1.replace("e", "7")
print(sent2)

# without using the built in replace() method in python. 
# string input
str = input()
newStr = ""

# iterating through the given string
for i in range (0, len(str)) :
    # replaces the 'e' with '7' when it comes across the loop 
    if (str[i] == "e") :
        newStr += "7"
    else :
        newStr += str[i]
        
print(newStr)