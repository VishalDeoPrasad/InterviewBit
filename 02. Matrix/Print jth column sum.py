def colSum(mat, k):
    sum = 0
    for row in range(len(mat)):
        sum += mat[row][k]
    print(sum)


mat = [[1,2,3],[4,5,6],[7,8,9]]
colSum(mat,2)