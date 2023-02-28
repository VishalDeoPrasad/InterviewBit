def matrixSum1(A, B):
    C = A.copy()
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]
    return C

def matrixSum(X, Y):
    result = [[X[i][j] + Y[i][j]  for j in range (len(X[0]))] for i in range(len(X))]
    return result

A = [[1,1,2],[2,1,6],[3,1,5]]
B = [[3,1,2],[2,1,1],[5,2,4]]

X = [[1,2,3], [4,5,6], [7,8,9]] 
Y = [[9,8,7], [6,5,4], [3,2,1]]

result = matrixSum(A, B)
for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j], end=" ")
    print()
