# Python program to calculate the sum of rows, columns and diagonals in a given 2d Array.
def calculateSum (arr) :
    rows = len(arr)
    columns = len(arr[0])
    rowSum, colSum, firstDiag, secondDiag = 0, 0, 0, 0
    
    for i in range (0, rows) :
        for j in range (0, columns) :
            rowSum += arr[i][j]
            
    for i in range (0, rows) :
        for j in range (0, columns) :
            colSum += arr[i][j]
            
    for i in range (0, len(arr)) :
        firstDiag += arr[i][i]
        secondDiag += arr[i][len(arr)-i-1]
        
    return rowSum, colSum, firstDiag, secondDiag
print(calculateSum(arr=[    
        [2, 2, 3],  
        [4, 5, 6],  
        [7, 8, 9]  
    ]))