# Count the Zeros
# Given an array of size N consisting of only 0's and 1's. The array is sorted in such a manner that all the 1's are placed first and then they are followed by all the 0's. Find the count of all the 0's.

def countZeroes (arr, n) :
    count = 0
    for i in range(n) :
        if arr[i] == 0 :
            count += 1
    return count
print(countZeroes(arr=[0, 0, 0, 0, 0], n=5))