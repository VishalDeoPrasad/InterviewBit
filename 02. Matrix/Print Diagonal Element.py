#print all diagonal from right to left mat[4][6]

def diagonalPrinting(mat, N, M):
    for k in range(M):     #print all diagonal staring from 0th row
        i, j = 0, k
        while (i<N and j>=0):
            print(mat[i][j], end=" ")
            i += 1
            j -= 1
    
    for k in range(1, N):  #print all diagonal staring from M-1 columns
        i, j = k, M-1
        while i<N and j>=0:
            print(mat[i][j], end = " ")
            i += 1
            j -= 1

mat = [[1,2,3,4],[4,5,6,7],[7,8,9,10], [11,12,13,14]]
mat1 = [[1,2,3,4],[4,5,6,7],[7,8,9,10], [11,12,13,14], [15,16,17,18], [19,20,21,22]]
mat = [[1,2,3,4,5,6],[4,5,6,7,8,9],[7,8,9,10,11,12], [11,12,13,14,13,14]]
diagonalPrinting(mat, 4, 4)