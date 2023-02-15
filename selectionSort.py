# Program to implement Selection sort in Python.

def selection_sort (nums) :
    for i in range (len(nums)) :
        minIndex = i
        for j in range (i+1, len(nums)) :
            if nums[minIndex] > nums[j] :
                minIndex = j
        nums[minIndex], nums[i] = nums[i], nums[minIndex]
    return nums
print(selection_sort(nums = [3,5,6,8,6,1,9,4,2,10,6,7,4,6,17,3]))
