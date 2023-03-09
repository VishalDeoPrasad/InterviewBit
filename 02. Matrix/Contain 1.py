#given a 2D Matrix every element is 0/1, every row sorted. find the first column which contain 1.
def firstContain(A):
    row = len(A)
    col = len(A[0])
    i, j = 0, col-1
    while i < row and j >= 0:
        if A[i][j] == 1:
            j -= 1
        if A[i][j] == 0:
            i += 1
        if j == col-1:
            return -1
    return j+1

A = [[0,0,0,1,1],[0,0,0,0,0],[1,1,1,1,1],[0,0,0,1,1],[0,0,0,1,1],[0,0,0,1,1]]
A2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print(firstContain(A))
