def colSum(mat):
    for i in range(len(mat)):
        temp_sum = 0
        for j in range(len(mat[0])):
            temp_sum += mat[j][i]
        print(temp_sum)
        temp_sum = 0
        
mat = [[1,2,3],[4,5,6],[7,8,9]]
colSum(mat)
