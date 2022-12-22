# Subarray with given sum
# Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S and return the left and right index(1-based indexing) of that subarray.
# In case of multiple subarrays, return the subarray indexes which comes first on moving from left to right.
# Note:- Both the indexes in the array should be according to 1-based indexing. You have to return an arraylist consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.

def subArraySum (arr, n, s) :
    subarray = []
    sum = 0
    for i in range(len(arr)+1) :
        for j in range(i) :
            sum += j
            if sum == s :
                
                break
                