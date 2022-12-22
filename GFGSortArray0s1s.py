# Sort an array of 0s, 1s and 2s
# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

def sort012 (arr, n) :
    arr.sort()
    return arr
print(sort012(arr=[0,2,1,2,0], n=5))