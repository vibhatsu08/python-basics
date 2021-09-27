#python program to print the fibonacci sequence 
num1 = 0
num2 = 1
end = 10

print(num1)
print(num2)

for i in range(0, end):
    nextTerm = num1 + num2
    num1 = num2
    num2 = nextTerm
    
    print(nextTerm)