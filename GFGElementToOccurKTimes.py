# First element to occur k times
# Given an array of N integers. Find the first element that occurs at least K number of times.

def firstElementKTime (a, n, k) :
    counts = {}
    firstValue = 0
    for i in a :
        if i in counts :
            counts[i] += 1
        else :
            counts[i] = 1
        if counts[i] == k :
            firstValue = i
            return firstValue
    return -1
        
print(firstElementKTime(a=[4,2,2,2,3,4,4,4,3,2], n=10, k=3))