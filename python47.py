#python program to find the transpose of a given matrix
m1 = [[1,2,3], [4,5,6], [7,8,9]]

result = [[1,1,1], [1,1,1], [1,1,1]]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        result[i][j] = m1[j][i]
        
for r in result:
    print(r)