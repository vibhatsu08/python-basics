#dissecting the program
print("hello world!") #for printing statements

#getting user input
myName = input()
print("my name is " + myName)

#finding the length of a given string
#string
nameLength = len(myName)
print(nameLength)

#str() function
numberStr = str(20)
print(numberStr)
print(len(numberStr))

#int() function
numberInt = 20.53
print(numberInt)
print(int(numberInt))

#float() function
numberFloat = 20
print(numberFloat)
print(float(numberFloat))

#round() function
numberRound = 20.91
print(int(numberRound)) #int() function converts the rounds the number to the number before the decimal place. for example 20.91 becomes 20.
print(round(numberRound)) #round() function converts the given number to the number closest. for example 20.91 gives 21 returns an int number.