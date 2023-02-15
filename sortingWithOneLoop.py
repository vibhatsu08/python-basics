# Trying to sort an array using one single loop, following the method given by GFG on their website.

def sortArray (arr) :
    j = 0
    while (j < len(arr)-1) :
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j = -1
        j += 1
    return arr
print(sortArray(arr=[2,3,1,3,2,4,6,7,9,2,19]))