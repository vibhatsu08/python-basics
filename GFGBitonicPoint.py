# Bitonic Point
# Given an array arr of n elements that is first strictly increasing and then maybe strictly decreasing, find the maximum element in the array.
# Note: If the array is increasing then just print the last element will be the maximum value.

def findMaximum (arr, n) :
    max = arr[0]
    for i in range (len(arr)) :
        if (arr[i] > max) :
            max = arr[i]
    return max

print(findMaximum(n=9, arr=[1,15,25,45,42,21,17,12,11]))
