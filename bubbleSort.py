# Program to implement Bubble Sort in Python.

def bubble_sort (nums) :
    swapped = True
    while swapped :
        swapped = False
        for i in range (len(nums)-1) :
            if nums[i] > nums[i+1] :
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True
    return nums
print(bubble_sort(nums=[5,2,45,6,3,56,7,3,2,45,6,78,12,1,4,5,1]))