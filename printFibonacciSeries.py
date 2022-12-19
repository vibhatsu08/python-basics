# python program to print the fibonacci series.
def printFibonacci (number) :
    firstNum = 0
    secondNum = 1
    nextNum = 0
    print(firstNum)
    print(secondNum)
    for i in range (number) :
        nextNum = firstNum + secondNum
        firstNum = secondNum
        secondNum = nextNum
        print(nextNum)
    
printFibonacci(10)