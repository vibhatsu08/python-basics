#python program to print all the armstrong numbers in a given interval
start = 1
end = 500

for i in range(start, end+1):
    order = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        lastDigit = temp % 10
        sum += lastDigit ** order
        temp //= 10
        
        if i == sum:
            print(i)
        