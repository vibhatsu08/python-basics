# Sum of Array Elements
# Given an integer array arr of size n, you need to sum the elements of arr.
def sumElement (arr, n) :
    sum = 0
    for i in arr :
        sum += i
    return sum
print(sumElement(arr=[1,2,3], n=3))