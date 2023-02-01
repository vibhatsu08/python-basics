# Program to implement Insertion Sort in Python.

def insertion_sort (nums) :
    for i in range (1, len(nums)) :
        currentIndex = i
        while (currentIndex > 0) and (nums[currentIndex] < nums[currentIndex-1]) :
            nums[currentIndex], nums[currentIndex-1] = nums[currentIndex-1], nums[currentIndex]
            currentIndex -= 1
    return nums
print(insertion_sort(nums = [7,3,2,5,6,10,9,8,1]))