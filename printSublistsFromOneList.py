# Print all sublists of a list in Python

def printSublists (numbers) :
    sublists = []
    for i in range(len(numbers)+1) :
        for j in range(i) :
            sublists.append(numbers[j:i])
    return sublists
print(printSublists(numbers=[1,2,3,4]))

# so what's basically happening in this program: 
# first, a loop is created to loop through the numbers list.
# second, an other loop is created, a nested loop to loop through the element from 0 to i, and the above loop is till length+1, because throughout the iteration, the counter will iterate till i-1.
# now, once the loops are created, the next step is to print the sublists of the given list.
# to do that, we need to use slicing from j to i, to remove all the sublists in the parent list.
