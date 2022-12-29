# K-th element of two sorted Arrays
# Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K. The task is to find the element that would be at the k’th position of the final sorted array.

def kthElement (arr1, arr2, n, m, k) :
    arr1.extend(arr2)
    temp = 0
    for i in range (len(arr1)) :
        for j in range (i+1, len(arr1)) :
            if arr1[j] < arr1[i]  :
                temp = arr1[j]
                arr1[j] = arr1[i]
                arr1[i] = temp
    return arr1[k-1]
print(kthElement(arr1=[2, 3, 6, 7, 9], arr2=[1, 4, 8, 10], n=5, m=4, k=5))
    

"""Example 1:

Input:
arr1[] = {2, 3, 6, 7, 9}
arr2[] = {1, 4, 8, 10}
k = 5
Output:
6
Explanation:
The final sorted array would be -
1, 2, 3, 4, 6, 7, 8, 9, 10
The 5th element of this array is 6."""

"""Input:
arr1[] = {100, 112, 256, 349, 770}
arr2[] = {72, 86, 113, 119, 265, 445, 892}
k = 7
Output:
256
Explanation:
Final sorted array is - 72, 86, 100, 112,
113, 119, 256, 265, 349, 445, 770, 892
7th element of this array is 256."""