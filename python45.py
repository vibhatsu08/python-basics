#python program to add two matrices
m1 = [[1,2,3], [4,5,6], [7,8,9]]
m2 = [[1,2,3], [4,5,6], [7,8,9]]

result = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(m1)): #iterate through rows 
    for j in range(len(m1[0])): #iterate through columns
        result[i][j] = m1[i][j] + m2[i][j]
        
for r in result:
    print(r)