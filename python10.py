#python program to print all the prime numbers in a given interval.
start = int(input())
end = int(input())

for i in range(start, end):
    for j in range(2, i):
        if i%j == 0:
            break
        else:
            print(j)
            
            