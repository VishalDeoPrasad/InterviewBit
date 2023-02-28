def rowSum(mat, k):
    sum = 0
    for col in range(len(mat[0])):
        sum += mat[k][col]
    print(sum)


mat = [[1,2,3],[4,5,6],[7,8,9]]
rowSum(mat, 2)