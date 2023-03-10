def findElement(Mat, elem):
    M = len(Mat)
    N = len(Mat[0])
    i, j = 0, N-1
    while i<M and j >= 0:
        if Mat[i][j] < elem:
            i += 1 #skip row
        elif Mat[i][j] > elem:
            j -= 1 #skip col
        elif Mat[i][j] == elem:
            return i*1009 + j
    return False





mat = [[1,2,3,4],[4,5,6,7],[7,8,9,10], [11,12,13,14]]
mat1 = [[1,2,3,4],[23,5,6,7],[7,8,9,10], [11,12,13,14], [15,16,17,18], [19,20,21,22]]
mat2 = [[1,2,3,4,5,6],[4,5,6,7,8,9],[7,8,9,10,11,12], [11,12,13,14,13,14]]

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = 2
A = [[1, 2],
     [3, 3]]
B = 3
print(findElement(A,B))