# Missing number in matrix
# Given a matrix of size n x n such that it has only one 0, Find the positive number (greater than zero) to be placed in place of the 0 such that sum of the numbers in every row, column and two diagonals become equal. If no such number exists, return -1.
# Note: Diagonals should be only of the form matrix[i][i] and matrix[i][n-i-1]. n is always greater than 1.

def MissingNo (matrix) :
    rows, cols = len(matrix), len(matrix[0])
    rowSum, colSum, diagSum1, diagSum2 = 0, 0, 0, 0
    missingNumber = 0
    
    # sum of rows and columns
    for i in range (0, rows) :
        for j in range (0, cols) :
            rowSum += matrix[i][j]
    