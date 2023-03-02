def Transpose(M):
    T = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
    return T

mat = [[1,2,3],[4,5,6],[7,8,9]]
T = Transpose(mat)
print(mat,T)