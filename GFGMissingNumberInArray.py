# Missing number in array
# Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

def MissingNumber (array, n) :
    sum = 0
    for i in range (len(array)) :
        sum += array[i]
        
    expectedSum = (n*(n+1))/2 #15
    
    missingNumber = expectedSum - sum
    return int(missingNumber)

print(MissingNumber(n=10, array=[6,1,2,8,3,4,7,10,5]))