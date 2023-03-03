#print all diagonal from right to left mat[4][6]

def diagonalPrinting(mat, M, N):
    for k in range(M):
        i, j = 0, k
        while (i<N and j>=0):
            print(mat[i][j], end=" ")
            i += 1
            j -= 1
    
    for k in range(1, N):
        i, j = k, M-1
        while i<N and j>=0:
            print(mat[i][j], end = " ")
            i += 1
            j -= 1
mat = [[1,2,3,3.5],[4,5,6,7.5],[7,8,9,9.5]]
diagonalPrinting(mat, 3, 4)