def rowSum(mat):
    for i in range(len(mat)):
        print(sum(mat[i]))

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(rowSum(mat))