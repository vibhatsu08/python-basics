# Write a python program to print Fibonacci numbers.
# int input for the number of terms
number_of_terms = int(input());

# function to recursively print the sequence
def printFibonacci(number_of_terms) :
    # returns 1 if the number of terms is less than or equal to 1
    if number_of_terms <= 1 :
        return number_of_terms
    # prints the nextnumber in the sequence by adding the the number that and the number before before that
    else :
        return printFibonacci(number_of_terms-1) + printFibonacci(number_of_terms-2);


# for loop to iterate over the numbers given
for i in range (number_of_terms) :
    if (number_of_terms <= 0) :
        print ("Enter a positive number")
    else :
        print (printFibonacci(i))