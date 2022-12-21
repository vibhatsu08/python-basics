# Wave Array
# Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place).
# In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
# If there are multiple solutions, find the lexicographically smallest one.

def convertToWave (n, a):
    for i in range (0, n-1, 2):
        a[i], a[i+1] = a[i+1], a[i]
    return a
        
            
print(convertToWave(n=6, a=[1,2,3,4,5,6]))

        