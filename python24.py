#list comprehension
#before list comprehension
def countNegatives():
    negativeNums = [-1, 3, 2, -5, 8, 9, -4]
    negativeNumsCount = 0
    
    for negativeNum in negativeNums:
        if negativeNum < 0:
            negativeNumsCount += 1
    print(negativeNumsCount)

countNegatives()

#after list comprehension
def countNegatives1():
    negativeNums = [-1, 3, 2, -5, 8, 9, -4]
    negativeNumsCount = 0
    
    return (negativeNum for negativeNum in negativeNums if negativeNum < 0 )
print(countNegatives1())