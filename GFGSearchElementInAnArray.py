# Search an Element in an array
# Given an integer array and another integer element. The task is to find if the given element is present in array or not.

def search (arr, N, X) :
    for i in range (len(arr)) :
        if X == arr[i] :
            return i
    return -1
        
print(search(arr=[1,2,3,4,5], N=5, X=5))
