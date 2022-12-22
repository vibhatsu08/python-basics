# Find duplicates in an array
# Given an array a[] of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array.
# Note: The extra space is only for the array to be returned.
# Try and perform all operations within the provided array. 
def duplicates (arr, n) :
    count = {}
    result = []
    for i in range(n) :
        if arr[i] in count :
            count[arr[i]] += 1
        else :
            count[arr[i]] = 1
            
    for key, values in count.items() :
        if values > 1 :
            result.append(key)
    result = sorted(result)
    
    if len(result) == 0 :
        return [-1]
    return result
        
print(duplicates(arr=[13,9,2,1, 1, 0, 22,25, 13, 22, 20, 3, 8, 11, 25, 10, 3, 15, 11, 19, 20, 2, 4, 25, 14, 23, 14], n=26))
                
