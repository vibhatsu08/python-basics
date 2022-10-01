# Write a python program to print identity matrix.
# input for the matrix, int because the input is taken as a string
n = int(input())

# first loop to loop through rows
for i in range (0, n) :
    # second loop to loop through columns
    for j in range (0, n) :
        # prints "1" if row == column
        # end="" is here so that the numbers stay on the same line if told otherwise
        if (i == j) :
            print ("1", end="")
        # prints "0" otherwise
        else :
            print ("0", end="")
    print()
        