def matrixSum(mat):
    sum = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            sum += mat[i][j]
    return sum

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(matrixSum(mat))