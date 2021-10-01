#python program to check for amstrong numbers in an interval
start = int(input())
end = int(input())

for i in range(start, end):
    temp = i
    sum = 0
    flag = True
    while temp>0:
        remainder = temp%10
        sum += remainder ** len(str(i))
        temp //= 10
    
    if sum == i:
        print(i)