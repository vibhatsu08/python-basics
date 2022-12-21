# Largest Element in Array
# Given an array A[] of size n. The task is to find the largest element in it.
def largest (arr, n) :
    max = arr[0]
    for i in range(len(arr)) :
        if arr[i] > max :
            max = arr[i]
    return max
print(largest(arr=[1, 8, 7, 56, 90], n=5))