#python program to generate a random number
import random

start = input()
start = int(start)
end = input()
end = int(end)

randomNumber = random.randint(start, end)
print(randomNumber)