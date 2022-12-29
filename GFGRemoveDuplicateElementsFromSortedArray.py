# Remove duplicate elements from sorted Array
# Given a sorted array A[] of size N, delete all the duplicated elements from A[]. Modify the array such that if there are X distinct elements in it then the first X positions of the array should be filled with them in increasing order and return the number of distinct elements in the array.

# This method is done using an other array to check if the element is present in it or not.
def remove_duplicate (A, N) :
    newArr = []
    for i in range(N) :
        if A[i] not in newArr :
            newArr.append(A[i])
    return newArr
    
print(remove_duplicate(A=[2,2,2,2,2,4,4], N=7))
