# Find minimum and maximum element in an array
# Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.

def getMinMax (n, a) :
    min = a[0]
    max = a[0]
    
    for i in range (len(a)) :
        if a[i] < min :
            min = a[i]
        if a[i] > max :
            max = a[i]
    return "min = {}, max = {}".format(min, max)
        
print(getMinMax(n=5, a=[1, 345, 234, 21, 56789]))
        
    